# Structures de données

## perk :
#### List[bool, bool]:
- perk[0] : `Vrai` si le joueur humain a utilisé l'atout, `Faux`sinon,
- perk[1] : `Faux` si l'ordinateur a utilisé l'atout, `Faux`sinon.

## grid :
#### List[`boardWidth`,`boardHeight`]

## gamestate :
#### Tuple[3] : 
- gamestate[0] : `grid`,
- gamestate[1] : `perk`,
- gamestate[2] : `playerTurn` (1 si au tour du joueur humain, 2 si au tour de l'ordinateur).

## gameadvance :
#### Liste : contient les gamestate correspondant aux coups joués.