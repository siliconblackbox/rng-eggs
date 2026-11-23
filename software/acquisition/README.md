# Acquisition

Scripts de contrôle des instruments et d'acquisition. Ils tournent sous Windows
(Anaconda), sur le poste relié au réseau du labo.

## Installation (une fois)

```bat
conda create -n rng python=3.12
conda activate rng
cd D:\Projets\Conscience_globale\software\acquisition
pip install -r requirements.txt
```

Le pilote **NI-DAQmx** doit être installé séparément pour la USB-6210.

## Fichiers

| Fichier | Rôle |
|---|---|
| `instruments.yaml` | Adresses IP et protocole de chaque instrument |
| `instruments.py` | Fonctions communes : lecture de la config, ouverture des connexions VISA |
| `idn_check.py` | Vérifie que chaque instrument répond à `*IDN?` |

## Vérification des instruments

```bat
python idn_check.py            :: tous
python idn_check.py --sauver   :: + trace dans logs\idn_<date>.yaml
```
