def init(board_width, board_height):
    grid = [[0 for _ in range(board_width)] for _ in range(board_height)]
    return grid


def clear(grid):
    board_width = len(grid)
    board_height = len(grid[0])
    grid = init(board_width, board_height)
    return grid


def affiche(grid):
    num_col = [i for i in range(len(grid[0]))]
    board_height = len(grid)
    print("  |", num_col)
    print("--" + "|" + "-" * ((len(num_col)) * 3 + 1))
    for row in range(board_height):
        print(board_height - row - 1, "|", grid[board_height - row - 1])


def check_valid_play(play_column, grid):
    board_height = len(grid[0])
    if grid[board_height][play_column] == 0:
        return True
    else:
        return False


def check_full_grid(grid, perk1, perk2):
    board_width = len(grid)
    column = 0
    full = False
    if perk1 and perk2:
        full = True
        while column <= board_width and full:
            if check_valid_play(column, grid):
                full = False
            column += 1
    return full


def add_coin(play_column, player, grid):
    board_width = len(grid)
    board_height = len(grid[0])
    if (board_width < 0
            or board_height < 0
            or play_column > board_width):
        return grid
    row = 0
    actual_coin = grid[row][play_column]
    while actual_coin and row <= board_height:
        actual_coin = grid[row][play_column]
        if actual_coin:
            row += 1
    grid[row][play_column] = player
    return grid


def remove_coin(column, grid):
    board_width = len(grid)
    board_height = len(grid[0])
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


def check_row(required_coins, grid):
    board_width = len(grid)
    board_height = len(grid[0])
    row = 0
    count = 0
    current = 0
    while (row <= board_height
           and count < required_coins):
        current = grid[row][0]
        col = 0
        count = 0
        while (col <= board_width
               and count < required_coins
               and board_width - col >= required_coins - count):
            if current == grid[row][col]:
                count += 1
            else:
                count = 1
            current = grid[row][col]
            col += 1
        row += 1
    if count == required_coins:
        winner = current
    else:
        winner = 0
    return winner


def check_col(required_coins, grid):
    board_width = len(grid)
    board_height = len(grid[0])
    col = 0
    count = 0
    current = 0
    while (col <= board_width
           and count < required_coins):
        current = grid[0][col]
        row = 0
        count = 0
        while (row <= board_height
               and count < required_coins
               and board_height - row >= required_coins - count
               and grid[row][col]):
            if current == grid[row][col]:
                count += 1
            else:
                count = 1
            current = grid[row][col]
            row += 1
        col += 1
    if count == required_coins:
        winner = current
    else:
        winner = 0
    return winner


def check_down_diag(required_coins, grid):
    board_width = len(grid)
    board_height = len(grid[0])
    row_start = required_coins - 1
    col_start = 0
    count = 0
    current = 0
    while (col_start <= board_width - required_coins + 1
           and count < required_coins):
        row = row_start
        col = col_start
        current = grid[row][col]
        count = 0
        while (col <= board_width
               and row >= 0
               and count < required_coins
               and min(board_width - col, row) >= required_coins - count):
            if current == grid[row][col]:
                count += 1
            else:
                count = 1
            current = grid[row][col]
            row -= 1
            col += 1
        if row_start == board_height:
            col_start += 1
        else:
            row_start += 1
    if count == required_coins:
        winner = current
    else:
        winner = 0
    return winner


def check_up_diag(required_coins, grid):
    board_width = len(grid)
    board_height = len(grid[0])
    row_start = board_height - required_coins + 1
    col_start = 0
    count = 0
    current = 0
    while (col_start <= board_width - required_coins + 1
           and count < required_coins):
        row = row_start
        col = col_start
        current = grid[row][col]
        count = 0
        while (col <= board_width
               and row <= board_height
               and count < required_coins
               and min(board_width - col, board_height - row) >= required_coins - count):
            if current == grid[row][col]:
                count += 1
            else:
                count = 1
            current = grid[row][col]
            row += 1
            col += 1
        if row_start == 0:
            col_start += 1
        else:
            row_start -= 1
    if count == required_coins:
        winner = current
    else:
        winner = 0
    return winner


def check_victory(required_coins, grid):
    if required_coins > 0:
        if (check_col(required_coins, grid) == 1
                or check_row(required_coins, grid) == 1
                or check_up_diag(required_coins, grid) == 1
                or check_down_diag(required_coins, grid) == 1):
            score = -1
        elif (check_col(required_coins, grid) == 2
              or check_row(required_coins, grid) == 2
              or check_up_diag(required_coins, grid) == 2
              or check_down_diag(required_coins, grid) == 2):
            score = 1
        else:
            score = 0
        return score


game_grid = init(8, 5)
game_grid[3][2] = 1
affiche(game_grid)
