# Projet « eggs » RNG — Décisions d'architecture et conception du RNG-01

*Compte-rendu de conception. Générateurs physiques de nombres aléatoires inspirés du Global Consciousness Project (Roger Nelson / PEAR), traités comme instrument à faible effet.*

---

## 0. Objet de ce document

Ce document consigne deux choses :

1. les **décisions d'architecture système** auxquelles nous sommes arrivés après avoir passé en revue les plateformes disponibles (Pi 3B, XBee, FPGA à Ethernet, ESP32, Proxmox) ;
2. la **conception détaillée du premier générateur (RNG-01)** : source de bruit, chaîne analogique, comparateur, traversée d'isolation, échantillonnage, et plan de caractérisation au NI USB-6210.

Il sert de référence de travail : tout le traitement en aval (format de log, statistiques, corrélations) suppose que la source analogique du RNG-01 existe et est caractérisée.

---

## 1. Posture épistémologique (rappel structurant)

Le projet est traité comme une **expérience instrumentale à faible effet**, avec une séparation stricte des couches. C'est ce qui distingue un instrument crédible d'une chasse aux anomalies.

```text
Niveau 1  Physique de la source (avalanche)
   ↓
Niveau 2  Bruit analogique
   ↓
Niveau 3  Conversion en bits
   ↓
Niveau 4  Statistiques individuelles
   ↓
Niveau 5  Corrélations inter-RNG
   ↓
Niveau 6  Corrélations avec des événements
   ↓
Niveau 7  Interprétation éventuelle
```

**L'hypothèse « conscience » est la dernière case, jamais la première.** L'issue la plus probable d'un montage rigoureux est un **résultat nul**, et ce résultat nul doit être considéré comme un **succès**, décidé à l'avance. Le mode d'échec à fuir est de « trouver » quelque chose par flexibilité d'analyse (p-hacking, comparaisons multiples).

Deux garde-fous méthodologiques non négociables, retenus dès maintenant :

- **conservation des données brutes** (jamais uniquement les bits « nettoyés ») ;
- **pré-enregistrement du protocole** avant de regarder les données, avec **fenêtres témoins** (« sham events ») passées dans le même pipeline pour servir de contrôle négatif.

---

## 2. Décisions d'architecture système

### 2.1 Principe directeur : eggs autonomes et hors-ligne

La clarification décisive est qu'il **n'y a aucun besoin de temps réel**. L'analyse est entièrement post-hoc, sur des fenêtres pré-enregistrées. Cela autorise la meilleure propriété possible :

> **Le réseau n'a pas besoin d'être actif pendant l'acquisition, seulement pendant la collecte.**

Un canal qu'on ne touche qu'après coup ne peut pas contaminer les fenêtres analysées. Chaque egg journalise localement, seul, sans lien vers les autres pendant les runs. On rapatrie les données **par pull** (`rsync` sur SSH, ou swap de carte SD) **en dehors** des fenêtres d'intérêt.

### 2.2 Ce qui a été écarté, et pourquoi

| Option envisagée | Statut | Raison |
|---|---|---|
| **WiFi (ESP32) + MQTT comme registre** | Écarté comme *registre* | WiFi = canal EM commun **et** horloge commune (AP, DHCP, NTP) → risque de fausse corrélation. MQTT best-effort → pertes de paquets possibles, **potentiellement corrélées** à un événement mondial (pic de trafic Internet) : une corrélation de *drops* réseau déguisée en signal. |
| **XBee** | Écarté | C'est du sans-fil, et sans besoin de temps réel il ne résout **aucun** problème restant. Introduirait un canal EM/synchro commun pour zéro gain. À réserver à un projet où le sans-fil est un atout. |
| **MQTT comme transport live** | Conservé optionnellement | Le protocole n'a jamais été le problème ; sur lien **filaire**, MQTT → base time-series → Grafana reste un bon confort de monitoring, **non autoritatif**. |

**Point clé :** l'ennemi n'était pas *MQTT le protocole* mais *le WiFi le médium* et *MQTT comme registre*. Sur Ethernet câblé, MQTT redevient acceptable — mais comme couche de confort, pas comme source de vérité.

