import pygame
# importe le fond
from background import Background
# importe la barre d'outils
from barre_Outils import Barre_Outils


class Game:
    
    # initialise l'instance Game
    def __init__(self, screen):
        self.bk = Background(screen)
        self.barre_Outils = Barre_Outils(screen)
    
    # dessine tout à chaque update
    def update(self,screen):
        # update la feuille
        self.bk.draw(screen)
        # update la barre d'outils
        self.barre_Outils.draw(screen)