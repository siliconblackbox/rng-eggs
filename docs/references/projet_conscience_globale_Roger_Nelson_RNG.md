# Projet « Conscience globale » — Roger Nelson et générateurs de nombres aléatoires

## 1. Introduction

Le **Global Consciousness Project (GCP)**, associé notamment aux travaux de **Roger Nelson** et au laboratoire **PEAR (Princeton Engineering Anomalies Research)**, cherche à déterminer si des événements mobilisant simultanément un très grand nombre de personnes pourraient être associés à de très faibles anomalies statistiques dans des réseaux de générateurs physiques de nombres aléatoires.

Ce sujet est particulièrement intéressant à explorer si on le traite comme une **expérience instrumentale à faible effet**, en séparant rigoureusement :

1. ce que mesure réellement l'électronique ;
2. ce que montrent les statistiques ;
3. l'interprétation éventuelle en termes de conscience.

Il ne faut donc pas partir de l'hypothèse que la conscience influence nécessairement les générateurs. L'objectif est plutôt de construire un système suffisamment bien caractérisé pour pouvoir rechercher objectivement un éventuel effet.

---

# 2. Que cherche réellement à mesurer le Global Consciousness Project ?

Le Global Consciousness Project a installé à travers le monde des générateurs physiques de nombres aléatoires, historiquement appelés des **« eggs »**.

Chaque appareil génère des bits à partir d'un phénomène électronique considéré comme fondamentalement aléatoire, plutôt qu'à partir d'un algorithme pseudo-aléatoire.

Les données sont :

- générées continuellement ;
- horodatées ;
- transmises vers un serveur central ;
- comparées entre plusieurs générateurs géographiquement séparés.

L'idée n'est pas simplement :

> « Une personne pense à 1 et le générateur produit davantage de 1. »

L'hypothèse étudiée est beaucoup plus subtile.

Lors d'un événement impliquant simultanément beaucoup de personnes, les générateurs indépendants pourraient éventuellement présenter une **corrélation extrêmement faible mais statistiquement détectable**.

C'est donc principalement la **corrélation entre plusieurs RNG indépendants** qui est intéressante.

---

# 3. Prudence scientifique

Le GCP a accumulé plusieurs centaines d'événements définis à l'avance.

Les auteurs du projet ont rapporté une déviation cumulative importante par rapport au modèle aléatoire attendu.

Cependant, l'interprétation de cette anomalie comme une manifestation d'une **conscience globale** demeure controversée.

Il faut donc distinguer :

- **anomalies statistiques rapportées : oui ;**
- **preuve établie que la conscience agit physiquement sur les RNG : non.**

Plusieurs explications alternatives doivent toujours être envisagées :

- biais expérimental ;
- choix des événements ;
- méthode statistique ;
- dérive des générateurs ;
- influences environnementales ;
- erreurs de synchronisation ;
- corrélations électriques ou électromagnétiques ;
- sélection involontaire des données.

C'est précisément cette incertitude qui rend le sujet expérimentalement intéressant.

---

# 4. Global Consciousness Project 2.0

Le projet moderne utilise une nouvelle génération de générateurs physiques de nombres aléatoires.

Un point particulièrement intéressant pour un projet électronique est l'utilisation de **diodes Zener en régime d'avalanche comme sources de bruit**.

Le principe est donc accessible avec des composants discrets.

Sources utiles :

- https://rng.observer/
- https://noosphere.princeton.edu/
- https://noosphere.princeton.edu/science2.html
- https://noosphere.princeton.edu/rdnelson/reg.html
- https://noosphere.princeton.edu/recipe.html

---

# 5. Principe général d'un générateur physique de nombres aléatoires

Le principe peut être représenté comme ceci :

```text
          phénomène physique aléatoire
                     │
                     ▼
             diode Zener en avalanche
                     │
              bruit analogique
                     │
             amplification / filtrage
                     │
                     ▼
             décision logique 0 / 1
             comparateur / bascule
                     │
               flux de bits
```

On peut améliorer le système en utilisant deux sources indépendantes :

```text
        Zener A                     Zener B
           │                           │
        ampli A                     ampli B
           │                           │
      comparateur A              comparateur B
           │                           │
           └──────────── XOR ──────────┘
                          │
                     flux de bits
```

