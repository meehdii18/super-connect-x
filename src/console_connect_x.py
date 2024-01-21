# ---LIBRARIES---#
import copy  # Accès à la fonction deepcopy
import random as rnd  # Accès aux fonctions d'aléatoire pour que l'IA soit moins prévisible

grid_type = list[list[int]]  # Définition du type grid (tableau d'entiers en deux dimensions)
perk_type = list[bool, bool]  # Définition du type perk (tableau de deux booléens)
gamestate_type = tuple[
    grid_type, perk_type, int]  # Définition du type gamestate (tuple d'une grille, des états des atouts et joueur dont c'est le tour)
gametree_type = list[gamestate_type]  # Définition du type gametree (tableau de gamestate)


def init(board_width: int = 7, board_height: int = 6) -> grid_type:
    """
    Fonction d'initialisation de la grille de jeu.
    :param board_width: Largeur de la grille de jeu.
    :param board_height: Hauteur de la grille de jeu.
    :return: Grille de jeu initialisée vide (toutes les cases valent 0).
    """
    grid = [[0 for _ in range(board_width)] for _ in range(board_height)]  # Création d'une tableau 2D de 0
    return grid  # On renvoie la grille initialisée


def clear(grid: grid_type) -> grid_type:
    """
    Fonction de réinitialisation de la grille de jeu.
    :param grid: Grille de jeu à réinitialiser.
    :return: Grille de jeu vide (toutes les cases contiennent des 0).
    """
    board_width = len(grid[0])  # Récupération de la largeur de la grille passée en paramètre
    board_height = len(grid)  # Récupération de la hauteur de la grille passée en paramètre
    grid = init(board_width, board_height)  # Appel de la fonction d'initialisation
    return grid  # On renvoie la grille réinitialisée


def affiche(grid: grid_type) -> None:
    """
    Fonction d'affichage de la grille dans la console.
    :param grid: Grille de jeu à afficher.
    :return: Rien (seulement des print).
    """
    board_width = len(grid[0])  # Récupération de la largeur de la grille passée en paramètre
    board_height = len(grid)  # Récupération de la hauteur de la grille passée en paramètre
    num_col = [i for i in range(board_width)]  # Récupération des numéros des colonnes
    print("  |", num_col)  # Affichage des numéros des colonnes
    print("--" + "|" + "-" * ((len(num_col)) * 3 + 1))  # Affichage de la délimitation numéros des colonnes/grille
    for row in range(board_height):  # Boucle d'affichage de chaque ligne
        print(row, "|", end=" ")  # Affichage du numéro de la ligne
        for col in grid[row]:  # Boucle d'affichage de chaque jeton de la ligne
            if col == 0:  # Cas où il n'y a pas de jeton
                print("\u001b[37m", end="")  # On change la couleur d'affichage à blanc
            elif col == 1:  # Cas où le jeton est celui du joueur 1
                print("\x1B[38;2;255;0;0m", end="")  # On change la couleur d'affichage à rouge
            elif col == 2:  # Cas où le jeton est celui du joueur 2
                print("\x1B[38;2;255;255;0m", end="")  # On change la couleur d'affichage à jaune
            # endif
            print("██ ", end="")  # On affiche des caractères pleins pour représenter le jeton
        # endfor
        print("\u001b[37m")  # On change à nouveau la couleur à blanc à la fin de chaque ligne
    # endfor


def check_valid_play(play_column: int, grid: grid_type) -> bool:
    """
    Fonction qui vérifie si on peut jouer le coup spécifié dans la grille.
    :param play_column: Colonne où l'on veut vérifier qu'il est possible de jouer.
    :param grid: Grille dans laquelle on veut vérifier la validité du coup.
    :return: Vrai si le coup est valide ; Faux sinon.
    """
    if grid[0][play_column] == 0:  # Cas où la colonne n'est pas totalement remplie
        valid_play = True  # Le coup est possible
    else:  # Cas où la colonne est totalement remplie
        valid_play = False  # Le coup n'est pas possible
    # endif
    return valid_play  # On renvoie le booléen indiquant la validité du coup


def check_full_grid(grid: grid_type, perk: perk_type) -> bool:
    """
    Fonction qui vérifie si la grille est pleine et que les atouts sont utilisés.
    :param grid: Grille que l'on veut vérifier.
    :param perk: Liste des booléens qui indiquent si les joueurs ont utilisé leur atout.
    :return: Vrai si la grille est pleine ; Faux sinon.
    """
    board_width = len(grid[0])  # Récupération de la largeur de la grille passée en paramètre
    column = 0  # Initialisation de la colonne à vérifier
    full = False  # Initialisation du booléen à Faux.
    if perk[0] and perk[
        1]:  # Cas où l'atout a été utilisé par les deux joueurs, si ce n'est pas le cas la fonction renvoie Faux
        full = True  # On change la valeur du booléen à Vrai
        while (column < board_width  # On itère chacune des colonnes
               and full):  # Si une colonne n'est pas pleine, on sort de la boucle
            if check_valid_play(column, grid):  # On vérifie pour chaque colonne qu'elle n'est pas pleine
                full = False  # Si la colonne n'est pas pleine, la grille non plus donc on change la valeur du booléen à Vrai
            # endif
            column += 1  # On passe à la colonne suivante
        # endwhile
    # endif
    return full  # On renvoie le booléen indiquant si la grille est pleine


