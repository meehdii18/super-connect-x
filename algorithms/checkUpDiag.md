## Fonction checkUpDiag

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
- Entier : `rowStart`, `colStart`, `row`, `col`, `count`, `winner`

#### Début
    rowStart <- boardHeight - requiredCoins + 1
    colStart <- 0
    count <- 0
    current <- 0
    TantQue colStart < boardWidth - requiredCoins + 1 ET count < requiredCoins faire :
        row <- rowStart
        col <- colStart
        current <- grid[row,col]
        count <- 0
        TantQue col <= boardWidth ET row <= boardHeight ET count < requiredCoins ET min(boardWidth-col,boardHeight-row) >= requiredCoins-count faire :
            Si current = grid[row,col] alors :
                count <- count + 1
            Sinon:
                count <- 1
            FinSi
            current <- grid[row,col]
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
        winner <- current
    Sinon
        winner <- 0
    FinSi
    renvoyer winner

#### Fin
	
					
				
				
			 
