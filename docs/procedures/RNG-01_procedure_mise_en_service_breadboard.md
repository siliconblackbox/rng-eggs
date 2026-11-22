# RNG-01 — Procédure de mise en service et de test (breadboard)

Nov 19, 2026 · @Steve Beaulieu

Référence : schéma *RNG-01\_breadboard\_schema.pdf* (2 pages). Principe : on monte et on valide un bloc à la fois, du continu vers le bruit, puis du bruit vers les bits. On ne passe pas à l'étape suivante tant que la précédente n'est pas conforme.

## Banc et conventions

| Appareil | Rôle |
| --- | --- |
| SPD3303X-E | CH1 = +12 V analogique (limite 50 mA), CH3 = +3,3 V numérique |
| SDM3045X | Tensions continues (rails, VREF, tension de claquage de la jonction) |
| SDS1104X-E | Signaux en direct, mesures Stdev, Rise/Fall, Duty |
| Analog Discovery 2 | Bode, spectre 14 bits, histogramme, flux de bits (analyseur logique) |
| NI USB-6210 | Acquisitions longues de caractérisation (étape 8) |

- Sonde de l'oscilloscope en x10, couplage AC pour le bruit, mode d'acquisition **Normal** (jamais Average sur du bruit).
- La masse de la sonde et celle du AD2 vont sur **GND** (analogique) ou sur **GND\_D** (numérique), jamais les deux en même temps.
- **Journal de banc** pour chaque mesure : date et heure, température ambiante, tension CH1, R\_bias, position de RV1, source choisie, nom du fichier de capture.
- **Témoin à chaque session** : une capture avec l'entrée à la masse (cavalier B = 0) avant toute mesure sur la source.

## Étape 0 — Préparation

1. Vérifier les brochages : 2N3904 (TO-92, souvent E-B-C), NE5532 et LM393 (8 = V+, 4 = GND), 4N25 (1 A, 2 K, 4 E, 5 C, 6 B), CD4053 (16 VDD, 7 VEE, 8 VSS), 74HC14 (14 VCC, 7 GND).
2. Régler l'alimentation **sans charge** : CH1 = 12,00 V, limite 50 mA ; CH3 = 3,3 V.
3. Vérifier que GND et GND\_D ne sont pas reliés : au SDM3045X, résistance entre les deux = circuit ouvert.

## Étape 1 — Rails et VREF (aucun CI en place)

**Monter :** découplage d'entrée (C10, C11), pont VREF (R20, R21, C20, C21).

| Mesure | Attendu |
| --- | --- |
| +12 V sur les rails | 12,00 V |
| VREF (SDM) | 6,00 V ± 0,1 V |
| Ondulation sur VREF (oscillo, AC) | < 1 mV crête, pas de 60 Hz visible |
| Courant total | ≈ 0,6 mA |

## Étape 2 — Source seule

