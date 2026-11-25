# Protocole — P0.1 : Chaîne d'acquisition USB-6210, vérification croisée et plancher de bruit

> **Règle :** ce protocole est rédigé et **gelé par un commit** avant toute mesure.
> Toute modification après le gel est consignée dans la section « Révisions »
> et justifiée dans le rapport (section « Écarts au protocole »).

| Champ | Valeur |
|---|---|
| Identifiant | P0.1 |
| Version | 1.0 |
| Auteur | Steve Beaulieu, ing. |
| Date de rédaction | 2026-11-24 |
| Commit de gel | Commit « P0.1 : gel du protocole v1.0 » (le hash est consigné dans les métadonnées de chaque mesure et dans le rapport) |
| Dossier de l'expérience | `experiments/P0.1_chaine_acquisition/` |
| Prérequis | Poste `daq-win11` opérationnel ; `idn_check.py` OK sur les 4 Siglent ; autotest NI MAX de `Dev1` réussi |

## 1. Objectif

Caractériser la chaîne d'acquisition **NI USB-6210 + poste `daq-win11`** avant tout
montage, afin qu'elle serve de référence (témoin) pour toutes les mesures analogiques
de la phase 1. On établit :

- **A.** le **plancher de bruit** de la carte, entrée en court-circuit, sur les gammes
  ±0,2 V, ±1 V et ±10 V : décalage, bruit efficace, densité spectrale, raies parasites ;
- **B.** la **stabilité** du décalage et du bruit sur 1 h (gamme ±0,2 V) ;
- **C.** la **concordance en continu** entre la 6210 et le multimètre SDM3045X sur
  plusieurs tensions et les trois gammes (vérification croisée, pas un étalonnage).

## 2. Question et hypothèses

- **Question :** la chaîne USB-6210 est-elle assez silencieuse, stable et cohérente pour
  mesurer sans biais notable le bruit propre des étages de RNG-01 (≈ 0,1 mV eff. au
  1ᵉʳ étage) et la source d'avalanche (quelques mV eff.) ?
- **H0 :** le plancher, la stabilité et la concordance respectent les critères de la
  section 3 ; la 6210 n'est le maillon limitant d'aucune mesure prévue.
- **H1 :** au moins un critère n'est pas respecté (bruit excessif, raies, dérive,
  erreur de gain) ; la chaîne doit être corrigée ou ses limites intégrées aux
  incertitudes des mesures suivantes.

## 3. Critères d'acceptation (fixés avant la mesure)

Justification des seuils : le plus petit signal à mesurer en phase 1 est le bruit propre
du 1ᵉʳ étage, ≈ 100 µV eff. Un plancher de 30 µV eff. ajouté en quadrature biaise cette
mesure de +4,4 %, biais corrigible par soustraction quadratique. Les valeurs observées
lors de l'essai préliminaire du 2026-11-24 (voir section 12) ont servi d'ordre de
grandeur ; les seuils incluent une marge.

| # | Grandeur | Gamme | Valeur attendue | Seuil d'acceptation | Méthode de calcul |
|---|---|---|---|---|---|
| C1 | Décalage (moyenne, entrée en court-circuit) | ±0,2 V | ≈ +20 µV | \|moyenne\| ≤ 100 µV | Moyenne des 60 s (partie A) |
| C2 | Bruit efficace dans la bande 1–34 kHz | ±0,2 V | ≈ 10 µV | ≤ 30 µV eff. | Intégrale de la DSP (Welch) entre 1 et 34 kHz, racine carrée |
| C3 | Bruit efficace dans la bande 1–34 kHz | ±1 V | ≈ 1 LSB (30 µV) | ≤ 60 µV eff. | Idem |
| C4 | Raies parasites dans 1–34 kHz | ±0,2 V | Aucune dominante | Puissance totale des raies ≤ 10 % de la puissance de bande | Raie = pic > 20 dB au-dessus de la médiane glissante de la DSP ; somme des puissances des raies / puissance totale 1–34 kHz |
| C5 | Stationnarité du bruit | ±0,2 V | Stable | Coefficient de variation du RMS par blocs de 10 s ≤ 5 % | Partie B, RMS de chaque bloc de 10 s |
| C6 | Dérive du décalage sur 1 h | ±0,2 V | Faible | max − min des moyennes par blocs de 60 s ≤ 20 µV | Partie B |
| C7 | Écart 6210 − SDM3045X | ±0,2 V, ±1 V, ±10 V | ≤ 0,1 % | \|écart\| ≤ 0,2 % de la lecture + 2 LSB de la gamme | Partie C, chaque point |
| C8 | Linéarité de la 6210 relativement au SDM | ±1 V, ±10 V | — | Résidus d'une droite ajustée (6210 en fonction de SDM) ≤ 3 LSB | Partie C, moindres carrés sur les points de la gamme |

