## Function: checkFullGrid

### Parameters:
- `boardWidth`: Integer (greater than 0)
- `boardHeight`: Integer (greater than 0)
- `grid`: 2D array of size [boardWidth, boardHeight]
- `perk1`: Boolean
- `perk2`: Boolean

### Pre-conditions:
- `boardHeight` > 0
- `boardWidth` > 0

### Post-conditions:
- Returns `True` if the grid is complete and all perks have been used
- Returns `False` if the grid is incomplete or not all perks have been used

### Variables:
- `col`: Integer
- `full`: Boolean

### Pseudocode:
1. Initialize `col` to 0 and `full` to `False`
2. If `perk1` and `perk2` are both `True`, set `full` to `True`
3. While `col` is less than or equal to `boardWidth` and `full` is `True`:
   - If `checkValidPlay(boardWidth, boardHeight, col, grid)` returns `True`, set `full` to `False`
   - Increment `col`
4. Return `full`


Fonction checkFullGrid(entier : boardWidth, entier : boardHeight, tableau[boardWidth, boardHeight] grid, booléen: perk1, booléen: perk2) : booléen
Pré-conditions : 
	boardHeight > 0
	boardWidth > 0
Post-conditions :
	Vrai si la grille est complète et que les atout ont tous été utilisés
	Faux si la grille est incomplète ou que les atouts n'ont pas tous été utilisés
Variables :
	entier : col
	booléen : full
Début :
	col <- 0
  	full <- Faux
  	Si ((perk1)ET(perk2)) alors :
   		full <- Vrai
    		TantQue ((col <= boardWidth)ET(full)) faire :
      			Si (checkValidPlay(boardWidth,boardHeight,col,grid)) alors :
        			full <- Faux
			FinSi
		FinTantQue
	FinSi
  	renvoyer full
Fin