**Monter :** R\_bias A (100 kΩ) et Q1 (2N3904, jonction B-E en inverse, collecteur en l'air).

1. **SDM sur SRC\_A** : noter la tension de claquage V\_BR. Attendu : 7 à 9 V. Courant de jonction = (12 − V\_BR) / 100 kΩ ≈ 30 à 50 µA.
2. **Oscillo sur SRC\_A** (AC, x10) : bruit aléatoire de quelques mV, sans motif répétitif. La sonde charge un peu ce nœud à haute impédance au-dessus de quelques dizaines de kHz ; c'est une vérification qualitative seulement.
3. Si la tension égale presque 12 V et qu'il n'y a pas de bruit : la jonction ne claque pas (mauvais brochage ou tension trop basse).
4. Refaire 1 et 2 avec **R\_bias B et DZ1** (Zener 6,8 V).

## Étape 3 — Étage 1, entrée à la masse

**Monter :** C1, R1, R2, C2, U1 (NE5532) avec son découplage. Entrée de C1 reliée à GND (cavalier B = 0, ou fil).

| Mesure | Attendu |
| --- | --- |
| Courant total | ≈ 8 à 10 mA |
| DC à TP1 (SDM) | VREF ± 50 mV |
| TP1 à l'oscillo, balayage rapide (limite 20 MHz désactivée) | Aucune oscillation |
| Bruit propre à TP1 (Stdev) | ≈ 0,1 mV rms ou moins |

**Bode (AD2, analyseur de réseau)** : débrancher l'entrée de la masse, injecter 10 mV crête sur l'entrée de C1, mesurer TP1. Attendu : gain ≈ 47 (33 dB) plat, −3 dB vers 1 kHz et vers 33 kHz.

## Étape 4 — Étage 2, entrée à la masse

**Monter :** C3, R3, R4, RV1, C4. RV1 au minimum.

1. **DC à TP2** : VREF ± 50 mV.
2. **Bode de la chaîne complète** : injecter environ 1 mV (AD2 avec un diviseur 100:1). Attendu : environ 40 dB avec RV1 au minimum, environ 67 dB au maximum, même bande de 1 à 33 kHz.
3. **Plancher de bruit** (entrée à la masse, RV1 à la position de travail visée) : noter Stdev à TP2 et capturer le spectre. Repérer toute raie (60 Hz et harmoniques, découpage, horloges). C'est la référence « témoin » de la chaîne.

## Étape 5 — Source branchée, réglage du gain

**Choisir :** B = 1, A = 0 (SRC\_A, 2N3904).

1. Monter RV1 jusqu'à **≈ 1 V rms à TP2** (mesure Stdev), crêtes à l'intérieur de 1,5 à 10,5 V, sans écrêtage. Noter la position de RV1 et le gain.
2. **Rapport source / plancher** : Stdev(source) / Stdev(entrée à la masse) ≥ 10 (20 dB). Sinon, le bruit de la chaîne ou une interférence domine.
3. **Spectre (AD2)** : plateau à peu près plat de 1 à 33 kHz. Toute raie qui dépasse nettement le plateau est une interférence à éliminer avant d'aller plus loin.
4. **Histogramme (AD2)** : gaussien, symétrique, sans troncature aux extrémités.
5. Refaire 1 à 4 avec **SRC\_B** (Zener), même gain, pour la comparaison.

## Étape 6 — Comparateur et isolation

**Monter :** R5, U2 (LM393), R7, U3 (4N25), R8, R9 ; CH3 = 3,3 V sur le côté numérique ; U5 (74HC14).

1. **Avant la mise sous tension** : refaire le test GND / GND\_D = circuit ouvert.
2. **Sortie LM393** (pin 1, masse GND) : bascules franches entre environ 0 et 12 V, sans rafales d'oscillation sur les transitions.
3. **Collecteur du 4N25** (masse de sonde sur GND\_D) : mesurer Rise et Fall. Attendu quelques µs. Ajuster R8 (1 à 3,3 kΩ) et R9 (100 kΩ à 1 MΩ) pour des fronts nets.
4. **BIT** (sortie du 74HC14) : niveaux 0 / 3,3 V propres, rapport cyclique (Duty) proche de 50 %. Un écart de quelques % est normal à ce stade : c'est le biais brut qu'on caractérise.

## Étape 7 — Premier flux de bits (AD2, analyseur logique)

1. Brancher l'entrée numérique du AD2 sur BIT, masse sur **GND\_D seulement**.
2. **Enregistrement A** : échantillonnage à 200 Hz (un bit toutes les 5 ms, cadence prévue du egg), au moins 10⁶ bits (environ 1 h 25).
3. **Enregistrement B** : échantillonnage rapide (par exemple 100 kHz) sur quelques secondes, pour mesurer la corrélation entre bits proches.
4. **Analyse (Python)** :
   - proportion de 1 et z-score du biais (pour 10⁶ bits, σ = 0,0005) ;
   - autocorrélation aux décalages 1 à 10 ;
   - test des séquences (runs).
5. Attendu : sur A, autocorrélation non significative ; sur B, corrélation visible aux courts décalages, qui fixe la cadence maximale utilisable. Un biais brut de quelques σ est attendu et sera traité au RNG-02 (masque XOR alterné).

## Étape 8 — Caractérisation au USB-6210

Reprend le plan de caractérisation de *RNG\_egg\_architecture\_et\_RNG-01.md* (section 4).

- **Réglages** : environ 200 kS/s, entrée différentielle (AI+ sur le point mesuré, AI− sur VREF), enregistrements longs.
- **Points** : source (par un tampon, pour ne pas la charger), TP1, TP2.
- **Mesures** : RMS, histogramme, densité spectrale, autocorrélation du signal analogique.
- **Balayages** : R\_bias (47 k, 100 k, 220 k, 470 k), tension d'alimentation, température ; 2N3904 contre Zener 6,8 V avec les mêmes réglages.
- **Critères de validation de la source** : stationnarité (RMS stable dans le temps), gaussianité, blancheur dans la bande (aucune raie dominante).

## Écarts avec le document de conception de septembre

La version breadboard garde les mêmes bandes et le même gain total, avec des valeurs adaptées au matériel en main :

| Élément | Document de septembre | Breadboard |
| --- | --- | --- |
| Rail de polarisation | +15 V séparé | +12 V commun |
| R1 / R3 | 2,2 kΩ | 4,7 kΩ |
| R2 / R4 | 100 kΩ | 220 kΩ / 10 kΩ + RV1 220 kΩ |
| Condensateurs d'entrée | 68 nF | 33 nF |
| Condensateurs de rétroaction | 47 pF | 22 pF |
| Choix de la source | à la main | CD4053 (source A, source B ou masse) |

À trancher avant la version soudée : garder le +12 V commun ou revenir à un rail de polarisation séparé.
