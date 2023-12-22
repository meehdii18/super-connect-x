## Fonction removeCoin

### Entrées :
- Entier : `col`,
- Entier : `boardWidth`,
- Entier : `boardHeight`,
- Tableau[`boardWidth`, `boardHeight`] : `grid`

### Pré-conditions :
- `boardWidth` > 0
- `boardHeight` > 0
- `col` <= `boardWidth`

### Sortie :
- Tableau[`boardWidth`, `boardHeight`] : `grid`

### Post-conditions :
- `grid` modifiée avec le jeton retiré si possible.

### Variables :
- Entier : `row`, `col`
- Booléen : `deleted`

#### Début
    row <- boardHeight - 1
    deleted <- Faux
    TantQue row >= 0 ET NON deleted faire :
        Si (grid[row,col] != 0) alors :
            grid[row,col] <- 0
            deleted <- Vrai
        FinSi
    FinTantQue
    renvoyer grid

#### Fin
	
					
				
				
			 
