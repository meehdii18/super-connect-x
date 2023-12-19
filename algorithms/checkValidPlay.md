## Fonction checkValidPlay

### Entrées :
- Entier : `boardWidth`,
- Entier : `boardHeight`,
- Entier : `playColumn`,
- Tableau[`boardWidth`, `boardHeight`] : `grid`

### Pré-conditions :
- `boardWidth` > 0
- `boardHeight` > 0
- `playColumn` <= `boardWidth`

### Sortie :
- Booléen : `valide`

### Post-conditions:
- Vrai si le mouvement est valide
- Faux sinon

### Variables:
- Booléen : `valide`

#### Début

	Si (grid[boardHeight,playColumn] = 0) alors :
		valide <- Vrai
	Sinon
		valide <- Faux
	FinSi
	renvoyer valide

#### Fin
