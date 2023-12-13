# super-power-4

état du jeu :<br />
[0 0 0 0 0 0 0<br />
 0 0 0 0 1 0 0<br />
 0 0 1 2 2 0 0<br />
 0 0 1 2 2 0 0<br />
 0 2 1 1 2 1 0<br />
 0 1 2 1 1 2 1]<br />

arbre = [grid]<br />
grid = [largeur][hauteur]<br />
gamestate = [grid,atout1,atout2]<br />
atout1,atout2 = bool<br />

Fonctions : <br />
ajouterjeton(joueur,grid,colonne) : ajoute un jeton dans grid <br />
checkgamestate(grid) : vérifie si il y a un gagnant à ce stade du jeu <br />
atout1(grid) : fait l’action de l’atout 1<br />
atout2(grid) : ‘’<br />
undo(gamestate) : fait un retour dans la liste gamestate<br />
redo(gamestate) : avance dans la liste game state                     dans le maximum / minimum de la liste<br />
cleargame(arbre, grid,atout1,atout2) : remet tout à 0<br />
