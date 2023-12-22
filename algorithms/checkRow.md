## Fonction checkRow


### Entrées :
- Entier : `requiredCoins`,
- Entier : `boardWidth`,
- Entier : `boardHeight`,
- Tableau[`boardWidth`, `boardHeight`] : `grid`

### Pré-conditions :
- `boardWidth` > 0
- `boardHeight` > 0
- `requiredCoins` > 0

### Sortie :
- Entier : `winner`

### Post-conditions :
- `winner` = 0 si il n'y a pas de combinaison gagnante
- `winner` = 1 si le joueur gagne
- `winner` = 2 si l'ordinateur gagne

### Variables :
- Entier : `row`, `col`, `count`, `winner`

#### Début
	row <- 0
    count <- 0
	TantQue ((row <= boardHeight)ET(count< requiredCoins)) faire :
		current <- grid[row,0]
		col <- 0
		count <- 0
		TantQue ((col <= boardWidth)ET(count < requiredCoins)ET(boardWidth-col >= requiredCoins-count) faire :
			Si (current = grid[row,col]) alors :
				count <- count + 1
			Sinon:
				count <- 1
			FinSi
			current <- grid[row,col]
			col <- col + 1	
		FinTantQue
		row <- row + 1
	FinTantQue
	Si (count = requiredCoins) alors :
		winner <- current
	Sinon
		winner <- 0
	FinSi
	renvoyer winner

#### Fin
	
					
				
				
			 
