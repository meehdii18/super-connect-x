## Fonction checkFullGrid

### Entrées :
- Entier : `boardWidth`
- Entier : `boardHeight`
- Tableau[`boardWidth`, `boardHeight`] : `grid`
- Tableau[2] : `perk`

### Pré-conditions :
- `boardHeight` > 0
- `boardWidth` > 0

### Sortie :
- Booléen : `full`

### Post-conditions :
- Vrai si la grille est complète et que tous les joueurs ont utilisé leur atout
- Faux si la grille est incomplète ou que les atouts n'ont pas tous été utilisés

### Variables
- Entier : `col`
- Booléen : `full`

#### Début
	col <- 0
  	full <- Faux
  	Si perk[0] ET perk[1] alors :
        full <- Vrai
        TantQue col < boardWidth ET full faire :
            Si checkValidPlay(boardWidth, boardHeight, col, grid) alors :
                full <- Faux
			FinSi
            col <- col + 1
		FinTantQue
	FinSi
  	renvoyer full

#### Fin
- Algorithme de [`checkValidPlay`](./checkValidPlay.md)
