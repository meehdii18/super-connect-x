# super-power-4

état du jeu : </br>
[0 0 0 0 0 0 0 </br>
 0 0 0 0 1 0 0</br>
 0 0 1 2 2 0 0</br>
 0 0 1 2 2 0 0</br>
 0 2 1 1 2 1 0</br>
 0 1 2 1 1 2 1]</br>


undoredo = [gamestate]</br>
gamegrid = [largeur][hauteur]</br>
gamestate = [grid,perk1,perk2,playerturn]</br>
perk1,perk2 = (bool,bool) (si déjà utilisé ou non par chaque joueur)</br>
activegamestate = type gamestate</br>
colorplayer1 = parmis (r , j, g…)</br>
colorplayer2 = … </br>
requiredcoins = entier strictement supérieur à 1 inférieur à max(largeur,hauteur)</br>
largeur = entier strictement supérieur à 3</br>
hauteur = entier strictement supérieur à 3</br>
aidepth = entier positif</br>
playerplayfirst = bool (true si l’humain commence)</br>
playerturn = bool (true si c’est au joueur humain de jouer)</br>



Fonctions : </br>
ajouterjeton(joueur, activegamestate,colonne,playerturn) : ajoute un jeton dans grid	</br>
checkvictory(activegamestate) : vérifie si il y a un gagnant à ce stade du jeu (vérifier match nul)</br>
	checkcolumn(activegamestate)</br>
	checkrow(activegamestate)</br>
	checkdiagup(activegamestate)</br>
	checkdiagdown(activegamestate)</br>
checkfullgrid(activegamestate) vérifie si la grille est pleine</br>
actionperk1(activegamestate) </br>
actionperk2(activegamestate)</br>
undo(undoredo,activegamestate) : fait un retour dans la liste gamestate</br>
redo(undoredo,activegamestate) : avance dans la liste game state      </br>
cleargame(activegamestate,perk1,perk2,undoredo) : remet tout à 0</br>


