## Function: addCoin

### Parameters:
- `boardWidth`: Integer (greater than 0)
- `boardHeight`: Integer (greater than 0)
- `playColumn`: Integer
- `player`: Integer (1 if it's the human player, 2 if it's the computer)
- `grid`: 2D array of size [boardWidth, boardHeight]

### Pre-conditions:
- `boardHeight` > 0
- `boardWidth` > 0
- `player` = 1 if it's the human player
- `player` = 2 if it's the computer

`playColumn` is valid and has been verified with `checkValidPlay` beforehand.

### Post-conditions:
- `grid`: Modified with the player's move

### Variables:
- `actualCoin`: Integer
- `row`: Integer

### Pseudocode:
1. Initialize `row` to 0
2. Set `actualCoin` to `grid[row,playColumn]`
3. While `actualCoin` is not 0 and `row` is less than or equal to `boardHeight`:
   - Set `actualCoin` to `grid[row,playColumn]`
   - If `actualCoin` is not 0, increment `row`
4. Set `grid[row,playColumn]` to `player`
5. Return `grid`


Fonction addCoin(entier : boardWidth, entier : boardHeight, entier: playColumn,entier : player, tableau[boardWidth, boardHeight] grid) : tableau[boardWidth, BoardHeight]
Pré-conditions : 
	boardHeight > 0
	boeardWidht > 0
	player = 1 si c'est l'humain
	player = 2 si c'est l'ordinateur
Post-conditions :
	grid : modifiée avec le coup du joueur effectué
	playColumn valide vérifiée avec checkValidPlay auparavant
Variables :
	entier : actualCoin, row
Début :
	row <- 0
	actualCoin <- grid[row,playColumn]
	TantQue ((actualCoin !=0)ET(row <= boardHeight)) faire :
		actualCoin <- grid[row,playColumn]
		Si (actualCoin) alors :
			row <- row + 1
		FinSi
	FinTantQue
	grid[row,playColumn] <- player
	renvoyer grid
Fin