def undo(gameadvance: gametree_type) -> None:
    """
    Fonction qui annule le dernier coup joué dans une partie entre deux joueurs.
    :param gameadvance: Arbre de jeu dans lequel on veut remonter.
    :return: Aucun (arbre de jeu modifié directement)
    """
    if len(gameadvance) >= 2:  # On vérifie qu'il existe des coups à annuler
        gameadvance.pop(-1)  # On supprime le dernier coup joué de l'arbe de jeu
    # endif


def undo_AI(gameadvance: gametree_type) -> None:
    """
    Fonction qui annule le dernier coup joué par l'IA et celui joué par le joueur avant cela.
    :param gameadvance: Arbre de jeu dans lequel on veut remonter.
    :return: Aucun (arbre de jeu modifié directement)
    """
    for _undo in range(2):  # On supprime les deux derniers coups de l'arbre de jeu
        undo(gameadvance)  # On appelle la fonction undo qui supprimera les coups
    # endfor


def use_perk(gamestate_not_to_touch: gamestate_type) -> gamestate_type:
    """
    Fonction qui supprime la ligne du bas de la grille, et qui "descend" tous les jetons en conséquence.
    :param gamestate_not_to_touch: L'état auquel le jeu est avant d'avoir joué l'atout, à ne pas modifier directement -> utiliser deepcopy().
    :return: L'état auquel le jeu est après avoir joué l'atout.
    """
    gamestate = copy.deepcopy(gamestate_not_to_touch)  # On crée une copie de l'état du jeu courant à l'aide de deepcopy
    grid = gamestate[0]  # Récupération de la grille de l'état de jeu passé en paramètre
    board_width = len(grid[0])  # Récupération de la largeur de la grille passée en paramètre
    board_height = len(grid)  # Récupération de la hauteur de la grille passée en paramètre
    player = gamestate[2]  # Récupération du joueur dont c'est le tour de jouer
    grid.pop(board_height - 1)  # Suppression de la ligne du bas de la grille
    grid.insert(0, [0 for _width in range(
        board_width)])  # Insertion d'une nouvelle ligne vide en haut pour conserver la bonne taille de grille
    gamestate[1][player - 1] = True  # Enregistrement de l'utilisation de l'atout par le joueur dont c'est le tour
    return gamestate  # On renvoie le nouvel état du jeu


def add_coin(play_column: int, player: int, grid_not_to_touch: grid_type) -> grid_type:
    """
    Fonction qui ajoute un jeton du joueur spécifié dans la colonne spécifiée de la grille spécifiée.
    :param play_column: Colonne où ajouter le jeton.
    :param player: Joueur dont le jeton doit être ajouté.
    :param grid_not_to_touch: Grille dans laquelle ajouter le jeton, à ne pas modifier directement -> utiliser deepcopy().
    :return: Grille dans laquelle le jeton a été ajouté.
    """
    grid = copy.deepcopy(grid_not_to_touch)  # On crée une copie de la grille à l'aide de deepcopy
    board_width = len(grid[0])  # Récupération de la largeur de la grille passée en paramètre
    board_height = len(grid)  # Récupération de la hauteur de la grille passée en paramètre
    if (0 <= play_column < board_width):  # On vérifie que la colonne spécifiée appartient bien à la grille
        row = board_height - 1  # On part du bas de la grille
        actual_coin = grid[row][play_column]  # On prend l'emplacement du bas de la grille dans la colonne spécifiée
        while (actual_coin  # On regarde si l'emplacement actuel contient un jeton
               and row >= 0):  # On vérifie qu'on ne sort par de la grille
            actual_coin = grid[row][play_column]  # On récupère l'emplacement actuel
            if actual_coin:  # On regarde si l'emplacement actuel contient un jeton
                row -= 1  # On passe à la ligne suivante
            # endif
        # endwhile
        grid[row][play_column] = player  # On ajoute le jeton du joueur spécifié à l'emplacement courant
    # endif
    return grid  # On renvoie la nouvelle grille


