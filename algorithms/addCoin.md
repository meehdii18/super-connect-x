## Fonction addCoin
Fonction addCoin(entier : boardWidth, entier : boardHeight, entier: playCol,entier : player, tableau[boardWidth, boardHeight] grid) : tableau[boardWidth, BoardHeight]

### Entrées:
- `boardWidth`: Entier
- `boardHeight`: Entier
- `playCol`: Entier
- `player`: Entier
- `grid`: Tableau [boardWidth, boardHeight]

### Pré-conditions:
- `boardWidth` > 0
- `boardHeight` > 0
- `playCol` < `boardHeight` et est valide selon `checkValidPlay`
- `player` = 1 si c'est au tour du joueur
- `player` = 2 si c'est au tour de l'ordinateur

### Post-conditions:
- `grid` modifiée avec le coup du joueur.

### Variables:
- Entier : `actualCoin`,`row`

#### Début
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

#### Fin