Le XOR permet de réduire certains biais systématiques si les deux sources sont réellement indépendantes.

---

# 6. Pourquoi utiliser une diode Zener ?

Lorsqu'une diode Zener est polarisée en inverse dans sa région d'avalanche, elle génère du bruit électrique.

Ce bruit contient notamment des phénomènes associés :

- au bruit d'avalanche ;
- aux fluctuations microscopiques du courant ;
- aux phénomènes de génération et recombinaison ;
- éventuellement au bruit thermique.

Le bruit généré est faible, mais il peut être amplifié.

Un montage expérimental simple pourrait commencer par :

```text
+12 V
  │
  R
  │
  ├──── sortie bruit
  │
 ZD1
6.8 V
  │
 GND
```

Avec, par exemple :

```text
Vcc = 12 V

ZD1 = Zener 6.8 V

R = 2.2 kΩ à 4.7 kΩ
```

Le courant approximatif dans la Zener est :

\[
I_Z = \frac{V_{CC}-V_Z}{R}
\]

Pour :

\[
V_{CC}=12~V
\]

\[
V_Z=6.8~V
\]

et :

\[
R=2.2~k\Omega
\]

on obtient :

\[
I_Z \approx \frac{12-6.8}{2200}
\]

\[
I_Z \approx 2.36~mA
\]

Il serait cependant préférable de **tester expérimentalement plusieurs courants** plutôt que de choisir définitivement une valeur théorique.

Le bruit lui-même est ici notre signal utile.

---

# 7. Mesurer d'abord le bruit analogique

Avant de transformer le bruit en bits, il serait intéressant de caractériser directement la source analogique.

Ton **NI USB-6210** pourrait être particulièrement utile pour cette étape.

On pourrait mesurer :

- amplitude RMS du bruit ;
- histogramme des amplitudes ;
- densité spectrale ;
- spectre FFT ;
- autocorrélation ;
- influence du courant dans la Zener ;
- influence de la température ;
- influence de la tension d'alimentation ;
- comparaison entre différentes références de Zener.

Cela permettrait de choisir la meilleure diode et le meilleur point de fonctionnement avant de construire la chaîne numérique.

---

# 8. Amplification du bruit

Le bruit brut provenant de la Zener risque de n'être que de quelques µV à quelques mV.

Une amplification importante sera donc nécessaire.

On pourrait utiliser par exemple un **NE5532**, préférable à un LM358 pour du faible bruit analogique.

Une chaîne pourrait être :

```text
Zener
  │
  ▼
couplage AC
  │
  ▼
filtre passe-haut
  │
  ▼
amplificateur ×20 à ×50
  │
  ▼
deuxième amplificateur ×20 à ×50
  │
  ▼
filtre passe-bas
```

Le gain total pourrait être de l'ordre de :

\[
G \approx 500 \text{ à } 2000
\]

La valeur exacte sera déterminée expérimentalement.

---

# 9. Bande passante

Une bande passante contrôlée est importante afin d'éviter que le système soit principalement sensible :

- au 60 Hz ;
- aux alimentations à découpage ;
- aux émissions RF ;
- aux microcontrôleurs proches ;
- aux perturbations électromagnétiques.

Une plage initiale intéressante serait par exemple :

\[
1~kHz < f < 30~kHz
\]

Les anciens générateurs PEAR utilisaient également une bande de bruit comparable.

La chaîne complète pourrait donc être :

```text
Zener
  ↓
filtre passe-haut
  ↓
ampli ×30
  ↓
ampli ×30
  ↓
filtre passe-bas
  ↓
comparateur
  ↓
0 / 1
```

---

# 10. Utilisation du LM393

Le **LM393** est très approprié pour transformer le bruit analogique amplifié en signal logique.

Une référence placée autour du point milieu permettra de décider :

```text
bruit > seuil  → 1

bruit < seuil  → 0
```

Cependant, le seuil devra être très stable.

Une solution possible consiste à créer une référence autour de :

\[
V_{REF} = \frac{V_{CC}}{2}
\]

et à centrer le bruit amplifié autour de cette tension.

Par exemple avec une alimentation analogique 5 V :

\[
V_{REF} = 2.5~V
\]

