## Fonction checkCol

### Entrées :
- Entier : `boardWidth`,
- Entier : `boardHeight`,
- Entier : `requiredCoins`,
- Entier : `player`
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
	TantQue col < boardWidth ET count< requiredCoins faire :
		row <- 0
		count <- 0
		TantQue row < boardHeight ET count < requiredCoins ET boardHeight-row >= requiredCoins-count faire :
			Si grid[row,col] = player alors :
				count <- count + 1
			Sinon:
				count <- 0
			FinSi
			row <- row + 1	
		FinTantQue
		col <- col + 1
	FinTantQue
	Si count = requiredCoins alors :
		winner <- player
	Sinon
		winner <- 0
	FinSi
	renvoyer winner

#### Fin
	
					
				
				
			 
