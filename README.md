# Conscience globale — Réseau d'œufs RNG physiques

Construction d'un réseau de générateurs physiques de nombres vraiment aléatoires (« œufs »),
inspiré du *Global Consciousness Project* (Roger Nelson), afin de tester l'existence de
corrélations entre des RNG géographiquement distribués.

**Auteur :** Steve Beaulieu, ing.
**Publication :** siliconblackbox.ca (à venir)

## Cadre épistémologique

Séparation stricte des couches d'analyse :

source physique → bruit analogique → conversion en bits → statistiques individuelles
→ corrélations inter-RNG → corrélations avec des événements → interprétation

L'hypothèse « conscience » est la dernière boîte, jamais la première. Les protocoles sont
écrits avant l'examen des données, et des fenêtres témoins (*sham*) servent de contrôles négatifs.

## Méthode de travail

Chaque jalon suit le même cycle : **protocole** (écrit avant) → **montage** → **mesures**
(données brutes immuables + métadonnées) → **analyse** (scripts reproductibles) → **rapport**.

## État d'avancement

| Phase | Description | État |
|---|---|---|
| 0 | Fondations : dépôt, gabarits, chaîne d'acquisition, plancher de bruit | En cours |
| 1 | RNG-01 sur breadboard, un étage à la fois (J1.1 à J1.6) | À venir |
| 2 | Numérisation et horodatage (W5500-EVB-Pico, GPS-PPS) | À venir |
| 3 | RNG-02 et contrôle d'indépendance inter-œufs | À venir |
| 4 | RNG-03 (source Zener) en comparaison de banc | À venir |
| 5 | Facteurs confondants (température, alimentation, RF) | À venir |
| 6 | PCB de l'œuf et boîtier | À venir |
| 7 | Réseau, protocole pré-enregistré, analyse d'événements | À venir |

## Organisation du dépôt

```
docs/          Architecture, décisions (ADR), procédures, références
hardware/      Schémas, nomenclatures, photos par unité
experiments/   Un dossier autoportant par jalon (protocole, données, figures, rapport)
software/      Acquisition, analyse, gabarits
firmware/      Code embarqué (à venir)
journal/       Cahier de laboratoire daté
media/         Photos et vidéos
```

## Licences

| Contenu | Licence |
|---|---|
| Code (`software/`, `firmware/`) | [MIT](LICENSE) |
| Documents, rapports, figures, photos et données | [CC BY 4.0](LICENSE-docs.md) |
| Matériel (schémas, PCB) | CERN-OHL-P v2 (à ajouter avec les premiers fichiers KiCad) |

Les documents de tiers cités dans `docs/references/` (fiches techniques, publications)
demeurent la propriété de leurs auteurs respectifs.
