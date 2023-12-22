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
- Entier : `score`,`victory`

#### Début

    victory = checkCol(requiredCoins, boardWidth, boardHeight, grid) OUEX checkRow(requiredCoins, boardWidth, boardHeight, grid)  OUEX checkDiagUp(requiredCoins, boardWidth, boardHeight, grid) OUEX checkDiagDown(requiredCoins, boardWidth, boardHeight, grid)
    Si victory == 1 alors :
        score <- -1
    Sinon Si victory == 2 alors
        score <- 1
    Sinon
        score <- 0
    Fin Si
    renvoyer score

#### Fin
	
					
				
				
			 
