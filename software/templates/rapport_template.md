# Rapport — <ID du jalon> : <titre court>

| Champ | Valeur |
|---|---|
| Identifiant | <ex. J1.1> |
| Protocole | [`protocole.md`](protocole.md) v<…> — commit de gel `<hash>` |
| Date(s) des mesures | AAAA-MM-JJ |
| Commit des données | `<hash>` |
| Commit des scripts d'analyse | `<hash>` |
| Verdict | **Conforme / Non conforme / Partiellement conforme** |

## 1. Résumé

Trois à cinq phrases : ce qui a été mesuré, le résultat principal, le verdict.

## 2. Écarts au protocole

Tout ce qui a été fait autrement que prévu, avec la raison. « Aucun » si c'est le cas.

| Écart | Raison | Impact estimé sur le résultat |
|---|---|---|
| | | |

## 3. Conditions de la mesure

- Montage réel (photo) : <lien>
- Instruments (extraits des métadonnées) : <modèle, série, firmware>
- Conditions ambiantes : <température, humidité>
- Témoins réalisés : <début / fin de session>

## 4. Données

| Fichier | Description | Taille | SHA-256 |
|---|---|---|---|
| `data/raw/…` | | | |

Les fichiers bruts sont immuables. Les fichiers dérivés sont dans `data/processed/`
et sont régénérables par les scripts.

## 5. Résultats

### 5.1 Analyse pré-enregistrée

Résultats dans l'ordre des critères du protocole.

| # | Critère | Attendu | Mesuré | Incertitude | Respecté ? |
|---|---|---|---|---|---|
| C1 | | | | | |

Figures : `figures/<…>.png` (générées par `software/analysis/<…>.py`).

### 5.2 Analyses exploratoires

Clairement séparées de ce qui précède. Ne servent pas au verdict ; elles peuvent
motiver un protocole futur.

## 6. Discussion

Interprétation à la bonne couche seulement (source physique → bruit analogique →
bits → statistiques…). Explications alternatives envisagées et écartées (ou non).

## 7. Limites

Incertitudes, biais possibles, ce que cette mesure ne permet **pas** de conclure.

## 8. Suite

Jalon suivant autorisé ? Modifications à apporter au montage ou au protocole ?