### 2.3 Le temps : GPS + PPS par egg

C'est le choix structurant du sous-système temporel. Chaque egg reçoit **son propre module GPS** (u-blox NEO-6M/7M/8M avec sortie **PPS**) et discipline son horloge locale sur le front PPS via **chrony**.

Pourquoi c'est la bonne réponse ici :

- **Indépendance préservée** : chaque egg a une horloge *matériellement indépendante*, aucun maître partagé.
- **Alignement sub-µs** : tous alignés sur l'UTC à mieux que la microseconde via une référence **céleste commune et passive** (le GPS n'émet rien → aucun canal EM introduit).

> **PTP (IEEE 1588) est volontairement rejeté** : il imposerait une horloge maître partagée sur le réseau, réintroduisant exactement le couplage qu'on veut éviter. Pour un RNG datacenter, PTP gagnerait ; pour *ce* projet dont la prémisse est l'indépendance, GPS-PPS gagne. L'objectif scientifique renverse le meilleur choix d'ingénierie habituel.

**Compromis honnête sur la finesse des fenêtres :**

- fenêtres fines (1 s) → **GPS-PPS requis** ;
- fenêtres grossières (30 s, 1 min) → un **RTC + recalage NTP** à la connexion suffit (un quartz à ±20 ppm ne dérive que ~centaine de ms sur quelques heures).

### 2.4 Registre local autoritatif

L'enregistrement de référence vit **sur chaque egg** (SD/flash), horodaté par l'horloge GPS. La stack réseau (MQTT/DB/Grafana) est explicitement **non autoritative**. Chaque échantillon porte un **numéro de séquence + timestamp GPS** dans le log local *et* dans tout message réseau, ce qui permet de réconcilier et de détecter le moindre trou.

### 2.5 Isolation matérielle (règle transversale, tous les eggs)

```text
[ Module analogique ]      |  traversée   |   [ Numérique ]
 alim linéaire propre      | optocoupleur |    Pi / Pico / FPGA
 Zener/2N3904 → NE5532      |   (LED→φ)    |    (bruyant, à l'écart)
 → LM393 = BIT décidé  ────┼──────────────┼──► GPIO / latch
                           |              |
 masse analogique          |  ISOLATION   |   masse numérique
```

- Le calculateur, aussi bruyant soit-il, **ne voit jamais le bruit brut ni la masse analogique**.
- Ce qui traverse est **un bit déjà décidé** en sortie du LM393, via **optocoupleur**.
- Alimentation **linéaire propre et séparée** pour l'analogique (jamais l'alim à découpage du SoC).

### 2.6 Rôle de chaque plateforme

| Plateforme | Rôle | Quand |
|---|---|---|
| **Pi 3B ×2** | Premiers eggs de validation (chaîne + pipeline de collecte). **Couper WiFi et Bluetooth** (`dtoverlay=disable-wifi`, `disable-bt`). Pas de RTC → **GPS-PPS + chrony** = stratum-1. SoC bruyant → isolation stricte. | RNG-01/02 |
| **RP2040/RP2350 (Pico)** + W5500 + SD + GPS-PPS | Eggs de **densification** : moins bruyants qu'un Pi, et les **PIO** donnent un échantillonnage du bit **rigoureusement déterministe**. | RNG-07 |
| **FPGA / SoC (type Zynq)** | Egg **instrument-grade** : capture déterministe + horodatage matériel verrouillé sur PPS, plusieurs régimes d'échantillonnage en parallèle. **Sur-dimensionné pour RNG-01.** Payant quand la rigueur temporelle devient le facteur limitant. | RNG-07+ |

**Deux mises en garde sur le FPGA :**

1. Il est **pire** qu'un Pico côté CEM (découpage, horloges rapides, DDR, PHY). L'isolation stricte compte donc *encore plus*.
2. Résister à la tentation de générer l'entropie **dans le fabric** (oscillateurs en anneau, métastabilité) : ce serait un autre projet et cela **détruirait la couche 1**. Le FPGA reste un **échantillonneur**, jamais la source du hasard.

---

## 3. Conception détaillée du RNG-01

### 3.1 Décision de source : jonction B-E du 2N3904 (primaire) vs Zener 6,8 V (comparaison)

