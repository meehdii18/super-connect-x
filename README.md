# super-power-4

état du jeu :
[0 0 0 0 0 0 0
 0 0 0 0 1 0 0
 0 0 1 2 2 0 0
 0 0 1 2 2 0 0
 0 2 1 1 2 1 0
 0 1 2 1 1 2 1]

arbre = [grid]
grid = [largeur][hauteur]
gamestate = [grid,atout1,atout2]
atout1,atout2 = bool

Fonctions : 
ajouterjeton(joueur,grid,colonne) : ajoute un jeton dans grid 
checkgamestate(grid) : vérifie si il y a un gagnant à ce stade du jeu 
atout1(grid) : fait l’action de l’atout 1
atout2(grid) : ‘’
undo(gamestate) : fait un retour dans la liste gamestate
redo(gamestate) : avance dans la liste game state                     dans le maximum / minimum de la liste
cleargame(arbre, grid,atout1,atout2) : remet tout à 0
