## Function: checkDownDiag

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
   - While `row` is less than or equal to `boardHeight` and `col` is less than or equal to `boardWidth` and `count` is less than `requiredCoins` and `boardHeight-row` is greater than or equal to `requiredCoins-count` and `grid[row,col]` is not 0:
     - If `current` equals `grid[row,col]`, increment `count`
     - Otherwise, set `count` to 1


Fonction checkDownDiag(entier : requiredCoins, entier : boardWidth, entier : boardHeight, tableau[boardWidth, boardHeight] grid) : entier
Pré-conditions : 
	requiredCoins > 0
	boardWidth > 0
	boardHeight > 0
Post-conditions :
	winner = 0 si pas de combinaison gagnante
	winner = 1 si le joueur gagne
	winner = 2 si l'ordinateur gagne
Variables :
entier rowStart, colStart, row, col, count, winner;
Début :
	rowStart <- requiredCoins - 1
  	colStart <- 0
	TantQue ((colStart < boardWidth - requiredCoins + 1)ET(count < requiredCoins)) faire :
        row <- rowStart
        col <- colStart
		current <- grid[row,col]
		count <- 0
		TantQue ((col <= boardWidth)ET(row >= 0)ET(count < requiredCoins)ET(min(boardWidth-col, row) >= requiredCoins-count) faire :
			Si (current = grid[row,col]) alors :
				count <- count + 1
			Sinon:
				count <- 1
			FinSi
			current <- grid[row,col]
      			row <- row - 1
			col <- col + 1
		FinTantQue
        Si (rowStart = boardHeight) alors :
            colStart <- colStart + 1
        Sinon
            rowStart <- rowStart + 1
        FinSi
	FinTantQue
	Si (count = requiredCoins) alors :
		winner <- current
	Sinon
		winner <- 0
	FinSi
	renvoyer winner
Fin
	
					
				
				
			 
