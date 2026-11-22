# Roger Nelson — The Global Consciousness Project : analyse détaillée

**Date de la fiche :** 2026-11-20  
**Source principale :** entretien de Roger D. Nelson par Jeffrey Mishlove, *New Thinking Allowed*, enregistré le 12 décembre 2018, durée ≈ 60 minutes.  
**Vidéo :** https://www.youtube.com/watch?v=xrt1hPwA978  
**Base documentaire :** transcription anglaise horodatée fournie par l'utilisateur (reconnaissance automatique imparfaite).  
**Statut :** synthèse critique de l'entretien, et non vérification indépendante des publications ou des données brutes. Version révisée le 2026-11-20 après relecture complète de la transcription : corrections, ajouts et contexte externe (section 20).

## 1. Résumé exécutif

Roger Nelson retrace près de quatre décennies de recherches sur l'idée qu'une intention individuelle ou une émotion collective pourrait être associée à des écarts statistiques dans les sorties de générateurs physiques de nombres aléatoires (*random event generators*, REG). Son récit suit trois étapes : (1) les expériences individuelles au laboratoire PEAR de Princeton, où un opérateur tente de faire monter ou descendre la moyenne de séquences binaires ; (2) les expériences « Field REG », où un générateur portable enregistre des données pendant des rassemblements émotionnellement cohérents ; (3) le *Global Consciousness Project* (GCP), réseau de générateurs répartis mondialement, enregistrant en continu pour permettre l'étude de fenêtres temporelles liées à des événements collectifs.

Nelson affirme que les analyses cumulées ont donné des résultats statistiquement significatifs et présente la cohérence émotionnelle comme une hypothèse centrale. Il insiste sur la qualité des instruments, les calibrations, les contrôles, la définition préalable des fenêtres d'observation et la répétition des essais. Il reconnaît toutefois des résultats inverses, l'absence de mécanisme physique démontré et la difficulté de distinguer diverses explications.

**Point critique :** un écart statistique, même significatif selon une méthode donnée, ne prouve ni une causalité mentale ni l'existence d'un « champ de conscience ». L'entretien ne fournit pas à lui seul les séries brutes, l'ensemble des critères de sélection, les scripts, les tailles d'effet ni une évaluation indépendante permettant de trancher.

## 2. Contexte historique : de PEAR au GCP [02:00–06:00 ; 20:35–21:40]

Nelson explique être arrivé au laboratoire *Princeton Engineering Anomalies Research* (PEAR) en 1980. Le laboratoire, associé à Robert Jahn, étudiait notamment l'hypothèse d'interactions anormales entre esprit et systèmes techniques. Nelson évoque les travaux antérieurs de Helmut Schmidt sur les générateurs aléatoires et l'intention. La question initiale est concrète : les états mentaux d'un humain peuvent-ils modifier des mesures issues d'un appareil électronique sans intervention physique ordinaire ?

Le GCP débute en 1997 selon Nelson ; son réseau collecte des données à partir d'août 1998. Il dit avoir quitté PEAR en 2002 et avoir clos le protocole expérimental formel du GCP vers la fin de 2015, après avoir visé 500 tests. Il précise que le GCP a démarré environ dix ans avant la fermeture de PEAR, laboratoire qui aura fonctionné 27 ans. Le réseau continue à fonctionner, mais son entretien décrit une diminution du nombre de stations actives en 2018. Ces dates caractérisent **la situation au moment de l'enregistrement**, pas nécessairement l'état actuel du projet.

## 3. Que mesure un REG physique ? [06:00–11:40]

Nelson distingue :

- **PRNG / générateur pseudo-aléatoire :** suite produite par un algorithme déterministe ; une même graine et un même état conduisent à la même suite.
- **TRNG / REG physique :** suite issue d'un processus physique difficile à prédire. Dans la description de Nelson, un circuit à diode produit un très faible signal associé à des phénomènes quantiques, puis une électronique convertit les fluctuations en bits 0 et 1.

Il présente ce dispositif comme une « pièce électronique » donnant approximativement 50 % de 0 et 50 % de 1. Il cite notamment l'effet tunnel dans la diode. **Précision technique :** la description orale ne constitue pas un schéma du circuit ; elle ne permet pas d'établir seule le composant exact, le régime de polarisation, le bruit dominant, le conditionnement analogique ni la méthode de débiaisage. Un générateur physique réel peut être biaisé, corrélé, sensible à la température, aux alimentations et aux perturbations électromagnétiques.

