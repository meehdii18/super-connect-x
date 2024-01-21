## Fonction checkVictory


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
- Entier : `victory`

### Post-conditions :
- `victory` = 0 si il n'y a pas de combinaison gagnante
- `victory` = 1 si le joueur gagne
- `victory` = 2 si l'ordinateur gagne

### Variables :
- Entier : `player`,`victory`

#### Début

    victory <- 0
    Pour player allant de 1 à 2 faire :
        victory <- victory OU checkRow(requiredCoins, grid, player)
        victory <- victory OU checkCol(requiredCoins, grid, player)
        victory <- victory OU checkUpDiag(requiredCoins, grid, player)
        victory <- victory OU checkDownDiag(requiredCoins, grid, player)
    Fin Pour
    renvoyer victory

#### Fin
	
					
				
				
			 
