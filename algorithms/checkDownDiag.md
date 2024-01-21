## Fonction checkDownDiag

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
- Entier : `rowStart`, `colStart`, `row`, `col`, `count`, `winner`

#### Début
	rowStart <- board_height - requiredCoins
  	colStart <- 0
    count <- 0
	TantQue colStart <= boardWidth - requiredCoins ET count < requiredCoins faire :
        row <- rowStart
        col <- colStart
		count <- 0
		TantQue col < boardWidth ET row < boardWidth ET count < requiredCoins faire :
			Si grid[row,col] = player alors :
				count <- count + 1
			Sinon:
				count <- 0
			FinSi
      		row <- row + 1
			col <- col + 1
		FinTantQue
        Si rowStart = 0 alors :
            colStart <- colStart + 1
        Sinon
            rowStart <- rowStart - 1
        FinSi
	FinTantQue
	Si count = requiredCoins alors :
		winner <- player
	Sinon
		winner <- 0
	FinSi
	renvoyer winner

#### Fin
	
					
				
				
			 