Le fait qu'une source repose sur la physique quantique n'implique **pas** que la conscience interagisse avec elle. Cette proposition demande un test distinct.

**Effet tunnel ou avalanche ?** Dans une jonction en claquage inverse, l'effet tunnel (effet Zener proprement dit) domine sous environ 5 V ; au-dessus d'environ 7 V, c'est le claquage par avalanche. Une jonction B-E de 2N3904 en claquage vers 7–9 V (source primaire de RNG-01) fonctionne donc en régime d'**avalanche**, pas d'effet tunnel ; une Zener de 6,8 V (RNG-03) se situe dans la zone de transition où les deux mécanismes coexistent. Cela ne change rien à l'hypothèse testée, mais le type de bruit est une variable à documenter pour toute comparaison avec les générateurs PEAR/GCP.

## 4. Protocole PEAR : intention haute, basse, témoin [11:40–15:25]

Le protocole « tripolaire » décrit par Nelson comprend trois conditions :

1. **High :** l'opérateur essaie d'obtenir une moyenne plus élevée.
2. **Low :** il essaie d'obtenir une moyenne plus faible.
3. **Baseline :** il laisse le dispositif fonctionner sans chercher à influencer le résultat.

Un essai rassemble **200 bits** ; le nombre de 1 suit idéalement une loi binomiale **X ~ Binomiale(200, 0,5)**, donc **E[X] = 100**, **Var(X) = 50** et **écart-type ≈ 7,071** si les bits sont indépendants et équitables. La moyenne observée peut s'écarter de 100 par simple hasard ; l'enjeu est de déterminer si les écarts répétés, orientés et prévus sont compatibles avec l'hypothèse nulle.

Nelson rapporte une observation inattendue : certaines séries de référence auraient présenté une variabilité inférieure à la théorie. Il suggère que des opérateurs s'efforçaient de produire une baseline « parfaitement équilibrée ». Cette interprétation est **une hypothèse**, pas une démonstration ; des défauts de génération ou de traitement pourraient également réduire la variance.

### Illustration numérique

Pour un bloc de 200 bits, obtenir 108 « 1 » correspond à un écart de +8, soit environ **1,13 écart-type** : cela n'a rien d'exceptionnel isolément. Une série de nombreux blocs nécessite un plan d'analyse explicite et une correction appropriée pour les tests multiples et les dépendances temporelles.

## 5. Psychokinèse ou « decision augmentation » ? [13:27–17:15]

Deux interprétations sont discutées :

- **Interaction esprit-machine / psychokinèse (PK) :** l'intention agirait sur le processus physique ou sur la distribution des résultats.
- **Decision augmentation / précognition :** l'opérateur ne modifierait pas les bits, mais choisirait inconsciemment le moment d'agir à partir d'une information supposée sur l'issue future.

Nelson considère la seconde hypothèse testable, mais dit que les données PEAR s'accorderaient mieux, selon lui, avec une forme d'interaction de type « champ ». Il admet qu'aucun modèle satisfaisant n'est établi. Son affirmation selon laquelle des mécanismes électromagnétiques conventionnels auraient été écartés est rapportée ici **comme son affirmation**, non comme un résultat vérifié par cette fiche.

**Question méthodologique majeure :** si le participant choisit librement le début des essais, il faut distinguer une influence sur la source d'une sélection des instants de mesure. Un protocole à déclenchement automatisé, horodaté et randomisé aide à séparer ces possibilités.

## 6. Le rôle de l'observateur et de l'expérimentateur [17:14–20:27]

Nelson évoque plusieurs éléments potentiellement impliqués : l'opérateur, l'expérimentateur, la formulation de la question expérimentale et des facteurs non identifiés. Il emploie la métaphore du « coyote » pour parler des résultats parfois inversés ou déroutants. Mishlove propose que des observateurs futurs puissent influencer rétroactivement une expérience ; Nelson discute cette possibilité spéculative. (L'attribution de cette réplique [≈19:41] à Mishlove est probable d'après la suite de l'échange, mais la transcription automatique ne permet pas d'en être certain.)

**Évaluation :** l'effet de l'expérimentateur est une vraie question de conception expérimentale, mais l'hypothèse d'une influence rétroactive n'est pas établie. Il faut distinguer une influence psychologique ordinaire sur le choix des paramètres, une sélection analytique a posteriori et une causalité physique rétrograde. Ces trois notions ne sont pas équivalentes.

