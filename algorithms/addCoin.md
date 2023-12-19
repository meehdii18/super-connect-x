## Fonction addCoin

### Entrées :
- Entier : `boardWidth`,
- Entier : `boardHeight`,
- Entier : `playCol`,
- Entier : `player`,
- Tableau [`boardWidth`, `boardHeight`] : `grid`

### Pré-conditions :
- `boardWidth` > 0,
- `boardHeight` > 0,
- `playCol` < `boardHeight` et est valide selon [`checkValidPlay`](./algorithms/checkValidPlay.md),
- `player` = 1 si c'est au tour du joueur,
- `player` = 2 si c'est au tour de l'ordinateur.

### Sortie :
- Tableau [boardWidth, boardHeight] : `grid` 

### Post-conditions :
- `grid` modifiée avec le coup du joueur.

### Variables :
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
