import pygame
# importe la classe Colors servant à savoir si une couleur est préssée
from colors import Colors

# variable contenant quelle couleur est sélectionnée
objet_Cliqué = 'black'

# fonction dessinant les couleurs dans la barre d'outils
def write_Color(r,v,b, x, y, screen,taille_Bordure, nom):
    global objet_Cliqué
    
    # crée une instance "Nom" de "Colors" en donnant la couleur et sa position pour savoir si elle est cliquée
    Nom = Colors([r,v,b], x,y, screen)
    
    # variable vraie ou fause si la couleur est sélectionnée ou non
    write_Cliké = Nom.color_Cliké(x, y)
    
    # si cette couleur est cliqué
    if write_Cliké :
        # donne à objet_Cliqué la nouvelle couleur
        objet_Cliqué = nom
        # le dessine
        pygame.draw.rect(screen, [100, 100, 100], [x, y, 30, 30])
        pygame.draw.rect(screen, [r, v, b], [x + taille_Bordure, y + taille_Bordure, 30 - 2*taille_Bordure, 30- 2*taille_Bordure])
    
    
    # pour une couleur si elle n'est pas actuellement sélectionné,
    if nom != objet_Cliqué :
        # dessine la couleur normalement
        pygame.draw.rect(screen, [150, 150, 150], [x, y, 30, 30])
        pygame.draw.rect(screen, [r, v, b], [x + taille_Bordure, y + taille_Bordure, 30 - 2*taille_Bordure, 30- 2*taille_Bordure])
    
    # si cette couleur est sélectionnée, 
    elif nom == objet_Cliqué:
        # dessine la couleur en l'encadrant en foncé
        pygame.draw.rect(screen, [100, 100, 100], [x, y, 30, 30])
        pygame.draw.rect(screen, [r, v, b], [x + taille_Bordure, y + taille_Bordure, 30 - 2*taille_Bordure, 30- 2*taille_Bordure])
    

# fonction retournant quelle couleur est actuellement sélectionnée
def fonction_Objet_Selectionné():
    return objet_Cliqué
    
    