## 7. Les expériences de terrain : Field REG [22:06–28:57]

Après miniaturisation des générateurs, les chercheurs les apportent dans des concerts, à l'opéra et dans d'autres rassemblements. Le générateur collecte en continu sans que les personnes présentes aient besoin de connaître sa présence. L'hypothèse est qu'un **état émotionnel collectif cohérent**, plutôt que la simple densité humaine, serait associé à une déviation des données.

Nelson indique que des lieux animés mais sans expérience émotionnelle partagée — centres commerciaux, gares — ont servi de comparateurs, sans produire selon lui le même type de signal. Il estime que les effets de terrain étaient plus importants que ceux du laboratoire, selon une manière particulière de normaliser l'effet par le temps investi. Il ne donne pas dans cet entretien les valeurs nécessaires pour reproduire cette comparaison.

Il reconnaît que l'expérimentateur pourrait constituer une variable confondante. Il avance toutefois un contre-argument [≈28:40] : ses propres résultats comme opérateur sont, dit-il, « plutôt modestes », ce qu'il présente comme une donnée utile contre l'hypothèse que tout l'effet viendrait de lui. Ce contre-argument est faible : un effet de l'expérimentateur n'exige pas que celui-ci soit un bon opérateur en laboratoire. Une mitigation proposée est de confier l'appareil à une autre personne, puis d'analyser les données séparément. **Pour une réplication rigoureuse :** prévoir aussi des périodes témoins, des événements sélectionnés sans consultation des données, des sites témoins, une procédure en aveugle et des métadonnées instrumentales.

## 8. Signatures individuelles et réseau neuronal [28:57–32:42]

Mishlove évoque une expérience de Dean Radin utilisant un réseau neuronal pour reconnaître des « signatures » propres à différents opérateurs à partir de segments de données. Nelson estime que cela rejoint certaines observations du laboratoire. L'entretien ne précise ni architecture du réseau, ni nombre d'exemples, ni séparation entraînement/test, ni procédure de validation ; il est donc impossible d'évaluer la robustesse du résultat ici.

Nelson raconte également que certains opérateurs réussissaient mieux lorsqu'ils établissaient un lien affectif avec l'appareil ou lorsqu'ils fixaient une intention puis cessaient de se concentrer. Il évoque une base d'environ 130 opérateurs, traités comme des collaborateurs plutôt que comme des sujets. L'exemple d'une participante lisant un magazine est **anecdotique** et ne prouve pas l'efficacité de cette stratégie.

**Lien avec l'apprentissage automatique :** il serait intéressant de tester des signatures individuelles, mais uniquement avec validation sur des sessions et des jours entièrement distincts, équilibrage des classes, contrôles de fuite de données, générateurs différents et évaluation sur des participants inconnus. Un classificateur performant peut autrement apprendre des signatures matérielles ou temporelles plutôt que des états mentaux.

## 9. De la noosphère au réseau mondial des « EGGs » [32:42–37:46]

Nelson évoque la **noosphère**, idée d'une enveloppe d'intelligence collective entourant la Terre, associée à Teilhard de Chardin. Il se demande si de grands événements partagés à l'échelle planétaire pourraient se manifester dans des générateurs éloignés les uns des autres.

Le dispositif proposé : plusieurs REG répartis dans le monde transmettent leurs mesures vers un serveur central ; des fenêtres d'événements sont ensuite soumises à des tests statistiques. Le surnom **EGG** renvoie, dans son récit, à une analogie avec un « électroencéphalogramme de Gaïa » : il s'agit d'une **métaphore**, et non d'un EEG mesurant directement l'activité cérébrale ou un champ électrophysiologique terrestre. L'idée vient du fils de Nelson, qui a conçu l'architecture logicielle de collecte ; le programme d'archivage central qui reçoit les données des eggs s'appelle le « basket ».

## 10. Événements mondiaux : funérailles de Diana et corpus de 500 tests [37:46–40:38]

Nelson cite les funérailles de la princesse Diana comme expérience précurseure : des collègues ont enregistré des données sur plusieurs appareils pendant une cérémonie suivie par une audience mondiale. Il décrit une déviation cumulative durant environ six heures. Il présente ce cas comme une motivation importante pour le GCP.