**Retenu pour le RNG-01 : la jonction base-émetteur du 2N3904 en claquage inverse (avalanche).**

Raisonnement :

- La **Zener 6,8 V** est pile dans la zone de transition Zener/avalanche (effet tunnel < 5 V, avalanche > 6 V). Bruit présent mais modeste, moins large bande.
- La **jonction B-E du 2N3904** avalanche vers **7–9 V** (V_EBO ≥ 6 V au datasheet) et donne un bruit d'avalanche **plus fort et plus large bande**, bien caractérisé, classique des TRNG.
- Contrepartie : elle exige une alimentation **au-dessus** de la tension de claquage → on prévoit un rail plus haut (**+15 V**) pour du courant stable avec marge.

> La Zener 6,8 V est **conservée comme alternative à caractériser** sur banc au RNG-03, pour trancher définitivement par la mesure (RMS, spectre, stationnarité). Le circuit est conçu pour accueillir l'une ou l'autre source.

### 3.2 Schéma de principe (une chaîne)

```text
+15V ─[R_bias]─┬─ nœud bruit ──┤(C_c)├── étage 1 ── étage 2 ── (C)── LM393 ── BIT ── opto ──►
               │                 NE5532/2   NE5532/2         slicer
             2N3904 B-E
             (avalanche)
               │
              GND_A
                         référence LM393 = mi-rail (6V) partagé avec les étages
```

### 3.3 Étage source (avalanche) et courant

Montage : **base + collecteur à la masse**, **émetteur tiré vers +15 V** par `R_bias`. La jonction B-E est ainsi **inversement polarisée** ; quand V_EB dépasse le claquage, elle avalanche. Le bruit est prélevé au nœud émetteur.

Courant approximatif dans la jonction (avec V_EB ≈ 8 V) :

\[
I \approx \frac{V_{CC} - V_{EB}}{R_{bias}} = \frac{15 - 8}{R_{bias}}
\]

Point de départ **R_bias = 100 kΩ** → I ≈ 7 V / 100 kΩ ≈ **70 µA**.

> **À balayer expérimentalement** (RNG-03) : R_bias de **47 k à 470 kΩ** (soit ≈ 15 µA à 150 µA). Le bruit lui-même est le signal ; on cherche le point qui maximise le RMS avec un spectre bien blanc et une bonne stationnarité.

### 3.4 Couplage AC et définition de bande (1 kHz – 30 kHz)

