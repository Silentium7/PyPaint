import pygame

stylo_Sélectionné = False


class Stylo :
    global seau_Sélectionné
    global stylo_Sélectionné
    
    def __init__(self, screen):
        self.color = [200, 200, 200]
        self.color_Encadré = [150, 150, 150]
        self.taille_Bordure = 5
        
    def draw(self, screen, x, y, w, h):
        print(seau_Sélectionné)
        
        stylo_Cliqué(x, y, w, h)
        if stylo_Sélectionné :
            
            self.color_Encadré = [100, 100, 100]
        else :
            self.color_Encadré = [150, 150, 150]
        pygame.draw.rect(screen, self.color_Encadré , [x, y, w, h])
        pygame.draw.rect(screen, self.color, [x + self.taille_Bordure, y + self.taille_Bordure, w - 2*self.taille_Bordure, h - 2*self.taille_Bordure])
        
def stylo_Cliqué(x, y, w, h):
    global stylo_Sélectionné
    #global seau_Sélectionné
    if pygame.mouse.get_pos()[0] > x and pygame.mouse.get_pos()[0] < x + w and pygame.mouse.get_pos()[1] > y and pygame.mouse.get_pos()[1] < y + h and pygame.mouse.get_pressed()[0] == 1 :
        seau_Sélectionné = False
        stylo_Sélectionné = True