La question du GCP n'est pas simplement « voit-on un pic ? », mais : **pour des fenêtres d'événements définies à l'avance, les statistiques observées s'écartent-elles systématiquement de leur distribution nulle ?** Nelson évoque environ **500 événements formels** et des résultats cumulés qu'il juge très significatifs. La transcription ne donne pas de tableau complet des événements, d'estimation globale d'effet ou de calcul vérifiable de probabilité (voir la section 20 pour le chiffre publié).

**Statistique utilisée.** Nelson dit avoir retenu *un* test primaire et quelques tests secondaires « pour des usages particuliers », sans les nommer. Il précise seulement que la somme cumulative des écarts jusqu'à la fin de la fenêtre « revient à tester un score Z ». C'est l'information manquante la plus importante pour reproduire l'analyse : il faut la chercher dans les publications (Bancel & Nelson, 2008).

### Attention aux courbes cumulatives

Une somme cumulative de fluctuations aléatoires peut montrer des montées, descentes et excursions impressionnantes **même sous l'hypothèse nulle**. Il faut comparer la courbe à une distribution de référence correcte, et non juger sa forme à l'œil. Une courbe montante ne démontre pas en elle-même une anomalie.

## 11. Le point méthodologique le plus solide : la préspécification [40:38–43:52]

Nelson répond à une objection essentielle : si l'on parcourt d'abord les données pour repérer des pics puis cherche ensuite un événement mondial correspondant, on trouvera forcément des coïncidences. Il dit avoir imposé, avant inspection des données pertinentes, la définition de **l'événement, de la fenêtre de début et de fin, et du test statistique**.

C'est un principe scientifique important, indépendant de la validité de l'hypothèse paranormale. Une préinscription utile devrait aussi documenter : règles d'inclusion/exclusion, gestion des données manquantes, correction des comparaisons multiples, traitement des stations défectueuses, définition de l'effet primaire et méthode de simulation du nul.

**Nuance :** le fait qu'un chercheur déclare avoir préspécifié ses analyses ne remplace pas l'audit des documents datés, de leur exhaustivité et de leur application effective.

## 12. Interprétations : champ d'information, Bohm et ordre impliqué [44:36–47:47]

Mishlove propose un lien avec le « quantum foam ». Nelson rapproche plutôt son intuition de l'**ordre impliqué** de David Bohm et d'une notion d'« information active ». Il imagine que des consciences pourraient contribuer à structurer des processus physiques désordonnés. Il évoque aussi, à titre d'illustration, une hypothèse de guérison à distance.

**Distinction impérative :** les travaux de Bohm sont un cadre de réflexion philosophique et physique ; leur invocation ne démontre pas que des pensées modifient les générateurs aléatoires ni qu'une guérison à distance soit possible. L'entretien n'expose aucune dérivation quantitative reliant l'intention, une variable de champ mesurable et une prédiction instrumentale falsifiable.

Pour faire de cette intuition un modèle scientifique, il faudrait au minimum définir une grandeur physique, ses unités, sa dynamique, son couplage au détecteur et des prédictions qui se distinguent de celles du hasard et des artefacts.

## 13. Suite du projet et nouvelles analyses [47:47–56:38]

En 2018, Nelson ne mène plus le programme formel initial, mais continue d'examiner occasionnellement les données et encourage des répliques indépendantes. Il mentionne l'application « Consciousness app » d'Adam Curry, qui pourrait collecter des données de type GCP sur des téléphones, avec géolocalisation, variables géomagnétiques et même mots-clés de recherche Google (projet non réalisé en 2018), ainsi que des travaux de Brian Williams sur des événements de « global harmony » (méditations, fêtes religieuses, marches pour la paix). Il rapporte une déviation cumulée de l'ordre d'une chance sur mille pour une sélection d'un peu plus de cent événements.

**Réserve :** cette analyse de sous-groupe exige une vérification des critères de sélection et de la multiplicité des catégories testées. Une probabilité nominale de 0,001 ne suffit pas à conclure sans connaître l'ensemble du processus analytique.

Nelson souligne que davantage de chercheurs et des expériences convaincantes et reproductibles seraient nécessaires pour susciter un intérêt scientifique plus large.

## 14. Résultats « à l'envers » et limites [56:38–59:14]

Mishlove résume les recherches comme produisant continuellement des résultats significatifs ; Nelson corrige explicitement cette caractérisation : il parle plutôt de résultats **inconstants**, avec des cas inversés. Il mentionne des méditations associées à des tendances négatives, alors que la prédiction formelle allait dans le sens positif. Il raconte aussi le cas d'une opératrice dont la direction des résultats changeait selon qu'elle choisissait elle-même son intention ou qu'une consigne aléatoire la lui imposait.

