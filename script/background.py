import pygame
from drawing import Drawing

class Background:
    
    # initialise l'instance background
    def __init__(self, screen):
        self.color = [255,255,255]
        
        # initialise le dessin
        self.dessin = Drawing()
        # dessine la feuille
        pygame.draw.rect(screen,self.color,[0,0,screen.get_width(),screen.get_height()])
    
    # dessine le dessin
    def draw(self,screen):
        
        # dessine le dessin
        self.dessin.draw(screen)