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
- Entier : `score`

### Post-conditions :
- `score` = 0 si il n'y a pas de combinaison gagnante
- `score` = -1 si le joueur gagne
- `score` = 1 si l'ordinateur gagne

### Variables :
- Entier : `score`

#### Début

    Si checkCol(requiredCoins, boardWidth, boardHeight, grid) == 1 OU checkRow(requiredCoins, boardWidth, boardHeight, grid) == 1 OU checkDiagUp(requiredCoins, boardWidth, boardHeight, grid) == 1 OU checkDiagDown(requiredCoins, boardWidth, boardHeight, grid) == 1 alors :
        score <- -1
    Sinon Si checkCol(requiredCoins, boardWidth, boardHeight, grid) == 2 OU checkRow(requiredCoins, boardWidth, boardHeight, grid) == 2 OU checkDiagUp(requiredCoins, boardWidth, boardHeight, grid) == 2 OU checkDiagDown(requiredCoins, boardWidth, boardHeight, grid) == 2 alors
        score <- 1
    Sinon
        score <- 0
    Fin Si
    renvoyer score

#### Fin
	
					
				
				
			 