def check_row(required_coins: int, grid: grid_type, player: int) -> int:
    """
    Fonction qui vérifie si il y a une victoire du joueur spécifié sur les lignes.
    :param required_coins: Le nombre de jetons à aligner pour gagner.
    :param grid: La grille où chercher une victoire.
    :param player: Le joueur pour qui chercher une victoire.
    :return: player si une victoire est trouvée ; 0 sinon.
    """
    board_width = len(grid[0])  # Récupération de la largeur de la grille passée en paramètre
    board_height = len(grid)  # Récupération de la hauteur de la grille passée en paramètre
    row = 0  # On initialise la ligne à 0
    count = 0  # On initialise le compte de jetons alignés à 0
    while (row < board_height  # On vérifie qu'on ne sort pas de la grille
           and count < required_coins):  # On vérifie que l'on n'a pas encore trouvé de victoire
        col = 0  # On initialise la colonne à 0
        count = 0  # On initialise le compte de jetons alignés à 0
        while (col < board_width  # On vérifie qu'on ne sort pas de la grille
               and count < required_coins  # On vérifie que l'on n'a pas encore trouvé de victoire
               and board_width - col >= required_coins - count):  # On vérifie en fonction du compte actuel qu'une victoire est encore possible sur cette ligne
            if grid[row][col] == player:  # Cas où l'emplacement actuel contient un jeton du joueur spécifié
                count += 1  # On ajoute 1 au compte
            else:  # Cas où l'emplacement actuel ne contient pas un jeton du joueur spécifié
                count = 0  # on réinitialise le compte à 0
            # endif
            col += 1  # On passe à la colonne suivante
        # endwhile
        row += 1  # On passe à la ligne suivante
    # endwhile
    if count == required_coins:  # Cas où une victoire a été trouvée
        winner = player  # On assigne l'entier correspondant au joueur à la variable indiquant la victoire
    else:  # Cas où aucune victoire n'a été trouvée
        winner = 0  # On assigne 0 à la variable indiquant la victoire
    # endif
    return winner  # On renvoie la variable indiquant la victoire


def check_col(required_coins: int, grid: grid_type, player: int) -> int:
    """
    Fonction qui vérifie si il y a une victoire du joueur spécifié sur les colonnes.
    :param required_coins: Le nombre de jetons à aligner pour gagner.
    :param grid: La grille où chercher une victoire.
    :param player: Le joueur pour qui chercher une victoire.
    :return: player si une victoire est trouvée ; 0 sinon.
    """
    board_width = len(grid[0])  # Récupération de la largeur de la grille passée en paramètre
    board_height = len(grid)  # Récupération de la hauteur de la grille passée en paramètre
    col = 0  # On initialise la colonne à 0
    count = 0  # On initialise le compte de jetons alignés à 0
    while (col < board_width  # On vérifie qu'on ne sort pas de la grille
           and count < required_coins):  # On vérifie que l'on n'a pas encore trouvé de victoire
        row = 0  # On initialise la ligne à 0
        count = 0  # On initialise le compte de jetons alignés à 0
        while (row < board_height  # On vérifie qu'on ne sort pas de la grille
               and count < required_coins  # On vérifie que l'on n'a pas encore trouvé de victoire
               and board_height - row >= required_coins - count):  # On vérifie en fonction du compte actuel qu'une victoire est encore possible sur cette colonne
            if grid[row][col] == player:  # Cas où l'emplacement actuel contient un jeton du joueur spécifié
                count += 1  # On ajoute 1 au compte
            else:  # Cas où l'emplacement actuel ne contient pas un jeton du joueur spécifié
                count = 0  # on réinitialise le compte à 0
            # endif
            row += 1  # On passe à la ligne suivante
        # endwhile
        col += 1  # On passe à la colonne suivante
    # endwhile
    if count == required_coins:  # Cas où une victoire a été trouvée
        winner = player  # On assigne l'entier correspondant au joueur à la variable indiquant la victoire
    else:  # Cas où aucune victoire n'a été trouvée
        winner = 0  # On assigne 0 à la variable indiquant la victoire
    # endif
    return winner  # On renvoie la variable indiquant la victoire


def check_up_diag(required_coins: int, grid: grid_type, player: int) -> int:
    """
    Fonction qui vérifie si il y a une victoire du joueur spécifié sur les diagonales montantes.
    :param required_coins: Le nombre de jetons à aligner pour gagner.
    :param grid: La grille où chercher une victoire.
    :param player: Le joueur pour qui chercher une victoire.
    :return: player si une victoire est trouvée ; 0 sinon.
    """
    board_width = len(grid[0])  # Récupération de la largeur de la grille passée en paramètre
    board_height = len(grid)  # Récupération de la hauteur de la grille passée en paramètre
    row_start = required_coins - 1  # On initialise la ligne de départ
    col_start = 0  # On initialise la colonne de départ
    count = 0  # On initialise le compte de jetons alignés à 0
    while (
            col_start <= board_width - required_coins  # On vérifie qu'il peut y avoir une victoire sur la diagonale montante partant d'ici
            and count < required_coins):  # On vérifie que l'on n'a pas encore trouvé de victoire
        row = row_start  # On initialise la ligne de l'emplacement à vérifier
        col = col_start  # On initialise la colonne de l'emplacement à vérifier
        count = 0  # On initialise le compte de jetons alignés à 0
        while (col < board_width  # On vérifie qu'on ne sort pas de la grille
               and row >= 0  # On vérifie qu'on ne sort pas de la grille
               and count < required_coins):  # On vérifie que l'on n'a pas encore trouvé de victoire
            if grid[row][col] == player:  # Cas où l'emplacement actuel contient un jeton du joueur spécifié
                count += 1  # On ajoute 1 au compte
            else:  # Cas où l'emplacement actuel ne contient pas un jeton du joueur spécifié
                count = 0  # on réinitialise le compte à 0
            # endif
            row -= 1  # On passe à la ligne suivante
            col += 1  # On passe à la colonne suivante
        # endwhile
        if row_start == board_height - 1:  # Cas où on n'est pas encore arrivé au bas de la grille
            col_start += 1  # On passe à la colonne de départ suivante
        else:  # Cas où on est arrivé au bas de la grille
            row_start += 1  # On passe à la ligne de départ suivante
        # endif
    # endwhile
    if count == required_coins:  # Cas où une victoire a été trouvée
        winner = player  # On assigne l'entier correspondant au joueur à la variable indiquant la victoire
    else:  # Cas où aucune victoire n'a été trouvée
        winner = 0  # On assigne 0 à la variable indiquant la victoire
    # endif
    return winner  # On renvoie la variable indiquant la victoire