La chaîne est **conforme** si C1 à C8 sont respectés. Un critère non respecté n'arrête
pas forcément la phase 1, mais impose une décision consignée dans le rapport
(correction, ou intégration de la limite dans les incertitudes).

LSB par gamme (16 bits) : ±0,2 V → 6,1 µV ; ±1 V → 30,5 µV ; ±10 V → 305 µV.

## 4. Montage

Aucun circuit RNG. Bornier à vis de la USB-6210, voie **ai0 en différentiel** :

| Configuration | Borne 15 (AI 0+) | Borne 16 (AI 8 / AI 0−) | Borne 28 (AI GND) |
|---|---|---|---|
| **CC** — court-circuit (parties A, B, témoins) | fil court vers 16 | fil court vers 15 et 28 | reliée à 16 |
| **SPD** — vérification croisée (partie C) | SPD3303X-E CH1 + ; SDM3045X HI | SPD CH1 − ; SDM LO ; fil vers 28 | reliée à 16 |

- Fils les plus courts possible (< 5 cm pour le court-circuit), torsadés pour la configuration SPD.
- La masse numérique (D GND, bornes 9 et 13) n'est pas utilisée.
- Photo du montage avant chaque configuration : `experiments/P0.1_chaine_acquisition/figures/`.
- Position physique : 6210 sur le banc, branchée au concentrateur USB de `pve-bureau`
  (port `3-9.2`). Aucun autre montage alimenté sur le banc pendant la mesure.

## 5. Instruments et réglages

| Instrument | Rôle | Réglages |
|---|---|---|
| NI USB-6210 (`Dev1`, SN 013271B1) | Mesure | Voie `Dev1/ai0`, différentielle. Parties A et témoins : 100 kS/s, 60 s par gamme (témoins : 10 s). Partie B : 10 kS/s, 3600 s. Partie C : 10 kS/s, 1 s par point |
| SPD3303X-E (192.168.1.53) | Source continue (partie C) | CH1, limite de courant 10 mA ; CH2 et CH3 éteints |
| SDM3045X (192.168.1.51) | Référence de comparaison (partie C) | DCV, gamme fixe adaptée au point, vitesse lente, impédance d'entrée > 10 GΩ si offerte ; 10 lectures par point |
| `daq-win11` (VM 220) | Pilotage et enregistrement | NI-DAQmx 2026 Q4, environnement conda `rng` |

Les identités (`*IDN?`, numéro de série et température interne de la 6210 si
disponible) sont relevées automatiquement dans les métadonnées de chaque fichier.

## 6. Variables

- **Indépendantes :** gamme d'entrée (±0,2 / ±1 / ±10 V) ; tension appliquée (partie C) ; temps (partie B).
- **Dépendantes :** moyenne, RMS, DSP, raies, résidus, écart avec le SDM.
- **Covariables consignées :** température ambiante (manuelle ou BME680), température
  interne de la 6210 si disponible, heure, état des autres équipements du bureau
  (chauffage, éclairage, chargeurs, autres VM actives sur `pve-bureau`).
- **Maintenues constantes :** câblage, port USB, poste d'acquisition, version du logiciel.

## 7. Témoins

- **Témoin de début** et **témoin de fin** : configuration CC, gamme ±0,2 V, 100 kS/s, 10 s.
  Ils encadrent la session et révèlent toute dérive ou perturbation survenue pendant celle-ci.
- La partie A est elle-même le témoin de la chaîne pour toute la phase 1 : elle sera
  **refaite en début de chaque campagne** de mesures (version courte : ±0,2 V, 60 s).

## 8. Procédure

1. Mettre sous tension la 6210 (VM démarrée), le SDM3045X et le SPD3303X-E (sorties OFF).
   **Réchauffement : 30 min.**
2. Si NI MAX le propose : **auto-étalonnage** de `Dev1` après le réchauffement. Consigner
   le résultat et la date dans le journal. Sinon, consigner « non disponible ».
