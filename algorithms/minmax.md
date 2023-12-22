## Fonction MinMax


### Entrées :
- Tableau[`boardWidth`, `boardHeight`] : `grid`
- Entier : `depth`
- Booléen : `maximazingPlayerTurn`

### Pré-conditions :
- `depth` > 0

### Sortie :
- Entier : `best`
- Entier : `bestCol`

### Post-conditions :
- `bestscore` = 0 si il y a égalité
- `bestscore` = -1 si le joueur a une combinaisaison gagnante
- `bestscore` = 1 si l'ordinateur a une combinaisaison gagnante

### Variables :

- Entier : `temp`
- Entier : `score`

#### Début

    score = checkVictory(grid)

    #Maximizer win
    Si (score == 1) Alors
        revnoyer score

    #Minimizer win
    Si (score == -1) Alors
        renvoyer score

    #Full grid
    Si (checkFullGrid(grid)) Alors
        renvoyer 0

    Si (maximazingPlayerTurn) Alors   
        best <- -1000
        bestCol <- -1
        Pour col allant de 0 à boardWidth - 1 faire
            Si (grid[boardHeight-1][col] == 0) Alors
                addCoin(boardWidth, boardHeight, col, 2, grid)
                temp = minimax(grid, depth + 1, non isMaximizingPlayerTurn)))
                removeCoin(col, boardWidth, boardHeight, grid)
                Si (temp>best) alors
                    best <- temp
                    best_col <- col
            FinSi
        renvoyer best, best_col
        Fin Pour
    Sinon
        best <- 1000
        Pour col allant de 0 à boardWidth -1 faire
            Si grid[boardHeight-1][col] == 0 Alors
                addCoin(boardWidth, boardHeight, col, 1, grid)
                temp = minimax(grid, depth + 1, non isMaximizingPlayerTurn)))     
                removeCoin(col, boardWidth, boardHeight, grid)
                Si temp<best alors
                    best <- temp
                    bestCol <- col
            FinSi
        renvoyer best, bestCol
        Fin Pour
    FinSi

#### Fin
