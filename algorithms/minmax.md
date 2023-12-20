## Fonction checkVictory


### Entrées :
- Tableau[`boardWidth`, `boardHeight`] : `grid`
- Entier : `depth`
- Booléen : `maximazingPlayerTurn`

### Pré-conditions :
- `depth` > 0

### Sortie :
- Entier : `bestscore`

### Post-conditions :
- `bestscore` = 0 si il y a égalité
- `bestscore` = -1 si le joueur a une combinaisaison gagnante
- `bestscore` = 1 si l'ordinateur a une combinaisaison gagnante

### Variables :


#### Début

    // Maximizer win
    score = checkVictory(grid)
    Si (score == 1) Alors
        revnoyer score

    // Minimizer win
    Si (score == -1) Alors
        renvoyer score

    Si (checkFullGrid(grid)) Alors
        renvoyer 0

    Si (maximazingPlayerTurn) Alors   
        best = -1000
        Pour col allant de 0 à boardWidth - 1 faire
            Si (grid[boardHeight-1][col] == 0) Alors
                addCoin(boardWidth, boardHeight, col, 2, grid)
                best = max(best,minimax(grid, depth + 1, non isMaximizingPlayerTurn))))
                removeCoin(col, boardWidth, boardHeight, grid)
            FinSi
        renvoyer best
        Fin Pour
    Sinon
        best = 1000
        Pour col allant de 0 à boardWidth -1 faire
            Si grid[boardHeight-1][col] == 0 Alors
                addCoin(boardWidth, boardHeight, col, 1, grid)
                best = min(best,minimax(grid, depth + 1, non isMaximizingPlayerTurn))))     
                removeCoin(col, boardWidth, boardHeight, grid)
            FinSi
        renvoyer best
        Fin Pour
    FinSi

#### Fin
