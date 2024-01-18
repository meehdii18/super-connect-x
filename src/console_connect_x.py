import copy
import random as rnd
import time


def init(board_width, board_height):
    grid = [[0 for _ in range(board_width)] for _ in range(board_height)]
    return grid


def clear(grid):
    board_width = len(grid[0])
    board_height = len(grid)
    grid = init(board_width, board_height)
    return grid


def affiche(grid):
    num_col = [i for i in range(len(grid[0]))]
    board_height = len(grid)
    print("  |", num_col)
    print("--" + "|" + "-" * ((len(num_col)) * 3 + 1))
    for row in range(board_height):
        print(row, "|", end=" ")
        for col in grid[row]:
            if col == 0:
                print("\u001b[37m", end="")
            elif col == 1:
                print("\x1B[38;2;255;0;0m", end="")
            elif col == 2:
                print("\x1B[38;2;255;255;0m", end="")
            print("██ ", end="")
        print("\u001b[37m")


def check_valid_play(play_column, grid):
    board_height = len(grid)
    if grid[0][play_column] == 0:
        return True
    else:
        return False


def check_full_grid(grid, perk):
    board_width = len(grid[0])
    column = 0
    full = False
    if perk[0] and perk[1]:
        full = True
        while column < board_width and full:
            if check_valid_play(column, grid):
                full = False
            column += 1
    return full


def undo(gameadvance):
    if len(gameadvance) >= 2:
        gameadvance.pop(-1)


def undo_AI(gameadvance):
    for _undo in range(2):
        undo(gameadvance)


def use_perk(gamestate_not_to_touch, play_column):
    gamestate = copy.deepcopy(gamestate_not_to_touch)
    grid = gamestate[0]
    board_height = len(grid)
    player = gamestate[2]
    row = 0
    while row < board_height:
        grid[row][play_column] = 0
        row += 1
    gamestate[1][player - 1] = True
    return gamestate


def add_coin(play_column, player, grid_not_to_touch):
    grid = copy.deepcopy(grid_not_to_touch)
    board_width = len(grid[0])
    board_height = len(grid)
    if (board_width < 0
            or board_height < 0
            or play_column > board_width):
        return grid
    row = board_height - 1
    actual_coin = grid[row][play_column]
    while actual_coin and row >= 0:
        actual_coin = grid[row][play_column]
        if actual_coin:
            row -= 1
    grid[row][play_column] = player
    return grid


def remove_coin(column, grid):
    board_width = len(grid[0])
    board_height = len(grid)
    if (board_width < 0
            or board_height < 0
            or column > board_width):
        return grid
    row = board_height - 1
    deleted = False
    while row >= 0 and not deleted:
        if grid[row][column] != 0:
            grid[row][column] = 0
            deleted = True
    return grid


def check_row(required_coins, grid, player):
    board_width = len(grid[0])
    board_height = len(grid)
    row = 0
    count = 0
    while (row < board_height
           and count < required_coins):
        col = 0
        count = 0
        while (col < board_width
               and count < required_coins
               and board_width - col >= required_coins - count):
            if grid[row][col] == player:
                count += 1
            else:
                count = 0
            col += 1
        row += 1
    if count == required_coins:
        winner = player
    else:
        winner = 0
    return winner


def check_col(required_coins, grid, player):
    board_width = len(grid[0])
    board_height = len(grid)
    col = 0
    count = 0
    while (col < board_width
           and count < required_coins):
        row = 0
        count = 0
        while (row < board_height
               and count < required_coins
               and board_height - row >= required_coins - count):
            if grid[row][col] == player:
                count += 1
            else:
                count = 0
            row += 1
        col += 1
    if count == required_coins:
        winner = player
    else:
        winner = 0
    return winner


def check_up_diag(required_coins, grid, player):
    board_width = len(grid[0])
    board_height = len(grid)
    row_start = required_coins - 1
    col_start = 0
    count = 0
    while (col_start <= board_width - required_coins
           and count < required_coins):
        row = row_start
        col = col_start
        count = 0
        while (col < board_width
               and row >= 0
               and count < required_coins):
            if grid[row][col] == player:
                count += 1
            else:
                count = 0
            row -= 1
            col += 1
        if row_start == board_height - 1:
            col_start += 1
        else:
            row_start += 1
    if count == required_coins:
        winner = player
    else:
        winner = 0
    return winner


def check_down_diag(required_coins, grid, player):
    board_width = len(grid[0])
    board_height = len(grid)
    row_start = board_height - required_coins
    col_start = 0
    count = 0
    while (col_start <= board_width - required_coins
           and count < required_coins):
        row = row_start
        col = col_start
        count = 0
        while (col < board_width
               and row < board_height
               and count < required_coins):
            if grid[row][col] == player:
                count += 1
            else:
                count = 0
            row += 1
            col += 1
        if row_start == 0:
            col_start += 1
        else:
            row_start -= 1
    if count == required_coins:
        winner = player
    else:
        winner = 0
    return winner