Ce passage est important : un résultat de signe opposé à la prédiction doit compter dans le bilan confirmatoire, et non être automatiquement requalifié en succès. Les analyses exploratoires peuvent générer de nouvelles hypothèses, mais celles-ci doivent ensuite être testées sur **de nouvelles données**.

Nelson reconnaît enfin que l'idée d'un détecteur d'humeur basé sur ces effets allait au-delà des preuves disponibles.

## 15. Évaluation critique structurée

| Proposition | Ce que rapporte l'entretien | Ce qu'on peut conclure de cette seule source |
|---|---|---|
| Les REG produisent des bits à partir d'un processus physique | Description technique générale | Plausible et testable, mais montage précis non documenté |
| Les opérateurs modifient la moyenne des bits | Nelson rapporte des déviations statistiques | Causalité mentale non démontrée par l'entretien |
| Les groupes émotionnellement cohérents affectent les REG | Résultats de terrain déclarés | Nécessite réplications contrôlées et données accessibles |
| Le réseau GCP réagit à des événements mondiaux | Analyses cumulées sur environ 500 événements | Résultats allégués ; force probante non vérifiable ici |
| Les effets peuvent précéder les événements | Discussion de précognition/rétroaction | Hypothèse spéculative, aucune démonstration spécifique ici |
| Un champ global de conscience existe | Interprétation philosophique de Nelson | Aucune mesure indépendante de ce champ présentée |
| Les analyses sont préspécifiées | Nelson décrit cette règle | Bonne pratique, à auditer sur les archives originales |

### Principales menaces à la validité

1. **Biais ou corrélation des bits :** source, comparateur, horloge, conditionnement, alimentation.
2. **Non-stationnarité :** température, vieillissement, dérive lente, perturbations communes.
3. **Sélection des événements :** choix des fenêtres, événements ignorés, catégories redéfinies.
4. **Multiplicité :** nombreux appareils, statistiques, sous-groupes et fenêtres.
5. **Dépendances entre stations :** synchronisation, traitement partagé, facteurs environnementaux.
6. **Interprétation causale :** association temporelle ne prouve pas une influence de la conscience.
7. **Réplicabilité :** nécessité d'analyses indépendantes sur des données inédites.

### Ce que la vidéo ne permet pas d'établir

La vidéo ne permet pas de vérifier directement les valeurs p globales, les intervalles de confiance, les tailles d'effet, la calibration des appareils, les critères de sélection détaillés, ni les résultats d'une réplication indépendante. Le cas du 11 septembre 2001, parfois cité à propos du GCP, n'est pas abordé du tout dans cet entretien.

## 16. Application proposée : laboratoire personnel de générateurs aléatoires

L'objectif raisonnable est de **construire une expérience capable de réfuter l'hypothèse**, pas un détecteur de conscience présumé fonctionnel.

### Architecture instrumentale

```text
Source physique de bruit (diode / jonction caractérisée)
       ↓
Amplification à faible bruit + filtrage + référence stable
       ↓
Comparateur avec seuil contrôlé
       ↓
Échantillonnage par microcontrôleur ou FPGA
       ↓
Flux de bits bruts + horodatages + télémétrie
       ↓
Enregistrement immuable + analyse Python
```

Pour un montage avec NE5532 et 74LS86 déjà envisagé, le **NE5532** peut être évalué comme amplificateur de conditionnement si son alimentation, son bruit et sa plage de mode commun conviennent ; le **74LS86** peut réaliser un XOR numérique, mais un XOR ne garantit ni l'indépendance ni une source quantique. Il faut mesurer les caractéristiques réelles et ne pas considérer le débiaisage comme une preuve de qualité statistique.

### Protocole A — Qualification de la source (sans participants)

- Enregistrer des données brutes sur plusieurs jours, à plusieurs températures et avec différentes alimentations.
- Mesurer proportion de 1, autocorrélations, dérive par fenêtre, distribution des longueurs de séries et éventuelles périodicités.
- Enregistrer tension d'alimentation, température, fréquence d'échantillonnage et pertes de communication.
- Employer une batterie de tests adaptée (par exemple NIST SP 800-22 comme diagnostic complémentaire), sans confondre « passe les tests » et « est physiquement aléatoire ».
- Définir un générateur de contrôle et une chaîne de traitement identique.

