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


#### Début

    Si (checkCol(requiredCoins, boardWidth, boardHeight, grid) == 1 ou checkRow(requiredCoins, boardWidth, boardHeight, grid) == 1 ou checkDiagUp(requiredCoins, boardWidth, boardHeight, grid) == 1 ou checkDiagDown(requiredCoins, boardWidth, boardHeight, grid) == 1) Alors
        score = -1
    Sinon Si (checkCol(requiredCoins, boardWidth, boardHeight, grid) == 2 ou checkRow(requiredCoins, boardWidth, boardHeight, grid) == 2 ou checkDiagUp(requiredCoins, boardWidth, boardHeight, grid) == 2 ou checkDiagDown(requiredCoins, boardWidth, boardHeight, grid) == 2) Alors
        score = 1
    Sinon
        score = 0
    Fin Si
    renvoyer score

#### Fin
	
					
				
				
			 
