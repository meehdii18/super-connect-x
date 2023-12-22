def init(board_width, board_height):
    grid = [[0 for _ in range(board_width)] for _ in range(board_height)]
    return grid


def affiche(grid):
    num_col = [i for i in range(len(grid[0]))]
    board_height = len(grid)
    print("  |", num_col)
    print("--" + "|" + "-" * ((len(num_col)) * 3 + 1))
    for row in range(board_height):
        print(board_height - row - 1, "|", grid[board_height - row - 1])


def check_valid_play(play_column, grid):
    board_width = len(grid)
    board_height = len(grid[0])
    if not (board_width < 0 or board_height < 0 or play_column > board_width):
        if grid[board_height][play_column] == 0:
            return True
        else:
            return False


def add_coin(play_column, player, grid):
    board_width = len(grid)
    board_height = len(grid[0])
    if board_width < 0 or board_height < 0 or play_column > board_width:
        return grid
    row = 0
    actual_coin = grid[row][play_column]
    while actual_coin and row <= board_height:
        actual_coin = grid[row][play_column]
        if actual_coin:
            row += 1
    grid[row][play_column] = player
    return grid


game_grid = init(8, 5)
game_grid[3][2] = 1
affiche(game_grid)