def check_victory(required_coins, grid):
    victory = 0
    for player in (1, 2):
        victory ^= (check_col(required_coins, grid, player)
                    ^ check_row(required_coins, grid, player)
                    ^ check_up_diag(required_coins, grid, player)
                    ^ check_down_diag(required_coins, grid, player))
    return victory


def evaluate_grid(grid, required_coins):
    score = 0
    weight = [[100, 5, 2], [-4, 0, 0]]
    for player in (1, 2):
        for distance_to_win in range(3):
            victory_indicator_row = check_row(required_coins - distance_to_win, grid, player)
            victory_indicator_col = check_col(required_coins - distance_to_win, grid, player)
            victory_indicator_diag_up = check_up_diag(required_coins - distance_to_win, grid, player)
            victory_indicator_diag_down = check_down_diag(required_coins - distance_to_win, grid, player)
            for victory_indicator in [victory_indicator_row, victory_indicator_col, victory_indicator_diag_up,
                                      victory_indicator_diag_down]:
                if victory_indicator == player:
                    score += weight[player - 1][distance_to_win]
    return score


def min_max(gamestate, required_coins, depth, maximizingPlayer):
    grid = gamestate[0]
    board_width = len(grid[0])
    perk = gamestate[1]
    full_board = check_full_grid(grid, perk)
    final_position_victory = check_victory(required_coins, grid)
    if depth == 0 or full_board or final_position_victory:
        if depth != 0:
            if final_position_victory == 2:
                return (None, 1000000000)
            elif final_position_victory == 1:
                return (None, -100000000)
            else:  # Game is over, no more valid moves
                return (None, 0)
        else:
            return (None, evaluate_grid(grid, required_coins))

    playable = [col for col in range(board_width) if check_valid_play(col, grid)]
    if maximizingPlayer:
        value = -10000000
        if not perk[1]:
            playable.append("perk")
        best_play_list = [rnd.choice(playable)]
        for col in playable:
            if col == "perk":
                for col_perk in range(board_width):
                    new_gamestate = copy.deepcopy(gamestate)
                    new_gamestate = use_perk(new_gamestate, col_perk)
                    new_gamestate[2] = 1
                    new_score = min_max(new_gamestate, required_coins, depth - 1, False)
                    if new_score[1] > value:
                        value = new_score[1]
                        best_play_list = [(col, col_perk)]
                    elif new_score[1] == value:
                        best_play_list.append((col, col_perk))
            else:
                grid_copy = copy.deepcopy(grid)
                grid_copy = add_coin(col, 2, grid_copy)
                new_gamestate = [grid_copy, perk, 1]
                new_score = min_max(new_gamestate, required_coins, depth - 1, False)
                if new_score[1] > value:
                    value = new_score[1]
                    best_play_list = [col]
                elif new_score[1] == value:
                    best_play_list.append(col)
            column = rnd.choice(best_play_list)
        return column, value

    else:  # Minimizing player
        value = 10000000
        if not perk[0]:
            playable.append("perk")
        best_play_list = [rnd.choice(playable)]
        for col in playable:
            if col == "perk":
                for col_perk in range(board_width):
                    new_gamestate = copy.deepcopy(gamestate)
                    new_gamestate = use_perk(new_gamestate, col_perk)
                    new_gamestate[2] = 2
                    new_score = min_max(new_gamestate, required_coins, depth - 1, True)
                    if new_score[1] < value:
                        value = new_score[1]
                        best_play_list = [col]
                    elif new_score[1] == value:
                        best_play_list.append(col)
            else :
                grid_copy = copy.deepcopy(grid)
                grid_copy = add_coin(col, 1, grid_copy)
                new_gamestate = [grid_copy, perk, 2]
                new_score = min_max(new_gamestate, required_coins, depth - 1, True)
                if new_score[1] < value:
                    value = new_score[1]
                    best_play_list = [col]
                elif new_score[1] == value:
                    best_play_list.append(col)
            column = rnd.choice(best_play_list)
        return column, value


