# Super Connect 4 Game

## Game State
The game state is represented as follows:</br>


| 0 | 0 | 0 | 0 | 0 | 0 | 0 |
|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| 0 | 0 | 1 | 2 | 2 | 0 | 0 |
| 0 | 0 | 1 | 2 | 2 | 0 | 0 |
| 0 | 2 | 1 | 1 | 2 | 1 | 0 |



## Variables
- `undoredo`: List of game states
- `gamegrid`: 2D array representing the game grid
- `gamestate`: Current game state (grid, perk1, perk2, playerturn)
- `perk1`, `perk2`: Booleans indicating if each player has used their perk
- `activegamestate`: Current game state type
- `colorplayer1`, `colorplayer2`: Player colors
- `requiredcoins`: Integer greater than 1 and less than max(width, height)
- `width`: Integer greater than 3
- `height`: Integer greater than 3
- `aidepth`: Positive integer
- `playerplayfirst`: Boolean (true if the human player goes first)
- `playerturn`: Boolean (true if it's the human player's turn)

## Functions
- [`addCoin(player, activegamestate, column, playerturn)`](./algorithms/addCoin.md): Adds a token to the grid
- [`checkVictory(activegamestate)`](./algorithms/checkVictory.md): Checks if there's a winner at this stage of the game (also checks for a draw)
    - [`checkCol(activegamestate)`](./algorithms/checkCol.md)
    - [`checkRow(activegamestate)`](./algorithms/checkRow.md)
    - [`checkDiagUp(activegamestate)`](./algorithms/checkUpDiag.md)
    - [`checkDiagDown(activegamestate)`](./algorithms/checkDownDiag.md)
- [`checkfullgrid(activegamestate)`](./algorithms/checkFullGrid.md): Checks if the grid is full and all the perks have been used
- [`actionperk1(activegamestate)`](./algorithms/actionperk1.md): Do perk 1 action
- [`actionperk2(activegamestate)`](./algorithms/actionperk2.md): Do perk 2 action

  