### Protocole B — Intention individuelle en aveugle

- Trois conditions : HIGH, LOW et BASELINE, comme dans PEAR.
- Blocs de 200 bits ; calendrier de conditions généré avant l'essai par une procédure indépendante.
- Ordre randomisé, sessions de durée fixe, opérateur sans accès aux données pendant l'essai.
- Statistique primaire prédéfinie : contraste orienté entre HIGH et LOW, avec définition exacte du calcul et du seuil.
- Séparer essais exploratoires et réplication confirmatoire ; conserver tous les essais et incidents.
- Tester également un flux témoin physiquement séparé, non exposé à l'opérateur.

### Protocole C — « Field REG » local

- Installer deux générateurs calibrés, l'un près d'une activité collective et l'autre dans un environnement témoin.
- Définir **avant l'événement** la fenêtre, la statistique, la direction prédite et les exclusions.
- Répéter sur plusieurs événements comparables et périodes témoins appariées.
- Mesurer les facteurs susceptibles de varier : température, secteur, Wi-Fi, vibrations, occupation, horloge et interruptions.
- Répliquer avec permutation des appareils et des lieux afin de dissocier « effet de lieu » et « effet du matériel ».

### Protocole D — Réseau distribué

Utiliser, si pertinent, plusieurs cartes du laboratoire pour collecter les bits et les métadonnées. La plateforme d'acquisition (Arduino, ESP8266/ESP32 ou FPGA) ne remplace pas la **source physique de hasard**. Chaque nœud devrait avoir un identifiant, une horloge synchronisée, un journal d'état, un flux brut et un contrôle d'intégrité. Une analyse centrale pourrait comparer les périodes d'événements aux fenêtres témoins et tester explicitement les corrélations inter-nœuds.

### Exemple de schéma de données

```csv
utc_timestamp,node_id,session_id,condition,block_id,n_bits,n_ones,temp_c,v_supply_v,quality_flag
2026-11-20T15:00:00Z,REG01,S001,BASELINE,1,200,102,22.4,5.01,OK
```

**Important :** cette ligne est un exemple fictif de format, pas une mesure.

## 17. Questions de recherche prioritaires

1. Un résultat subsiste-t-il lorsque la condition HIGH/LOW est attribuée automatiquement et cachée jusqu'à la fin ?
2. Les anomalies éventuelles suivent-elles l'opérateur, le générateur, le lieu ou la période de mesure ?
3. L'effet allégué apparaît-il dans les **bits bruts** ou seulement après une transformation statistique ?
4. Une corrélation entre plusieurs générateurs dépasse-t-elle ce qu'expliquent les horloges, réseaux et perturbations communes ?
5. Une signature individuelle peut-elle être prédite sur des sessions futures sans fuite de données ?
6. Les résultats se reproduisent-ils après verrouillage complet du protocole et des scripts ?
7. Une hypothèse de rétrocausalité produit-elle une prédiction prospective distincte d'un simple choix de fenêtres a posteriori ?

## 18. Repères chronologiques pour retrouver les passages

| Horodatage | Sujet |
|---|---|
| 02:00–06:00 | Arrivée à Princeton, histoire de PEAR et de Schmidt |
| 06:00–10:31 | REG physique, diode, effet tunnel, pseudo-aléatoire |
| 10:31–13:27 | Calibration, blocs de 200 bits, protocole tripolaire |
| 13:27–17:14 | Interaction esprit-machine, précognition, décision augmentée |
| 17:14–20:35 | Observateur, expérimentateur, spéculations rétroactives |
| 20:35–25:47 | Transition vers les Field REG, cohérence émotionnelle |
| 25:47–32:42 | Contrôles de terrain, signatures individuelles, réseau neuronal |
| 32:42–37:46 | Noosphère, naissance du GCP, réseau EGG |
| 37:46–40:38 | Funérailles de Diana et événements mondiaux |
| 40:38–43:52 | Préspécification et risques de sélection a posteriori |
| 43:52–47:47 | Accès aux résultats, Bohm, champ d'information |
| 47:47–53:07 | Fin du protocole formel, pistes mobiles, « global harmony » |
| 53:07–56:38 | Questions futures et intérêt scientifique |
| 56:38–59:14 | Résultats inversés et limites d'interprétation |

## 19. Conclusion pour le projet « Conscience globale »

