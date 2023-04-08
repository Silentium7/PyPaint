import pygame

class Colors:
    
    # initialise l'instance Colors
    def __init__(self, color, x, y, screen):
        self.image = pygame.draw.rect(screen, color, [x, y, 30, 30])
        self.rect = (0, 0, 30, 30)
        self.cliked = False
        
    
    # fonction renvoyant True si un objet est préssé
        # - si la sourie est appuyée
        # - si le curseur passe sur le bouton
    def color_Cliké(self, x, y):
        if pygame.mouse.get_pressed()[0] == 1 and pygame.mouse.get_pos()[0] > x and pygame.mouse.get_pos()[0] < x+30 and pygame.mouse.get_pos()[1] > y and pygame.mouse.get_pos()[1] < y + 30:
           
           return True
        else:
            return False