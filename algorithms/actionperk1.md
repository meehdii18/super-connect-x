## Fonction perk1

### Entrées :
- Entier : `boardWidth`,
- Entier : `boardHeight`,
- Entier : `playColumn`,
- Entier : `player`,
- Tableau [3] : `gamestate`
- Tableau [`boardWidth`,`boardHeight`] : `grid`

### Pré-conditions :
- `playColumn` <= `boardWidth`,
- `player` = 1 si c'est au tour du joueur,
- `player` = 2 si c'est au tour de l'ordinateur.

### Sortie :
- Tableau [3] : `gamestate` 

### Post-conditions :
- `grid` modifiée avec la colonne supprimée en moins,
- `gamestate` prend en compte l'utilisation de l'atout par le joueur qui l'a utilisé.

### Variables :
- Entier : `actualCoin`,`row`

#### Début
	row <- 0
	TantQue row < boardHeight ET grid[row,playColumn] != 0 faire :
        grid[row,playColumn] <- 0    
        row <- row + 1
    FinTantQue
    gamestate[0] <- grid
    gamestate[1][player] <- Vrai 
	renvoyer gamestate

#### Fin