L'intérêt le plus directement exploitable de cette entrevue n'est pas qu'elle démontre un effet de la conscience sur la matière : **elle fournit une famille d'hypothèses testables et un cadre expérimental à améliorer**. Les expériences PEAR suggèrent une comparaison contrôlée entre intentions opposées ; les Field REG suggèrent des mesures continues lors d'événements ; le GCP montre l'intérêt, mais aussi les difficultés, d'une collecte distribuée et d'une analyse statistique préenregistrée.

La priorité pratique est de fabriquer **un REG physique fiable**, puis d'établir une référence instrumentale longue et indépendante de toute intervention humaine. Seulement ensuite, mener des expériences intentionnelles préenregistrées, avec témoins et réplications. Si des anomalies persistent, l'étape suivante consiste à éliminer méthodiquement les explications électroniques, environnementales et statistiques avant d'envisager une interprétation plus ambitieuse.

## 20. Contexte externe : le résultat publié et la critique de Bancel

*Section ajoutée après recherche ; ces éléments ne viennent pas de l'entretien.*

- **Résultat global.** Nelson (2024, *Journal of Anomalous Experience and Cognition*) rapporte que les résultats cumulés sur les 500 événements formels confirment l'hypothèse avec **Z = 7,31**.
- **Critique interne de Peter Bancel.** Physicien, collaborateur du GCP depuis 2001, Bancel a publié « Searching for Global Consciousness: A Seventeen Year Exploration » (*Explore*, 2017). Sur 17 ans et près de 500 événements, il admet l'écart d'environ 7 écarts-types, mais conclut que les données n'appuient **pas** l'hypothèse d'une conscience globale : le résultat s'expliquerait mieux par un **effet orienté vers un but** (*goal-oriented effect*) lié à des individus, en particulier aux décisions de l'équipe lorsqu'elle fixait les paramètres de chaque test (choix des événements et des fenêtres).
- **Réponse de Nelson.** Dans « Weighting the Parameters » puis dans son article de 2024, Nelson soutient que plusieurs analyses complémentaires révèlent une structure qu'un modèle d'effet de l'expérimentateur ne peut expliquer, mais qu'un modèle de type champ englobe naturellement.

**Conséquence pour le projet « Conscience globale ».** Si Bancel a raison, le maillon faible n'est ni le matériel ni la statistique, mais **le choix humain des fenêtres d'événements**, même préenregistré. Les fenêtres témoins fictives (*sham windows*) déjà prévues contrôlent le taux de faux positifs, mais ne départagent pas les deux modèles. L'étape suivante serait une **sélection automatique des événements** selon une règle fixée d'avance et appliquée sans intervention humaine (par exemple : tout événement dépassant un seuil d'audience ou de couverture sur une source externe donnée), avec paramètres de fenêtre fixes. Un modèle « champ » prédit un effet sur ces événements ; un modèle « orienté vers un but » prédit qu'il disparaît quand plus personne ne choisit les paramètres.

### Références

- Bancel, P. & Nelson, R. (2008). « The GCP Event Experiment: Design, Analytical Methods, Results ». *Journal of Scientific Exploration*, 22(3), 309–333. https://noosphere.princeton.edu/papers/pdf/GCP.JSE.B&N.2008.pdf
- Bancel, P. (2017). « Searching for Global Consciousness: A Seventeen Year Exploration ». *Explore*.
- Nelson, R. « Weighting the Parameters, a Response to Bancel's “Searching for Global Consciousness” ». https://core.ac.uk/download/229001747.pdf
- Nelson, R. (2024). « Global Consciousness: Manifesting Meaningful Structure in Random Data ». *Journal of Anomalous Experience and Cognition*. https://doi.org/10.31156/jaex.25553
- Psi Encyclopedia (SPR), « Peter A Bancel ». https://psi-encyclopedia.spr.ac.uk/articles/peter-bancel/

---

### Note sur la source

Cette fiche résume et analyse **l'entrevue de 2018 telle que transcrite**. Les horodatages sont approximatifs ; les noms propres et certains termes techniques ont été normalisés lorsque le contexte les rendait clairs. Les interprétations critiques, formules, exemples numériques et propositions de protocoles sont des **ajouts analytiques** et non des citations de Roger Nelson. Les sections 1 à 19 reposent uniquement sur l'entretien ; seule la section 20 s'appuie sur des sources externes, sans lecture intégrale des articles cités.