Le signal pourrait donc osciller autour de 2,5 V.

---

# 11. Deux RNG indépendants

Une deuxième version du projet devrait comporter **deux chaînes complètement indépendantes** :

```text
Zener A → ampli A → comparateur A → A ─┐
                                       XOR → bit final
Zener B → ampli B → comparateur B → B ─┘
```

Le XOR pourrait être réalisé avec un :

- 74HC86 ;
- 74HCT86 ;
- ou directement dans le microcontrôleur.

Il serait cependant très intéressant de conserver simultanément :

```text
RAW_A

RAW_B

A_XOR_B
```

On disposerait ainsi des données brutes pour les analyses ultérieures.

Il ne faudrait surtout pas conserver uniquement les bits « nettoyés ».

---

# 12. Acquisition par microcontrôleur

Un **ATmega32U4** serait parfaitement adapté pour l'acquisition.

Son rôle serait limité principalement à :

- lire les bits ;
- compter les 1 ;
- regrouper les mesures ;
- horodater ou recevoir un horodatage du PC ;
- transmettre les données USB.

Le microcontrôleur ne devrait idéalement pas être utilisé comme source de hasard.

Le caractère aléatoire doit provenir du phénomène analogique.

---

# 13. Exemple : 200 bits par seconde

Supposons que l'on décide de prélever exactement :

\[
N=200
\]

bits chaque seconde.

On obtient par exemple :

```text
011010010101001010...
```

Puis on compte le nombre de bits à 1.

Supposons :

```text
103 bits = 1

97 bits = 0
```

Pour une source équilibrée :

\[
X \sim B(200,0.5)
\]

La moyenne théorique est :

\[
\mu = np
\]

donc :

\[
\mu = 200 \times 0.5
\]

\[
\boxed{\mu = 100}
\]

La variance est :

\[
\sigma^2=np(1-p)
\]

donc :

\[
\sigma^2=200\times0.5\times0.5
\]

\[
\sigma^2=50
\]

et :

\[
\sigma=\sqrt{50}
\]

\[
\boxed{\sigma\approx7.071}
\]

---

# 14. Calcul du score z

Chaque seconde peut alors produire un score :

\[
z=\frac{X-\mu}{\sigma}
\]

Donc :

\[
z=\frac{X-100}{7.071}
\]

Si on obtient :

\[
X=113
\]

alors :

\[
z=\frac{113-100}{7.071}
\]

\[
\boxed{z\approx1.84}
\]

Une valeur de 1,84 pour une seule seconde n'a rien d'extraordinaire.

Des fluctuations de ce type apparaissent naturellement dans une séquence aléatoire.

---

# 15. Réseau de plusieurs générateurs

Supposons maintenant que nous ayons :

\[
N=20
\]

générateurs indépendants.

Chaque générateur produit son propre score :

\[
z_1,z_2,z_3,\dots,z_{20}
\]

On peut calculer une mesure collective :

\[
Z_{réseau}
=
\frac{\sum_{i=1}^{N}z_i}{\sqrt{N}}
\]

Puis :

\[
NetVar = Z_{réseau}^{2}
\]

Ce type de statistique permet de rechercher une variation collective du réseau.

L'idée importante est que l'on ne recherche pas nécessairement :

> davantage de 1 que de 0.

On cherche plutôt si plusieurs générateurs supposément indépendants présentent **simultanément des écarts inhabituels**.

---

# 16. Corrélation entre générateurs

C'est probablement l'aspect le plus intéressant du projet.

Avec plusieurs RNG :

```text
RNG1 ──────────┐
RNG2 ──────────┤
RNG3 ──────────┤
RNG4 ──────────┤
               ▼
       analyse statistique
               │
               ▼
      corrélation temporelle
```

Normalement :

\[
corr(RNG_i,RNG_j)\approx0
\]

pour :

\[
i\neq j
\]

Une corrélation persistante ou événementielle pourrait donc être recherchée.

Mais avant d'envisager une interprétation inhabituelle, il faudrait éliminer les causes ordinaires.

---

# 17. Sources possibles de fausses corrélations

Une corrélation entre plusieurs appareils peut être provoquée par :

