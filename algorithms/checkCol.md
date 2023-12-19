## Function: checkCol

### Parameters:
- `requiredCoins`: Integer (greater than 0)
- `boardWidth`: Integer (greater than 0)
- `boardHeight`: Integer (greater than 0)
- `grid`: 2D array of size [boardWidth, boardHeight]

### Pre-conditions:
- `requiredCoins` > 0
- `boardWidth` > 0
- `boardHeight` > 0

### Post-conditions:
- `winner` = 0 if no winning combination
- `winner` = 1 if the player wins
- `winner` = 2 if the computer wins

### Variables:
- `row`, `col`, `count`, `winner`: Integer

### Pseudocode:
1. Initialize `col` to 0
2. While `col` is less than or equal to `boardWidth` and `count` is less than `requiredCoins`:
   - Set `current` to `grid[0,col]`
   - Initialize `row` to 0 and `count` to 0

Fonction checkCol(entier : requiredCoins, entier : boardWidth, entier : boardHeight, tableau[boardWidth, boardHeight] grid) : entier
Pré-conditions : 
	requiredCoins > 0
	boardWidth > 0
	boardHeight > 0
Post-conditions :
	winner = 0 si pas de combinaison gagnante
	winner = 1 si le joueur gagne
	winner = 2 si l'ordinateur gagne
Variables :
entier row, col, count, winner;
Début :
	col <- 0
	TantQue ((col <= boardWidth)ET(count< requiredCoins)) faire :
		current <- grid[0,col]
		row <- 0
		count <- 0
		TantQue ((row <= boardHeight)ET(count < requiredCoins)ET(boardHeight-row >= requiredCoins-count)ET(grid[row,col]!=0)) faire :
			Si (current = grid[row,col]) alors :
				count <- count + 1
			Sinon:
				count <- 1
			FinSi
			current <- grid[row,col]
			row <- row + 1	
		FinTantQue
		col <- col + 1
	FinTantQue
	Si (count = requiredCoins) alors :
		winner <- current
	Sinon
		winner <- 0
	FinSi
	renvoyer winner
Fin
	
					
				
				
			 
