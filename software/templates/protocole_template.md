# Protocole — <ID du jalon> : <titre court>

> **Règle :** ce protocole est rédigé et **gelé par un commit** avant toute mesure.
> Toute modification après le gel est consignée dans la section « Révisions »
> et justifiée dans le rapport (section « Écarts au protocole »).

| Champ | Valeur |
|---|---|
| Identifiant | <ex. J1.1> |
| Version | 1.0 |
| Auteur | Steve Beaulieu, ing. |
| Date de rédaction | AAAA-MM-JJ |
| Commit de gel | <hash git, rempli après le commit> |
| Dossier de l'expérience | `experiments/<ID>_<nom>/` |
| Prérequis | <jalons précédents qui doivent être conformes> |

## 1. Objectif

Une ou deux phrases. Ce que la mesure doit établir, et rien de plus.

## 2. Question et hypothèses

- **Question :** <formulée de façon à pouvoir y répondre par les données>
- **H0 (hypothèse nulle) :** <ce qu'on s'attend à observer si rien d'anormal>
- **H1 :** <l'alternative>

## 3. Critères d'acceptation (fixés avant la mesure)

| # | Grandeur mesurée | Instrument | Valeur attendue | Tolérance | Méthode de calcul |
|---|---|---|---|---|---|
| C1 | | | | | |
| C2 | | | | | |

Le jalon est **conforme** si tous les critères sont respectés. Un critère non respecté
arrête la progression vers le jalon suivant.

## 4. Montage

- Schéma de référence : `hardware/<unité>/schematics/<fichier>` (révision : <…>)
- Composants spécifiques (valeurs mesurées si pertinent) : <…>
- Photo du montage à prendre avant la mesure : `media/` ou `experiments/<ID>/`

## 5. Instruments et réglages

| Instrument | Rôle | Réglages (gamme, couplage, bande, fs, durée…) |
|---|---|---|
| | | |

Les identités des instruments (`*IDN?`, firmware) sont relevées automatiquement
dans les métadonnées de chaque mesure.

## 6. Variables

- **Indépendantes (contrôlées) :** <ex. tension d'alimentation, R_bias>
- **Dépendantes (mesurées) :** <ex. écart-type du bruit, V_BR>
- **Covariables consignées :** température ambiante, humidité, heure, état du réseau électrique (à préciser)
- **Maintenues constantes :** <…>

## 7. Témoins (contrôles négatifs)

- Témoin d'entrée à la masse en début **et** en fin de session.
- <autres témoins : source débranchée, instrument seul, fenêtre *sham*…>

## 8. Procédure

1. Préparation et vérifications de sécurité.
2. Témoin de début de session.
3. Mesures (dans l'ordre, avec les noms de fichiers prévus).
4. Témoin de fin de session.
5. Calcul des sommes SHA-256 des fichiers bruts.

Convention de nommage : `AAAAMMJJ-HHMMSS_<ID>_<config>_<essai>.<ext>` + fichier
`.meta.yaml` du même nom (voir `software/templates/mesure.meta.yaml`).

## 9. Analyse prévue (pré-enregistrée)

- Script(s) : `software/analysis/<…>.py` (version = commit)
- Traitements : <filtrage, fenêtrage, statistiques…> — paramètres fixés ici.
- Tests statistiques et seuils : <…>
- Ce qui serait considéré comme une **analyse exploratoire** (rapportée séparément) : <…>

## 10. Critères d'arrêt et risques

- Arrêt immédiat si : <surintensité, oscillation, échauffement…>
- Risques pour la validité de la mesure : <couplage 60 Hz, charge de la sonde, dérive thermique…>

## 11. Révisions

| Version | Date | Modification | Justification |
|---|---|---|---|
| 1.0 | | Version initiale | |