def check_down_diag(required_coins: int, grid: grid_type, player: int) -> int:
    """
    Fonction qui vérifie si il y a une victoire du joueur spécifié sur les diagonales descendantes.
    :param required_coins: Le nombre de jetons à aligner pour gagner.
    :param grid: La grille où chercher une victoire.
    :param player: Le joueur pour qui chercher une victoire.
    :return: player si une victoire est trouvée ; 0 sinon.
    """
    board_width = len(grid[0])  # Récupération de la largeur de la grille passée en paramètre
    board_height = len(grid)  # Récupération de la hauteur de la grille passée en paramètre
    row_start = board_height - required_coins  # On initialise la ligne de départ
    col_start = 0  # On initialise la colonne de départ
    count = 0  # On initialise le compte de jetons alignés à 0
    while (
            col_start <= board_width - required_coins  # On vérifie qu'il peut y avoir une victoire sur la diagonale descendante partant d'ici
            and count < required_coins):  # On vérifie que l'on n'a pas encore trouvé de victoire
        row = row_start  # On initialise la ligne de l'emplacement à vérifier
        col = col_start  # On initialise la colonne de l'emplacement à vérifier
        count = 0  # On initialise le compte de jetons alignés à 0
        while (col < board_width  # On vérifie qu'on ne sort pas de la grille
               and row < board_height  # On vérifie qu'on ne sort pas de la grille
               and count < required_coins):  # On vérifie que l'on n'a pas encore trouvé de victoire
            if grid[row][col] == player:  # Cas où l'emplacement actuel contient un jeton du joueur spécifié
                count += 1  # On ajoute 1 au compte
            else:  # Cas où l'emplacement actuel ne contient pas un jeton du joueur spécifié
                count = 0  # on réinitialise le compte à 0
            # endif
            row += 1  # On passe à la ligne suivante
            col += 1  # On passe à la colonne suivante
        # endwhile
        if row_start == 0:  # Cas où on n'est pas encore arrivé en haut de la grille
            col_start += 1  # On passe à la colonne de départ suivante
        else:  # Cas où on est arrivé en haut de la grille
            row_start -= 1  # On passe à la ligne de départ suivante
        # endif
    # endwhile
    if count == required_coins:  # Cas où une victoire a été trouvée
        winner = player  # On assigne l'entier correspondant au joueur à la variable indiquant la victoire
    else:  # Cas où aucune victoire n'a été trouvée
        winner = 0  # On assigne 0 à la variable indiquant la victoire
    # endif
    return winner  # On renvoie la variable indiquant la victoire


def check_victory(required_coins: int, grid: grid_type) -> int:
    """
    Fonction qui vérifie si il y a une victoire dans la grille spécifiée.
    :param required_coins: Le nombre de jetons à aligner pour gagner.
    :param grid: La grille où chercher une victoire.
    :return: le joueur pour lequel une victoire est trouvée ; 0 si aucune victoire trouvée.
    """
    victory = 0  # On initialise la variable indiquant une victoire
    for player in (1, 2):  # On regarde les victoires pour chacun des deux joueurs
        victory |= (check_row(required_coins, grid, player)  # On vérifie les victoires sur les lignes
                    | check_col(required_coins, grid, player)  # On vérifie les victoires sur les colonnes
                    | check_up_diag(required_coins, grid,
                                    player)  # On vérifie les victoires sur les diagonales montantes
                    | check_down_diag(required_coins, grid,
                                      player))  # On vérifie les victoires sur les diagonales descendantes
    # endfor
    return victory  # On renvoie la variable indiquant une victoire


def evaluate_grid(required_coins: int, grid: grid_type) -> int:
    """
    Fonction d'évaluation de la grille pour l'IA, de grandes valeurs sont une bonne chose pour l'IA.
    :param required_coins: Le nombre de jetons à aligner pour gagner.
    :param grid: La grille à évaluer.
    :return: Le score d'évaluation de la grille
    """
    score = 0  # On initialise le score à 0
    weight = [[100, 5, 2],  # Initialisation des bonus pour l'IA (bons coups de l'IA)
              [-4, -1, 0]]  # Initialisation des malus pour l'IA (bons coups du joueurs)
    for player in (1, 2):  # On évalue les combinaisons du joueur et de l'IA
        for distance_to_win in range(3):  # On parcours les combinaisons de moins en moins longues
            victory_indicator_row = check_row(required_coins - distance_to_win, grid, player)  # Combinaisons en ligne
            victory_indicator_col = check_col(required_coins - distance_to_win, grid, player)  # Combinaisons en colonne
            victory_indicator_diag_up = check_up_diag(required_coins - distance_to_win, grid,
                                                      player)  # Combinaisons en diagonales montantes
            victory_indicator_diag_down = check_down_diag(required_coins - distance_to_win, grid,
                                                          player)  # Combinaisons en diagonales descendantes
            for victory_indicator in [victory_indicator_row, victory_indicator_col, victory_indicator_diag_up,
                                      victory_indicator_diag_down]:  # On regarde les indicateurs de chaque direction
                if victory_indicator == player:  # Cas de bonne combinaison trouvée
                    score += weight[player - 1][distance_to_win]  # On fait évoluer le score en fonction des bonus/malus
                # endif
            # endfor
        # endfor
    # endfor
    return score  # On renvoie le score