3. Relever la température ambiante.
4. Câbler la configuration **CC**. Photo.
5. **Témoin de début** (10 s, ±0,2 V).
6. **Partie A** : 60 s à 100 kS/s sur ±0,2 V, puis ±1 V, puis ±10 V.
7. **Partie B** : 3600 s à 10 kS/s sur ±0,2 V. Ne pas toucher au banc.
8. Câbler la configuration **SPD**. Photo.
9. **Partie C**, pour chaque gamme, points en ordre **montant puis descendant**
   (pour séparer une dérive d'un effet de la tension) :
   - ±0,2 V : 0,05 → 0,10 → 0,18 → 0,10 → 0,05 V
   - ±1 V : 0,25 → 0,50 → 0,90 → 0,50 → 0,25 V
   - ±10 V : 2,5 → 5,0 → 9,0 → 5,0 → 2,5 V
   Pour chaque point : régler le SPD, attendre 10 s, lire le SDM (10 lectures),
   acquérir 1 s à la 6210, relire le SDM (10 lectures). La valeur SDM retenue est la
   moyenne avant/après ; l'écart avant/après est consigné.
   Après le dernier point : SPD CH1 sur OFF.
10. Recâbler la configuration **CC**. **Témoin de fin** (10 s, ±0,2 V).
11. Relever la température ambiante. Calculer les SHA-256 de tous les fichiers bruts.

Les étapes 5 à 11 sont exécutées par le script `software/acquisition/p01_acquisition.py`,
qui marque une pause et attend une confirmation aux étapes de recâblage.

Convention de nommage : `AAAAMMJJ-HHMMSS_P0.1_<partie>_<gamme>_<essai>.<ext>` et son
fichier `.meta.yaml` (gabarit `software/templates/mesure.meta.yaml`).

Format des données brutes : échantillons **bruts int16** de la 6210 avec les coefficients
de mise à l'échelle fournis par DAQmx (dans les métadonnées), afin que la conversion en
volts soit reproductible. Taille estimée : A ≈ 3 × 12 Mo, B ≈ 72 Mo (à placer sous
Git LFS ou archive externe, voir `.gitignore`), C négligeable.

## 9. Analyse prévue (pré-enregistrée)

Script : `software/analysis/p01_analyse.py` (version = commit au moment de l'analyse).

- Conversion int16 → V avec les coefficients DAQmx enregistrés.
- **Parties A et témoins :** moyenne ; écart-type ; DSP de Welch (fenêtre de Hann,
  segments de 2¹⁶ échantillons, chevauchement 50 %) ; RMS de bande 1–34 kHz par
  intégration de la DSP ; détection des raies selon la définition de C4, avec la liste
  des fréquences, de leurs amplitudes et de l'origine probable (60 Hz et harmoniques,
  découpage, horloges).
- **Partie B :** RMS et moyenne par blocs de 10 s et de 60 s ; C5 et C6 ; tracé
  temporel avec la température si disponible.
- **Partie C :** pour chaque point, moyenne 6210 contre moyenne SDM ; écart absolu et
  relatif (C7) ; droite ajustée par gamme et résidus (C8) ; comparaison montée/descente.
- **Comparaison témoin de début / témoin de fin :** différence des moyennes et des RMS.

**Analyses exploratoires** (rapportées séparément, sans incidence sur le verdict) :
histogrammes et normalité (asymétrie, aplatissement) ; autocorrélation ; DSP aux
fréquences inférieures à 1 kHz ; comparaison de la partie A avec l'essai préliminaire.

## 10. Critères d'arrêt et risques

- **Arrêt :** surintensité ou limitation de courant au SPD, valeur hors gamme à la 6210,
  perte de la 6210 dans la VM (déconnexion USB), redémarrage de Windows.
- **Risques pour la validité :**
  - couplage au 60 Hz et aux alimentations à découpage du bureau (chargeurs, `pve-bureau`
    lui-même) → consigner les appareils présents, comparer les témoins ;
  - transmission USB à travers une VM (latence, pertes) → DAQmx signale les dépassements
    de tampon ; toute erreur invalide le fichier ;
  - le SDM3045X n'est **pas** une référence nettement plus juste que la 6210 : la partie C
    établit une **concordance**, pas une exactitude absolue ;
  - étalonnage externe de la 6210 échu (2008) : les résultats valent pour cet exemplaire,
    à cette date.

## 11. Ce que cette mesure ne permet pas de conclure

- L'exactitude absolue de la 6210 (aucune référence traçable).
- Le comportement de la carte avec une source à haute impédance (le court-circuit est à
  impédance nulle) : il sera vérifié avec le tampon LMC6482 lors de J1.1.

## 12. Observations préliminaires (2026-11-24, NI MAX, avant rédaction — hors analyse)

Mesures manuelles, ai1 en différentiel à 1 kHz, servant uniquement à dimensionner les seuils :
décalage ≈ +20 µV (±1 V) et ≈ +23 µV (±0,2 V) ; bruit ≈ 1 LSB à ±1 V et ≈ 8–10 µV eff. à
±0,2 V (bande 0–500 Hz) ; écart 6210 − SDM de +0,9 mV à 1 V (gamme ±1 V) et ≈ +4,3 mV à
10 V (gamme ±10 V). Ces valeurs ne font pas partie des résultats de P0.1.

## 13. Révisions

| Version | Date | Modification | Justification |
|---|---|---|---|
| 1.0 | 2026-11-25 | Version initiale, relue et approuvée par S. Beaulieu | — |