- variation du réseau électrique ;
- 60 Hz commun ;
- perturbation électromagnétique ;
- température ;
- Wi-Fi ;
- téléphones cellulaires ;
- horloge commune ;
- logiciel commun ;
- erreur de synchronisation ;
- alimentation commune ;
- transmission USB ;
- dérive des comparateurs ;
- changement climatique ou atmosphérique ;
- proximité physique des appareils.

Il serait donc idéal de placer les appareils :

- sur des alimentations séparées ;
- dans des endroits différents ;
- avec des horloges indépendantes ;
- avec synchronisation temporelle uniquement au niveau des données.

---

# 18. Capteurs environnementaux

Chaque appareil pourrait également mesurer :

- température ;
- tension d'alimentation ;
- humidité ;
- éventuellement champ magnétique ;
- niveau RF ;
- pression atmosphérique.

Par exemple :

```text
RNG
 │
 ├── bits aléatoires
 ├── température
 ├── tension alimentation
 ├── humidité
 └── timestamp
```

On pourrait ensuite vérifier si une anomalie observée dans les bits est corrélée avec un facteur physique.

---

# 19. Tests statistiques du générateur

Avant toute expérience concernant la conscience, le générateur doit être soigneusement caractérisé.

## 19.1 Proportion de bits

Vérifier :

\[
P(1)\approx0.5
\]

et :

\[
P(0)\approx0.5
\]

---

## 19.2 Autocorrélation

On veut vérifier que :

\[
corr(x_t,x_{t+k})\approx0
\]

pour différents décalages \(k\).

---

## 19.3 Test des runs

On étudie les suites telles que :

```text
1111

000

11

0
```

pour vérifier qu'elles suivent les probabilités attendues.

---

## 19.4 Histogrammes

On peut regrouper les bits par blocs :

```text
200 bits

1000 bits

10000 bits
```

et observer la distribution du nombre de 1.

Elle devrait suivre approximativement une loi binomiale puis une distribution normale lorsque \(N\) devient grand.

---

## 19.5 FFT

Une FFT du signal analogique peut révéler :

- 60 Hz ;
- harmoniques ;
- alimentations à découpage ;
- interférences périodiques ;
- oscillations parasites.

---

## 19.6 Suites de tests

On pourrait éventuellement utiliser :

- NIST Statistical Test Suite ;
- Dieharder ;
- PractRand.

Cependant :

> réussir des tests statistiques ne prouve jamais qu'une source est véritablement aléatoire.

Cela signifie seulement que certains défauts détectables n'ont pas été observés.

---

# 20. Protocole expérimental

Une règle fondamentale serait de définir les expériences **avant de regarder les données**.

Par exemple :

```text
Événement : éclipse solaire

Début :
18:00:00 UTC

Fin :
18:30:00 UTC

Statistique :
corrélation inter-RNG

Fenêtre :
1 seconde

Méthode :
définie avant l'expérience
```

Il faudrait éviter de modifier ensuite :

- la durée ;
- la fenêtre temporelle ;
- les appareils sélectionnés ;
- la statistique utilisée.

Sinon il devient très facile de trouver involontairement une anomalie dans des données aléatoires.

C'est le problème des comparaisons multiples et du **p-hacking**.

---

# 21. Architecture générale du projet

Une architecture possible serait :

```text
                    ┌───────────────────┐
                    │     Zener A       │
                    └────────┬──────────┘
                             │
                          bruit
                             │
                             ▼
                        ampli + filtre
                             │
                             ▼
                          LM393
                             │
                             ▼
                           BIT A
                             │
                             │
                             ├─────────┐
                             │         │
                             │        XOR
                             │         │
                             │         ▼
                             │      BIT XOR
                             │
                    ┌────────┴──────────┐
                    │     Zener B       │
                    └────────┬──────────┘
                             │
                          bruit
                             │
                             ▼
                        ampli + filtre
                             │
                             ▼
                          LM393
                             │
                             ▼
                           BIT B

                               │
                               ▼
                       ATmega32U4
                               │
                               ▼
                              USB
                               │
                               ▼
                              PC
                               │
                               ▼
                   acquisition continue
                               │
                               ▼
                        fichiers CSV
                               │
                               ▼
                      analyse Python
```

---

# 22. Plan de développement proposé

## RNG-01 — Source simple

Construire :