def min_max(gamestate: gamestate_type, required_coins: int, depth: int, maximizingPlayer: bool) -> tuple:
    """
    Fonction récursive qui cherche les meilleurs coups pour l'IA.
    :param gamestate: L'état du jeu auquel il faut chercher un bon coup.
    :param required_coins: Le nombre de jetons à aligner pour gagner.
    :param depth: Le nombre de coup d'avance que l'IA explore pour faire son choix.
    :param maximizingPlayer: Si Vrai, l'IA cherche le meilleur coup pour elle ; Si Faux, l'IA cherche le meilleur coup pour le joueur.
    :return: Un tuple contenant la colonne choisie par l'IA et la valeur d'évaluation associée au coup sur cette colonne.
    """
    grid = gamestate[0]  # Récupération de la grille de l'état de jeu passé en paramètre
    board_width = len(grid[0])  # Récupération de la largeur de la grille passée en paramètre
    board_height = len(grid)  # Récupération de la hauteur de la grille passée en paramètre
    perk = gamestate[1]  # Récupération de l'utilisation des atouts de l'état de jeu passé en paramètre
    full_board = check_full_grid(grid, perk)  # On vérifie si la grille est pleine
    final_position_victory = check_victory(required_coins, grid)  # On vérifie si il y a une victoire dans la grille
    if (depth == 0  # Cas où l'IA atteint la limite de coup qu'elle peut calculer
            or full_board  # Cas où il n'y a plus de coup possible pour aucun des 2 camps
            or final_position_victory):  # Cas où il y a une victoire d'un des camps
        if depth != 0:  # Cas où l'IA n'a pas atteint la limite de coup qu'elle peut calculer
            if final_position_victory == 2:  # Cas où il y a une victoire de l'IA
                return (None, 1000000000)  # On renvoie un score très bon
            elif final_position_victory == 1:  # Cas où il y a une victoire du joueur
                return (None, -100000000)  # On renvoie un score très mauvais
            else:  # Cas où il n'y a pas de victoire
                return (None, 0)  # On renvoie un score neutre
            # endif
        else:  # Cas où l'IA atteint la limite de coup qu'elle peut calculer
            return (None, evaluate_grid(required_coins, grid))  # On renvoie l'évaluation de la grille
        # endif
    # endif
    playable = [col for col in range(board_width) if
                check_valid_play(col, grid)]  # On crée la liste de tous les coups possibles

    if maximizingPlayer:  # Cas où c'est à l'IA de jouer
        value = -10000000  # On donne un score très mauvais pour l'IA, afin qu'elle trouve mieux
        if not perk[1]:  # Cas où l'IA peut encore utiliser son atout
            playable.append("perk")  # On ajoute l'atout aux cas possibles
        # endif
        best_play_list = [rnd.choice(
            playable)]  # On crée une liste des meilleurs coups dans laquelle on met un des coups possibles, choisi aléatoirement
        for col in playable:  # On teste chaque coup possible
            if col == "perk":  # Cas où le coup étudié est l'atout
                new_gamestate = copy.deepcopy(gamestate)  # On crée une copie de l'état du jeu
                new_gamestate = use_perk(new_gamestate)  # On y joue l'atout
                new_gamestate = (new_gamestate[0], new_gamestate[1], 1)  # On change le tour de jeu
                new_score = min_max(new_gamestate, required_coins, depth - 1,
                                    False)  # La fonction se rappelle elle même avec une profondeur de moins, on récupère le score
                if new_score[1] > value:  # Cas où le score trouvé est meilleur que celui que l'ordi avait enregistré
                    value = new_score[1]  # On met à jour le score avec la nouvelle meilleure valeur
                    best_play_list = [
                        col]  # On réinitialise la liste des meilleurs coups à la colonne du nouveau meilleur coup
                elif new_score[1] == value:  # Cas où le score trouvé est le même que celui que l'ordi avait enregistré
                    best_play_list.append(col)  # On ajoute à la liste des meilleurs coups la colonne trouvée
                # endif
            else:  # Cas où le coup étudié n'est pas l'atout
                grid_copy = copy.deepcopy(grid)  # On crée une copie de la grille de jeu
                grid_copy = add_coin(col, 2, grid_copy)  # On y joue le coup de la colonne correspondante "col"
                new_gamestate = (
                    grid_copy, perk, 1)  # On crée l'état de jeu avec la nouvelle grille, on y change le tour de jeu
                new_score = min_max(new_gamestate, required_coins, depth - 1,
                                    False)  # La fonction se rappelle elle même avec une profondeur de moins, on récupère le score
                if new_score[1] > value:  # Cas où le score trouvé est meilleur que celui que l'ordi avait enregistré
                    value = new_score[1]  # On met à jour le score avec la nouvelle meilleure valeur
                    best_play_list = [
                        col]  # On réinitialise la liste des meilleurs coups à la colonne du nouveau meilleur coup
                elif new_score[1] == value:  # Cas où le score trouvé est le même que celui que l'ordi avait enregistré
                    best_play_list.append(col)  # On ajoute à la liste des meilleurs coups la colonne trouvée
                # endif
            # endif
        # endfor
        column = rnd.choice(
            best_play_list)  # On choisit aléatoirement un des meilleurs coups (dont l'évaluation est égale)
        return (column, value)  # On renvoie le coup choisi et la valeur d'évaluation associée

    else:  # Cas où c'est au joueur de jouer
        value = 10000000  # On donne un score très bon pour l'IA, afin qu'elle trouve mieux pour le joueur
        if not perk[0]:  # Cas où le joueur peut encore utiliser son atout
            playable.append("perk")  # On ajoute l'atout aux cas possibles
        # endif
        best_play_list = [rnd.choice(
            playable)]  # On crée une liste des meilleurs coups dans laquelle on met un des coups possibles, choisi aléatoirement
        for col in playable:  # On teste chaque coup possible
            if col == "perk":  # Cas où le coup étudié est l'atout
                new_gamestate = copy.deepcopy(gamestate)  # On crée une copie de l'état du jeu
                new_gamestate = use_perk(new_gamestate)  # On y joue l'atout
                new_gamestate = (new_gamestate[0], new_gamestate[1], 2)  # On change le tour de jeu
                new_score = min_max(new_gamestate, required_coins, depth - 1,
                                    True)  # La fonction se rappelle elle même avec une profondeur de moins, on récupère le score
                if new_score[1] < value:
                    value = new_score[1]
                    best_play_list = [col]
                elif new_score[1] == value:
                    best_play_list.append(col)
                # endif
            else:
                grid_copy = copy.deepcopy(grid)
                grid_copy = add_coin(col, 1, grid_copy)
                new_gamestate = (grid_copy, perk, 2)
                new_score = min_max(new_gamestate, required_coins, depth - 1, True)
                if new_score[
                    1] < value:  # Cas où le score trouvé est moins bon pour l'IA que celui que l'ordi avait enregistré
                    value = new_score[1]  # On met à jour le score avec la nouvelle pire valeur
                    best_play_list = [
                        col]  # On réinitialise la liste des meilleurs coups à la colonne du nouveau meilleur coup pour le joueur
                elif new_score[1] == value:  # Cas où le score trouvé est le même que celui que l'ordi avait enregistré
                    best_play_list.append(col)  # On ajoute à la liste des meilleurs coups la colonne trouvée
                # endif
            # endif
        # endfor
        column = rnd.choice(
            best_play_list)  # On choisit aléatoirement un des meilleurs coups (dont l'évaluation est égale)
        return (column, value)  # On renvoie le coup choisi et la valeur d'évaluation associée
    # endif