def do_game_turn(gameadvance, required_coin, play_AI):
    gamestate = copy.deepcopy(gameadvance[-1])
    if __name__ == '__main__':
        print("-" * 60)
        affiche(gamestate[0])
        print("-" * 60)
        print("[Undo] : \'u\'\t[Perk] : \'p\'")
    col_to_play = -1
    valid_play = False
    board_width = len(gamestate[0][0])
    win = 0
    if play_AI:
        AI_depth = 5
        if gamestate[2] == 1:
            while col_to_play < 0 or col_to_play >= board_width or not valid_play:
                col_to_play = input(
                    "Entrer une colonne pour jouer entre 0 et {1} : ".format(gamestate[2],
                                                                             board_width - 1))
                if col_to_play == 'u':
                    undo_AI(gameadvance)
                    col_to_play = 0
                    valid_play = True
                elif col_to_play == 'p':
                    player = gamestate[2]
                    if not gamestate[1][player - 1]:
                        print("-" * 60)
                        col_to_play_perk = -1
                        while col_to_play_perk < 0 or col_to_play_perk >= board_width:
                            col_to_play_perk = int(input(
                                "Entrer une colonne pour votre atout entre 0 et {1} : ".format(gamestate[2],
                                                                                               board_width - 1)))
                        gamestate = use_perk(gamestate, col_to_play_perk)
                        if gamestate[2] == 1:
                            gamestate[2] = 2
                        else:
                            gamestate[2] = 1
                        gameadvance.append(gamestate)
                        col_to_play = 0
                        valid_play = True
                    else:
                        print("Joueur {0} : Vous avez déja utilisé votre atout !".format(gamestate[2]))
                        col_to_play = -1
                else:
                    try:
                        col_to_play = int(col_to_play)
                        if 0 <= col_to_play < board_width:
                            valid_play = check_valid_play(col_to_play, gamestate[0])
                        if valid_play:
                            gamestate[0] = add_coin(col_to_play, 1, gamestate[0])
                            gamestate[2] = 2
                        win = check_victory(required_coin, gamestate[0])
                        gameadvance.append(gamestate)
                    except ValueError:
                        print("Veuillez rentrer une valeur valide.")
                        col_to_play = -1
        else:
            value = min_max(gamestate, required_coin, AI_depth, True)
            col_AI_play = value[0]
            print(gamestate[1])
            if type(col_AI_play) == tuple:
                col_AI_play = col_AI_play[1]
                gamestate = use_perk(gamestate,col_AI_play)
            else:
                gamestate[0] = add_coin(col_AI_play, 2, gamestate[0])
            gamestate[2] = 1
            win = check_victory(required_coin, gamestate[0])
            gameadvance.append(gamestate)
    else:
        while col_to_play < 0 or col_to_play >= board_width or not valid_play:
            col_to_play = input(
                "Joueur {0} : Entrer une colonne pour jouer entre 0 et {1} : ".format(gamestate[2],
                                                                                      board_width - 1))
            if col_to_play == 'u':
                undo(gameadvance)
                col_to_play = 0
                valid_play = True
            elif col_to_play == 'p':
                player = gamestate[2]
                if not gamestate[1][player - 1]:
                    print("-" * 60)
                    col_to_play_perk = -1
                    while col_to_play_perk < 0 or col_to_play_perk >= board_width:
                        col_to_play_perk = int(input(
                            "Joueur {0} : Entrer une colonne pour votre atout entre 0 et {1} : ".format(gamestate[2],
                                                                                                        board_width - 1)))
                    gamestate = use_perk(gamestate, col_to_play_perk)
                    if gamestate[2] == 1:
                        gamestate[2] = 2
                    else:
                        gamestate[2] = 1
                    gameadvance.append(gamestate)
                    col_to_play = 0
                    valid_play = True
                else:
                    print("Joueur {0} : Vous avez déja utilisé votre atout !".format(gamestate[2]))
                    col_to_play = -1
            else:
                try:
                    col_to_play = int(col_to_play)
                    if 0 <= col_to_play < board_width:
                        valid_play = check_valid_play(col_to_play, gamestate[0])
                    if valid_play:
                        gamestate[0] = add_coin(col_to_play, gamestate[2], gamestate[0])
                        if gamestate[2] == 1:
                            gamestate[2] = 2
                        else:
                            gamestate[2] = 1
                    win = check_victory(required_coin, gamestate[0])
                    gameadvance.append(gamestate)
                except ValueError:
                    print("Veuillez rentrer une valeur valide.")
                    col_to_play = -1
    return win


if __name__ == '__main__':
    select_play_against_AI = ''
    width = -1
    height = -1
    required_coin_nb = -1
    while select_play_against_AI != 'y' and select_play_against_AI != 'n':
        select_play_against_AI = input("Voulez vous jouer contre une AI ? [y/n] : ")
    if select_play_against_AI == 'y':
        play_against_AI = True
    else:
        play_against_AI = False
    while width < 0:
        width = int(input("Entrer une largeur de grille supérieure à  0 : "))
    while height < 0:
        height = int(input("Entrer une hauteur de grille supérieure à  0 : "))
    max_required_coin = min(width, height)
    while required_coin_nb < 0 or required_coin_nb > max_required_coin:
        required_coin_nb = int(input(
            "Entrer le nombre de jetons à aligner pour gagner la partie, compris entre 0 et {0} : ".format(
                max_required_coin)))

    game_grid = init(width, height)
    game_state = [game_grid, [False, False], 1]
    game_advance = [game_state]
    win = 0
    while win == 0 and not check_full_grid(game_advance[-1][0],game_advance[-1][1]):
        win = do_game_turn(game_advance, required_coin_nb, play_against_AI)
    print("-" * 60)
    affiche(game_advance[-1][0])
    print("-" * 60)
    if win == 1:
        print("Le joueur 1 a gagné !")
    elif win == 2:
        print("Le joueur 2 a gagné !")
    else:
        print("Partie finie, égalité !")
    print("-" * 60)