```text
Zener → amplificateur → LM393 → microcontrôleur
```

Objectif :

- produire un premier flux de bits ;
- observer le bruit ;
- mesurer le biais.

---

## RNG-02 — Deux sources

Construire :

```text
Zener A → chaîne A
Zener B → chaîne B
```

Puis enregistrer :

```text
RAW_A
RAW_B
XOR
```

---

## RNG-03 — Caractérisation analogique

Utiliser notamment le **NI USB-6210** pour mesurer :

- bruit RMS ;
- spectre ;
- histogramme ;
- autocorrélation ;
- influence du courant ;
- influence de la température.

---

## RNG-04 — Caractérisation numérique

Analyser :

- moyenne ;
- variance ;
- proportion 0/1 ;
- autocorrélation ;
- runs ;
- distribution binomiale ;
- tests NIST ;
- Dieharder ;
- PractRand.

---

## RNG-05 — Enregistreur continu

Produire par exemple :

```text
timestamp, RNG_A, RNG_B, XOR, temperature, supply
```

Exemple :

```text
2026-09-02T22:14:31.000Z,103,99,101,23.4,5.001
```

Chaque ligne pourrait représenter une seconde contenant 200 tirages.

---

## RNG-06 — Expériences préenregistrées

Définir à l'avance :

- événement ;
- heure ;
- durée ;
- statistique ;
- appareils ;
- méthode d'analyse.

Puis exécuter l'expérience sans modifier le protocole.

---

## RNG-07 — Mini réseau GCP

Construire plusieurs appareils physiquement séparés.

Par exemple :

```text
EGG-01
EGG-02
EGG-03
EGG-04
```

Chaque appareil :

```text
RNG
+
température
+
tension alimentation
+
timestamp
```

Toutes les données sont ensuite réunies pour l'analyse.

---

# 23. Une approche particulièrement intéressante

Une possibilité serait de construire progressivement notre propre **mini Global Consciousness Project expérimental**.

L'objectif ne serait pas de démontrer immédiatement une influence de la conscience.

L'objectif serait d'abord de disposer d'un réseau de générateurs extrêmement bien caractérisé.

On pourrait alors étudier plusieurs niveaux :

```text
Niveau 1
Physique de la Zener

        ↓

Niveau 2
Bruit analogique

        ↓

Niveau 3
Conversion en bits

        ↓

Niveau 4
Statistiques individuelles

        ↓

Niveau 5
Corrélations entre RNG

        ↓

Niveau 6
Corrélations avec des événements

        ↓

Niveau 7
Interprétation éventuelle
```

Cette progression permet de conserver une séparation nette entre :

- électronique ;
- traitement du signal ;
- statistiques ;
- hypothèses sur la conscience.

---

# 24. Pourquoi ce projet est particulièrement intéressant

Ce projet touche simultanément plusieurs domaines :

- électronique analogique ;
- bruit électronique ;
- physique des semi-conducteurs ;
- acquisition de données ;
- microcontrôleurs ;
- traitement du signal ;
- statistiques ;
- théorie de l'information ;
- méthodologie scientifique ;
- étude de la conscience.

Il permet surtout de transformer une question très spéculative en une **expérience électronique mesurable et reproductible**.

---

# 25. Première réalisation proposée

Le premier prototype pourrait être construit autour de :

- 2 × diodes Zener ;
- NE5532 ;
- LM393 ;
- 74HC86 ;
- ATmega32U4 ;
- alimentation analogique propre ;
- NI USB-6210 pour la caractérisation initiale.

Architecture :

```text
Zener A
   │
   ▼
filtre
   │
   ▼
NE5532
   │
   ▼
LM393
   │
   ├──────────────► RAW_A
   │
   ▼
  XOR ────────────► XOR
   ▲
   │
LM393
   ▲
   │
NE5532
   ▲
   │
filtre
   ▲
   │
Zener B

RAW_A
RAW_B
XOR
  │
  ▼
ATmega32U4
  │
  ▼
USB
  │
  ▼
PC
```

L'étape suivante logique serait de concevoir le **schéma électronique détaillé de ce premier “EGG”**, avec les valeurs des résistances, condensateurs, gains des amplificateurs, fréquence des filtres, seuil du LM393 et méthode d'acquisition.