def do_game_turn(gameadvance: gametree_type, required_coin: int, play_AI: bool) -> int:
    """
    Fonction qui effectue un tour de jeu dans la console.
    :param gameadvance: Arbre de jeu sur lequel jouer un tour.
    :param required_coin: Le nombre de jetons à aligner pour gagner.
    :param play_AI: Vrai si on joue contre l'IA ; Faux si on joue à deux joueurs.
    :return: le nombre du joueur gagnant en cas de victoire ; 0 sinon
    """
    gamestate = copy.deepcopy(gameadvance[-1])  # On crée une copie de l'état du jeu courant à l'aide de deepcopy
    print("-" * 60)  # On affiche une ligne de séparation dans la console
    affiche(gamestate[0])  # On affiche la grille de jeu
    print("-" * 60)  # On affiche une ligne de séparation dans la console
    print("[Undo] : \'u\'\t[Perk] : \'p\'")  # On affiche les coups spéciaux et comment les utiliser
    col_to_play = -1  # On initialise la colonne de jeu à une valeur négative
    valid_play = False  # Variable de vérification de validité du coup donné
    board_width = len(gamestate[0][0])  # Récupération de la largeur de la grille de jeu
    win = 0  # Initialisation à 0 de la variable de victoire
    if play_AI:  # Cas où on joue contre l'IA
        AI_depth = 5  # On donne la profondeur 5 à l'IA
        if gamestate[2] == 1:  # Cas où c'est au joueur de jouer
            while col_to_play < 0 or col_to_play >= board_width or not valid_play:  # On vérifie que le coup est valide
                col_to_play = input(
                    "Entrer une colonne pour jouer entre 0 et {1} : ".format(gamestate[2],
                                                                             board_width - 1))  # On demande un coup au joueur
                if col_to_play == 'u':  # Cas où le coup donné est "undo"
                    undo_AI(gameadvance)  # On annule les derniers coups de l'IA et du joueur
                    col_to_play = 0  # On actualise la colonne de jeu à 0 pour sortir de la boucle
                    valid_play = True  # On actualise valid_play à Vrai pour sortir de la boucle

                elif col_to_play == 'p':  # Cas où le coup donné est l'atout
                    if not gamestate[1][0]:  # Cas où le joueur n'a pas déjà utilisé son atout
                        print("-" * 60)  # On affiche une ligne de séparation dans la console
                        print("Vous avez utilisé votre atout !")  # On informe le joueur qu'il a utilisé son atout
                        gamestate = use_perk(gamestate)  # On utilise l'atout
                        gamestate = (gamestate[0], gamestate[1], 2)  # On change le tour de jeu
                        gameadvance.append(gamestate)  # On ajoute le coup à l'arbre de jeu
                        col_to_play = 0  # On actualise la colonne de jeu à 0 pour sortir de la boucle
                        valid_play = True  # On actualise valid_play à Vrai pour sortir de la boucle
                    else:  # Cas où le joueur a déjà utilisé son atout
                        print(
                            "Vous avez déja utilisé votre atout !")  # On informe le joueur qu'il a déjà utilisé son atout
                        col_to_play = -1  # On réinitialise la colonne de jeu à une valeur négative
                    # endif

                else:  # Cas où le coup donné est une colonne
                    try:  # On vérifie que c'est bien un nombre
                        col_to_play = int(col_to_play)  # On essaie de convertir le coup en entier
                        if 0 <= col_to_play < board_width:  # Cas où le coup est une colonne valide de la grille
                            valid_play = check_valid_play(col_to_play, gamestate[
                                0])  # On regarde si on peut jouer dans cette colonne
                        # endif
                        if valid_play:  # Cas où le coup est possible
                            gamestate = (add_coin(col_to_play, 1, gamestate[0]), gamestate[1],
                                         2)  # On ajoute le jeton dans la colonne
                        # endif
                        win = check_victory(required_coin, gamestate[0])  # On vérifie les victoires éventuelles
                        gameadvance.append(gamestate)  # On ajoute le coup à l'arbre de jeu
                    except ValueError:  # Cas où le coup n'est pas un nombre
                        print(
                            "Veuillez rentrer une valeur valide.")  # On informe le joueur que son coup n'est pas valide
                        col_to_play = -1  # On réinitialise la colonne de jeu à une valeur négative
                    # endtry
                # endif
            # endwhile
        else:  # Cas où c'est à l'IA de jouer
            value = min_max(gamestate, required_coin, AI_depth, True)  # On récupère le coup de l'IA et son score
            col_AI_play = value[0]  # On assigne le coup de l'IA à col_AI_play
            if col_AI_play == "perk":  # Cas où le coup donné est l'atout
                gamestate = use_perk(gamestate)  # On utilise l'atout
                gamestate = (gamestate[0], gamestate[1], 1)  # On change le tour de jeu
                print("Atout utilisé par l'ordinateur !")  # On informe le joueur que l'IA a utilisé son atout
            else:  # Cas où le coup donné est une colonne
                gamestate = (
                    add_coin(col_AI_play, 2, gamestate[0]), gamestate[1], 1)  # On ajoute le jeton dans la colonne
            # endif
            win = check_victory(required_coin, gamestate[0])  # On vérifie les victoires éventuelles
            gameadvance.append(gamestate)  # On ajoute le coup à l'arbre de jeu

    else:  # Cas où on joue à deux joueurs
        while col_to_play < 0 or col_to_play >= board_width or not valid_play:  # On vérifie que le coup est valide
            col_to_play = input(
                "Joueur {0} : Entrer une colonne pour jouer entre 0 et {1} : ".format(gamestate[2],
                                                                                      board_width - 1))  # On demande un coup au joueur
            if col_to_play == 'u':  # Cas où le coup donné est "undo"
                undo(gameadvance)  # On annule le dernier coup joué
                col_to_play = 0  # On actualise la colonne de jeu à 0 pour sortir de la boucle
                valid_play = True  # On actualise valid_play à Vrai pour sortir de la boucle

            elif col_to_play == 'p':  # Cas où le coup donné est l'atout
                player = gamestate[2]  # On récupère le joueur dont c'est le tour
                if not gamestate[1][player - 1]:  # On vérifie qu'il peut encore utiliser son atout
                    print("-" * 60)  # On affiche une ligne de séparation dans la console
                    print("Joueur {0} : vous avez utilisé votre atout !".format(
                        player))  # On informe le joueur qu'il a utilisé son atout
                    gamestate = use_perk(gamestate)  # On utilise l'atout
                    if gamestate[2] == 1:  # Cas où c'est le tour du joueur 1
                        gamestate = (gamestate[0], gamestate[1], 2)  # On change le tour de jeu
                    else:  # Cas où c'est le tour du joueur 2
                        gamestate = (gamestate[0], gamestate[1], 1)  # On change le tour de jeu
                    # endif
                    gameadvance.append(gamestate)  # On ajoute le coup à l'arbre de jeu
                    col_to_play = 0  # On actualise la colonne de jeu à 0 pour sortir de la boucle
                    valid_play = True  # On actualise valid_play à Vrai pour sortir de la boucle
                else:
                    print("Joueur {0} : Vous avez déja utilisé votre atout !".format(
                        gamestate[2]))  # On informe le joueur qu'il a déjà utilisé son atout
                    col_to_play = -1  # On réinitialise la colonne de jeu à une valeur négative
                # endif

            else:  # Cas où le coup donné est une colonne
                try:  # On vérifie que c'est bien un nombre
                    col_to_play = int(col_to_play)  # On essaie de convertir le coup en entier
                    if 0 <= col_to_play < board_width:  # Cas où le coup est une colonne valide de la grille
                        valid_play = check_valid_play(col_to_play, gamestate[
                            0])  # On regarde si on peut jouer dans cette colonne
                    # endif
                    if valid_play:  # Cas où le coup est possible
                        if gamestate[2] == 1:  # Cas où c'est au tour du joueur 1
                            gamestate = (add_coin(col_to_play, gamestate[2], gamestate[0]), gamestate[1],
                                         2)  # On joue le coup et on change de tour
                        else:  # Cas où c'est au tour du joueur 2
                            gamestate = (add_coin(col_to_play, gamestate[2], gamestate[0]), gamestate[1],
                                         1)  # On joue le coup et on change de tour
                        # endif
                    # endif
                    win = check_victory(required_coin, gamestate[0])  # On vérifie les victoires éventuelles
                    gameadvance.append(gamestate)  # On ajoute le coup à l'arbre de jeu
                except ValueError:  # Cas où le coup n'est pas un nombre
                    print(
                        "Veuillez rentrer une valeur valide.")  # On informe le joueur que son coup n'est pas valide
                    col_to_play = -1  # On réinitialise la colonne de jeu à une valeur négative
                # endtry
            # endif
        # endwhile
    # endif
    return win  # On renvoie la variable indiquant une éventuelle victoire


