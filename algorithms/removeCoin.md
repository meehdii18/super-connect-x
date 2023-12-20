## Fonction removeCoin

### Entrées :
- Entier : `col`,
- Entier : `boardWidth`,
- Entier : `boardHeight`,
- Tableau[`boardWidth`, `boardHeight`] : `grid`

### Pré-conditions :
- `boardWidth` > 0
- `boardHeight` > 0
- `requiredCoins` > 0
- `col` < `boardWidth`

### Sortie :
- Tableau[`boardWidth`, `boardHeight`] : `grid`

### Post-conditions :
- `grid` modifiée avec le jeton retiré si possible.

### Variables :
- Entier : `row`, `col`, `count`, `winner`

#### Début
    Pour row allant de board à boardHeight - 1 à 0 un pas de -1 faire
        Si (grid[row][col] != 0) Alors
            grid[row][col] = 0
            break
        FinSi
    FinPour
    renvoyer grid

#### Fin
	
					
				
				
			 
