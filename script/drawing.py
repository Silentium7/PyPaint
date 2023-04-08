import pygame

# importe la fonction permettant de savoir quel est la couleur sélectionnée
from write_Color import fonction_Objet_Selectionné

# importe la fonction servant à connaitre la taille de la brosse/tampon choisit
from curseur import fonction_Taille_Tampon



# classe faisant le dessin
class Drawing:
    
    # initialise le dessin
    def __init__(self):
        self.color = [255, 0,0]
    
    # met self.color à la bonne couleur
    def update_Color(self):
        if fonction_Objet_Selectionné() == 'black' :
            self.color = [0,0,0]
        elif fonction_Objet_Selectionné() == 'gray_1' :
            self.color = [85,85,85]
        elif fonction_Objet_Selectionné() == 'gray_2' :
            self.color = [170,170,170]
        elif fonction_Objet_Selectionné() == 'white' :
            self.color = [255,255,255]
        
        elif fonction_Objet_Selectionné() == 'brown' :
            self.color = [127,0,0,]
        elif fonction_Objet_Selectionné() == 'red' :
            self.color = [255,0,0,]
        elif fonction_Objet_Selectionné() == 'orange' :
            self.color = [255,85,0]
        elif fonction_Objet_Selectionné() == 'yellow' :
            self.color = [255,255,0]
        
        elif fonction_Objet_Selectionné() == 'green_1' :
            self.color = [0,127,0]
        elif fonction_Objet_Selectionné() == 'cyan_1' :
            self.color = [0,127,127]
        elif fonction_Objet_Selectionné() == 'green_2' :
            self.color = [0,255,0]
        elif fonction_Objet_Selectionné() == 'cyan_2' :
            self.color = [0,255,255]
        
        elif fonction_Objet_Selectionné() == 'violet' :
            self.color = [127,0,255]
        elif fonction_Objet_Selectionné() == 'blue' :
            self.color = [0,0,255]
        elif fonction_Objet_Selectionné() == 'pink' :
            self.color = [255,127,127]
        elif fonction_Objet_Selectionné() == 'magenta' :
            self.color = [255,0,255]
        
    
    # si on clique, dessine un rond de la bonne taille
    def draw(self, screen):
        self.update_Color()
        if pygame.mouse.get_pressed()[0] == 1 and pygame.mouse.get_pos()[0] < 1719 :
            pygame.draw.circle(screen, self.color, [pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]], fonction_Taille_Tampon())
            
    
    