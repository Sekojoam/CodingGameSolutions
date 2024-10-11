    Objectif
Une fois téléporté dans la structure, votre mission sera de :
atteindre la salle de commande depuis laquelle vous désactiverez le champ de force
revenir à votre position de départ une fois le champ de force désactivé

    Règles
La structure se présente comme un labyrinthe rectangulaire composé de cellules. Une fois dans le labyrinthe, Rick peut aller dans les directions suivantes: haut, bas, gauche et droite (UP, DOWN, LEFT, RIGHT).

Rick utilise son tricordeur pour scanner la zone se trouvant autour de lui mais à cause des interférences, il ne peut scanner que les cellules situées dans un carré de 5 cases de côté et centré sur lui.

Malheureusement, Spock avait raison, il s'agit bien d'un piège ! Une fois le poste de commande atteint, le compte-à-rebours d'une alarme se déclenche et vous avez un nombre limité de tours avant que l'alarme ne s'active. Une fois l'alarme activée, c'en est fini de Rick...

Rick échouera si l'une de ces situations se produit :
Le jetpack de Rick n'a plus d'énergie. Vous avez assez d'énergie pour 1200 mouvements.
Rick n'atteint pas sa position de départ avant que l'alarme ne s'active. Le compte-à-rebours de l'alarme se déclenche une fois la salle de commande atteinte.
Rick touche un mur ou le sol : il est déchiqueté par un piège mécanique.
Vous gagnez si vous atteignez la salle de commande et revenez à votre position de départ avant que l'alarme ne s'active.

    Format du labyrinthe
Le labyrinthe est fourni en entrée sous forme ASCII. Le caractère # représente un mur, le caractère . représente un espace vide, la lettre T représente votre position de départ, la lettre C représente la salle de commande et le caractère ? représente une cellule que vous n'avez pas encore scannée. Par exemple :

??????????????????????????????
#..............???????????????
#.#############???????????????
#.....T........???????????????
#.......................#.#..#
#.#######################.#..#
#.....##......##......#....###
#...####..##..##..##..#..#...#
#.........##......##.....#.C.#
##############################

Position de départ ligne 3, colonne 6.

Salle de commande ligne 8, colonne 27.

(La numérotation commence à zéro)

 	Note
Les tests fournis et les validateurs utilisés pour le calcul du score sont similaires mais différents.

 	Entrées du jeu
Le programme doit d'abord lire les données d'initialisation depuis l'entrée standard, puis, dans une boucle infinie, lire depuis l'entrée standard les données relatives au labyrinthe et fournir sur la sortie standard les instructions de mouvement de Rick.

Entrée d'initialisation

Ligne 1 : 3 entiers : R C A

R,C sont respectivement le nombre de lignes et de colonnes du labyrinthe.

A indique le nombre initial du compte-à-rebours de l'alarme, c-à-d le nombre de tours maximum dont dispose Rick pour revenir de la salle de commande à sa position de départ.

Entrée pour un tour de jeu

Ligne 1 : 2 entiers : KR and KC. Rick est situé dans le labyrinthe ligne KR,colonne KC. La cellule ligne 0, colonne 0 est située dans le coin haut gauche du labyrinthe.


R lignes suivantes : C caractères  # ou  . ou  T ou C ou  ? (c-à-d une ligne du labyrinthe en ASCII)


Sortie pour un tour de jeu

Une ligne unique indiquant le mouvement à effectuer : UP DOWN LEFT ou  RIGHT

Contraintes

10 ≤ R ≤ 100

20 ≤ C ≤ 200

1 ≤ A ≤ 100

0 ≤ KR < R

0 ≤ KC < C

Temps de réponse pour un tour ≤ 150ms

Il y a un seul caractère T et un seul caractère C dans le labyrinthe.

