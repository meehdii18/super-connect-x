## Fonction checkFullGrid

### Entrées :
- Entier : `boardWidth`
- Entier : `boardHeight`
- Tableau[`boardWidth`, `boardHeight`] : `grid`
- Booléen : `perk1`
- Booléen : `perk2`

### Pré-conditions :
- `boardHeight` > 0
- `boardWidth` > 0

### Sortie :


### Post-conditions :
- Vrai si la grille est complète et que les atout ont tous été utilisés
- Faux si la grille est incomplète ou que les atouts n'ont pas tous été utilisés

### Variables
- Entier : `col`
- Booléen : `full`

#### Début
	col <- 0
  	full <- Faux
  	Si ((perk1)ET(perk2)) alors :
   		full <- Vrai
    		TantQue ((col <= boardWidth)ET(full)) faire :
      			Si (checkValidPlay(boardWidth, boardHeight, col, grid)) alors :
        			full <- Faux
			FinSi
		FinTantQue
	FinSi
  	renvoyer full

#### Fin
