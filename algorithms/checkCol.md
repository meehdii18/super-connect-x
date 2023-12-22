## Fonction checkCol

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
	col <- 0
    count <- 0
    current <-0
	TantQue col < boardWidth ET count< requiredCoins faire :
		current <- grid[0,col]
		row <- 0
		count <- 0
		TantQue row < boardHeight ET count < requiredCoins ET boardHeight-row >= requiredCoins-count ET grid[row,col]!=0 faire :
			Si current = grid[row,col] alors :
				count <- count + 1
			Sinon:
				count <- 1
			FinSi
			current <- grid[row,col]
			row <- row + 1	
		FinTantQue
		col <- col + 1
	FinTantQue
	Si count = requiredCoins alors :
		winner <- current
	Sinon
		winner <- 0
	FinSi
	renvoyer winner

#### Fin
	
					
				
				
			 