Toute la chaîne est **couplée AC** — c'est essentiel : cela bloque toute dérive DC de la source et des offsets d'ampli, garantissant un signal **de moyenne nulle** présenté au comparateur (condition d'un biais P(1) ≈ 0,5).

Bande cible **1 kHz < f < 30 kHz** pour rester à l'écart du 60 Hz et de ses harmoniques basses, sous la RF, et au-dessus des perturbations lentes.

### 3.5 Amplification NE5532 étagée (passe-bande + gain)

Deux étages **inverseurs** (le NE5532 est double → un boîtier = deux étages), chacun formant un **passe-bande actif** :

**Étage 1 :**
- Gain : G₁ = −R2/R1, avec **R1 = 2,2 kΩ**, **R2 = 100 kΩ** → **G₁ ≈ −45**
- Passe-haut d'entrée : C_in avec R1 → f_HP = 1/(2π·R1·C_in). Avec **C_in = 68 nF** → **f_HP ≈ 1,06 kHz**
- Passe-bas de contre-réaction : C_f sur R2 → f_LP = 1/(2π·R2·C_f). Avec **C_f = 47 pF** → **f_LP ≈ 34 kHz**

**Étage 2 :** identique (R3 = 2,2 kΩ, R4 = 100 kΩ, C = 68 nF, C_f = 47 pF), **couplé AC** à l'étage 1.

Résultat : passe-bande **2 pôles ≈ 1–34 kHz**, gain total :

\[
G_{tot} = G_1 \cdot G_2 \approx 45 \times 45 \approx \mathbf{2000}
\]

> **Trim du gain selon la mesure :** l'avalanche donne souvent plus de bruit que prévu. Si l'amplitude sature, passer R2/R4 à **47 kΩ** → G ≈ 21/étage → **G_tot ≈ 460**. Plage utile visée : **≈ 460 à 2000**. Objectif final : quelques volts crête-à-crête autour du mi-rail avant le comparateur.

### 3.6 Masse virtuelle mi-rail (6 V)

Ampli sur **+12 V** avec référence à **V_CC/2 = 6 V** :

- Diviseur **10 kΩ / 10 kΩ** depuis +12 V, découplé par **100 µF ∥ 100 nF**.
- Les étages inverseurs référencent leur entrée + à ce 6 V.
- **Upgrade propre :** buffer le mi-rail avec un ampli dédié (moins de bruit injecté). Pour un premier proto, le diviseur bien découplé suffit.

### 3.7 Comparateur LM393 (le point délicat)

Le biais du bit dépend de la fraction du temps où le bruit est au-dessus du seuil. **Toute la difficulté pratique est la stabilité du seuil relatif au centre du bruit.**

Règles de conception :

- **Référence liée au mi-rail partagé.** Le seuil du LM393 est pris sur le **même nœud 6 V** que le centrage des étages : toute dérive devient **commune** et s'annule → la décision reste équilibrée. (Astuce centrale.)
- **Entrée bruit couplée AC** au comparateur, polarisée sur la référence par une résistance → signal **strictement de moyenne nulle** au slicer.
- **Pas d'hystérésis.** On ne veut pas biaiser les statistiques. Le « chatter » entre deux instants d'échantillonnage n'a aucune importance : on ne **latche** la sortie qu'au coup d'horloge de 200 Hz. Le LM393 fonctionne en **slicer rapide** ouvert.
- Sortie **collecteur ouvert** → pull-up → attaque la **LED de l'optocoupleur**.

### 3.8 Traversée d'isolation

La sortie LM393 pilote la **LED de l'optocoupleur**. Côté numérique, le phototransistor tire une ligne logique propre référencée à la **masse numérique isolée** et au rail du calculateur (p. ex. 3,3 V). Les deux domaines n'ont **pas besoin de partager un niveau logique** : l'opto est le point de passage, ce qui casse aussi les **boucles de masse** entre eggs.

### 3.9 Échantillonnage (200 tirages/s)

- Latch de la sortie comparateur à **200 Hz** (rythme des eggs GCP historiques → comparabilité).
- Indépendance : intervalle **5 ms** ≫ temps de corrélation du bruit ≈ 1/34 kHz ≈ **29 µs** → échantillons décorrélés d'un facteur ~170 → **indépendants**. **À vérifier** explicitement (autocorrélation ≈ 0 au lag de 5 ms) au RNG-04.
- RNG-01 : le Pi lit le GPIO sur un timer 200 Hz. Plus tard : latch matériel déterministe (Pico PIO / FPGA).

### 3.10 Débiaisage : AUCUN au RNG-01

Le RNG-01 **garde tout brut** — on caractérise d'abord le biais réel de la source. Le débiaisage vient au RNG-02, et deux philosophies distinctes seront comparées :

- **Masque XOR alternant (style PEAR)** : XOR du bit brut avec une séquence déterministe `1010…`. Annule le biais DC du 1ᵉ ordre **sans** détruire les fluctuations → **préféré** pour ce projet.
- **XOR de deux sources** indépendantes : bon pour un TRNG crypto, mais **efface la structure** qu'on cherche à détecter. À n'utiliser qu'en gardant `RAW_A`, `RAW_B` et `XOR` **séparément**.

### 3.11 Architecture d'alimentation

| Rail | Usage | Nature |
|---|---|---|
| **+15 V** | Polarisation avalanche (R_bias) | Linéaire propre |
| **+12 V** | NE5532 + LM393, mi-rail 6 V | Linéaire propre |
| **+3,3 V** (côté numérique) | Phototransistor opto, GPIO | Rail du calculateur, **isolé** |

> Jamais d'alim à découpage côté analogique. Séparation des masses A/N imposée par l'optocoupleur.

### 3.12 Nomenclature (BOM) RNG-01

- 1 × **2N3904** (source avalanche) — *+ 1 × Zener 6,8 V pour comparaison RNG-03*
- 1 × **NE5532** (double ampli faible bruit)
- 1 × **LM393** (comparateur)
- Résistances : R_bias 100 kΩ (à balayer 47 k–470 k) ; R1/R3 2,2 kΩ ; R2/R4 100 kΩ (option 47 kΩ) ; diviseur mi-rail 2 × 10 kΩ ; pull-up LM393 ; R série LED opto
- Condensateurs : C_in ×2 **68 nF** ; C_f ×2 **47 pF** ; couplages inter-étages ; découplage mi-rail **100 µF + 100 nF** ; découplages d'alim
- 1 × **optocoupleur** (p. ex. 4N35 / PC817)
- Alim linéaire +15 V et +12 V propres
- **NI USB-6210** pour la caractérisation initiale

---

## 4. Plan de caractérisation au NI USB-6210

Le 6210 (**250 kS/s, 16 bits**, Nyquist 125 kHz) couvre largement la bande 1–30 kHz. Caractériser **avant** de figer quoi que ce soit.

### 4.1 Points de mesure dans la chaîne

1. **Bruit brut** au nœud émetteur — via **buffer** (la source est haute impédance, ne pas la charger).
2. **Après étage 1.**
3. **Après étage 2** (signal final avant comparateur).

### 4.2 Mesures à réaliser

- **Amplitude RMS** du bruit.
- **Histogramme des amplitudes** → attendu ≈ **gaussien** (bruit d'avalanche/thermique).
- **DSP / FFT** → attendu **large bande / plat** sur 1–30 kHz. Surveiller : **60 Hz + harmoniques**, spurs d'alim à découpage, pickup RF, horloges de MCU voisins.
- **Autocorrélation** du signal analogique.
- **Balayages paramétriques** : courant (via R_bias), **température**, tension d'alimentation.
- **Comparaison 2N3904 vs Zener 6,8 V** (même banc, mêmes réglages).

### 4.3 Réglages d'acquisition

- Échantillonner à **~200 kS/s** pour une bonne résolution spectrale au-delà de 30 kHz.
- **Enregistrements longs** pour des statistiques stables.
- **Deux voies simultanées** possibles → utile au RNG-02 pour vérifier directement la corrélation croisée des deux sources analogiques.

### 4.4 Critères de validation de la source

- **Stationnarité** : RMS stable dans le temps.
- **Gaussianité** : histogramme cohérent.
- **Blancheur dans la bande** : DSP plate, pas de raies parasites dominantes.

---

## 5. Feuille de route (rappel)

| Étape | Contenu |
|---|---|
| **RNG-01** | Source unique → ampli → LM393 → MCU. Premier flux, mesure du biais **brut**. *(objet de ce document)* |
| **RNG-02** | Deux chaînes indépendantes ; enregistrer `RAW_A`, `RAW_B`, `XOR` (masque alternant PEAR). |
| **RNG-03** | Caractérisation analogique au 6210 ; **trancher 2N3904 vs Zener**. |
| **RNG-04** | Caractérisation numérique (proportion, autocorrélation au lag 5 ms, runs, binomiale, NIST/Dieharder/PractRand). |
| **RNG-05** | Enregistreur continu : `timestamp_GPS, seq, RNG_A, RNG_B, XOR, temp, supply, pps_valid`. |
| **RNG-06** | Expériences **pré-enregistrées** + fenêtres témoins. |
| **RNG-07** | Mini-réseau : plusieurs eggs séparés (Pico/FPGA), collecte par pull. |

---

## 6. Prochaine étape concrète

1. **Monter le RNG-01** sur breadboard/proto avec les valeurs ci-dessus (source 2N3904, R_bias 100 kΩ, NE5532 ×2 en passe-bande, LM393 slicer, opto).
2. **Caractériser au 6210** aux trois points de mesure (§4) et **balayer R_bias**.
3. **Trancher la source** (2N3904 vs Zener) sur données.
4. **Vérifier** l'autocorrélation au lag de 5 ms avant de valider le rythme de 200 Hz.

*Décisions ouvertes à confirmer par la mesure : valeur finale de R_bias, gain total (460 vs 2000), coupures exactes de bande, choix définitif de la source.*
