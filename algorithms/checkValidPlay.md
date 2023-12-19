## Function: checkValidPlay

### Parameters:
- `boardWidth`: Integer (greater than 0)
- `boardHeight`: Integer (greater than 0)
- `playColumn`: Integer
- `grid`: 2D array of size [boardWidth, boardHeight]

### Pre-conditions:
- `boardWidth` > 0
- `boardHeight` > 0
- `playColumn` <= `boardWidth`

### Post-conditions:
- Returns `True` if the move is valid
- Returns `False` if the move is not valid

### Variables:
- `valid`: Boolean

### Pseudocode:
1. If `grid[boardHeight,playColumn]` equals 0, set `valid` to `True`
   - Otherwise, set `valid` to `False`
2. Return `valid`


Fonction checkValidPlay(entier : boardWidth, entier : boardHeight, entier : playColumn, tableau[boardWidth, boardHeight] grid) : booléen
Pré-conditions : 
	boardWidth > 0
	boardHeight > 0
	playColumn <= boardWidth
Post-conditions :
	valide = True si le coup est valide
	valide = False si le coup n'est pas valide
Variables :
	booléen : valide
Début :
	Si (grid[boardHeight,playColumn] = 0) alors :
		valide <- Vrai
	Sinon
		valide <- Faux
	FinSi
	renvoyer valide
Fin
