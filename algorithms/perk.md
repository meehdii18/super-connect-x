## Fonction perk1

### Entrées :
- Entier : `boardWidth`,
- Entier : `boardHeight`,
- Entier : `player`,
- Tableau [3] : `gamestate`
- Tableau [`boardWidth`,`boardHeight`] : `grid`

### Pré-conditions :
- `player` = 1 si c'est au tour du joueur,
- `player` = 2 si c'est au tour de l'ordinateur.

### Sortie :
- Tableau [3] : `gamestate` 

### Post-conditions :
- `grid` modifiée avec la colonne supprimée en moins,
- `gamestate` prend en compte l'utilisation de l'atout par le joueur qui l'a utilisé.

### Variables :
- Entier : `col`,`row`,`currentRow`

#### Début
	currentRow <- boardHeight - 2
    row <- currentRow - 1
	TantQue row != 0 faire :
        grid[currentRow] <- grid[row]
        currentRow <- currentRow -1
        row <- row - 1
    FinTantQue
    Pour col allant de 0 à boardWidth - 1 faire :
        grid[0,col] <- 0
    FinPour
    gamestate[0] <- grid
    gamestate[1][player - 1] <- Vrai 
	renvoyer gamestate

#### Fin