if __name__ == '__main__':  # On éxécute ce code seulement si ce fichier est éxécuté en tant que code principal
    select_play_against_AI = ''  # On initialise le choix de jeu contre l'IA ou non
    width = -1  # On initialise la largueur à une valeur négative
    height = -1  # On initialise la hauteur à une valeur négative
    required_coin_nb = -1  # On initialise le nombre de jetons à aligner pour gagner à une valeur négative
    while select_play_against_AI != 'y' and select_play_against_AI != 'n':  # On veut récupérer 'y' ou 'n'
        select_play_against_AI = input(
            "Voulez vous jouer contre une AI ? [y/n] : ")  # On demande à l'utilisateur si il veut jouer contre l'IA ou non
    if select_play_against_AI == 'y':  # Cas où l'utilisateur veut jouer contre l'IA
        play_against_AI = True  # On choisir de joueur avec l'IA
    else:  # Cas où l'utilisateur veut jouer à deux joueurs
        play_against_AI = False  # On choisir de joueur sans l'IA
    while width < 0:  # On veut une largeur positive
        width = int(input("Entrer une largeur de grille supérieure à  0 : "))  # On demande la largeur de la grille
    while height < 0:  # On veut une hauteur positive
        height = int(input("Entrer une hauteur de grille supérieure à  0 : "))  # On demande la hauteur de la grille
    max_required_coin = min(width, height)  # On veut pouvoir gagner dans toutes les directions
    while required_coin_nb < 0 or required_coin_nb > max_required_coin:  # On vérifie que le nombre de jetons est positif et valide
        required_coin_nb = int(input(
            "Entrer le nombre de jetons à aligner pour gagner la partie, compris entre 0 et {0} : ".format(
                max_required_coin)))  # On demande le nombre de jetons à aligner pour gagner

    game_grid = init(width, height)  # On initialise la grille de jeu
    game_state = (game_grid, [False, False], 1)  # On initialise l'état du jeu
    game_advance = [game_state]  # On initialise l'arbre de jeu
    win = 0  # On initialise la victoire à 0
    while not check_full_grid(game_advance[-1][0], game_advance[-1][1]  # On joue tant que la grille n'est pas pleine
                                                   and win == 0):  # On joue tant qu'il n'y a pas de victoire
        win = do_game_turn(game_advance, required_coin_nb, play_against_AI)  # On effectue un tour de jeu
    print("-" * 60)  # On affiche une ligne de séparation dans la console
    affiche(game_advance[-1][0])  # On affiche la grille finale de la partie
    print("-" * 60)  # On affiche une ligne de séparation dans la console
    if win == 1:  # Cas où le joueur 1 gagne
        print("Le joueur 1 a gagné !")  # On informe du joueur victorieux
    elif win == 2:  # Cas où le joueur 2 gagne
        print("Le joueur 2 a gagné !")  # On informe du joueur victorieux
    else:  # Cas d'égalité
        print("Partie finie, égalité !")  # On informe de l'égalité
    print("-" * 60)  # On affiche une ligne de séparation dans la console
