## Fonction minMax


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

- Entier : `temp`,`score`,`best`,`bestCol`

#### Début

    score = checkVictory(grid)

    #Maximizer win
    Si score != 1 alors :
        renvoyer score

    #Minimizer win
    Si score = -1 alors :
        renvoyer score

    #Full grid
    Si checkFullGrid(grid) alors :
        renvoyer 0

    Si maximazingPlayerTurn alors :  
        best <- -1000
        bestCol <- -1
        Pour col allant de 0 à boardWidth - 1 faire :
            Si (grid[boardHeight-1,col] = 0) alors :
                addCoin(boardWidth, boardHeight, col, 2, grid)
                temp = minMax(grid, depth - 1, NON maximizingPlayerTurn)
                removeCoin(col, boardWidth, boardHeight, grid)
                Si (temp>best) alors :
                    best <- temp
                    best_col <- col
                FinSi
            FinSi
        renvoyer best, best_col
        FinPour
    Sinon
        best <- 1000
        bestCol <- -1
        Pour col allant de 0 à boardWidth -1 faire :
            Si grid[boardHeight-1,col] = 0 alors :
                addCoin(boardWidth, boardHeight, col, 1, grid)
                temp = minMax(grid, depth - 1, NON maximizingPlayerTurn)     
                removeCoin(col, boardWidth, boardHeight, grid)
                Si temp<best alors :
                    best <- temp
                    bestCol <- col
                FinSi
            FinSi
        renvoyer best, bestCol
        FinPour
    FinSi

#### Fin
