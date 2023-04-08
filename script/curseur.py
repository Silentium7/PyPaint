import pygame

# variable de la taille de la brosse/tampon
taille_Tampon = ()

# classe du curseur de la taille de la brosse/tampon
class Curseur:
    
    # initialise la classe
    def __init__(self, screen):
        
        # rectangle englobant le curseur et son rail
        self.x_Depart = screen.get_width() - 149
        self.y_Depart = 200
        
        # valeur du curseur
        self.value = 30
        self.value_Max = 80
        
        # couleur du curseur
        self.color = [150, 150, 150]
        
        # taille du curseur et son x (son y est aussi self.y_Depart)
        self.w = 10
        self.h = 40
        self.x = self.x_Depart + self.value
        
        # couleur du rail
        self.rail_Color = [230,230,230]
        
        # taille et coordonnés du rail
        self.rail_w = 100
        self.rail_h = 20
        self.rail_x = self.x_Depart
        self.rail_y = self.y_Depart + self.h/2 - self.rail_h/2
        
        
    # fonction visant à dessiner le curseur et la représentation de la taille
    def draw(self, screen):
        
        # actualise si le curseur à bougé
        self.move_Curseur()
        
        # ajuste la valeur du curseur si elle est trop grande ou trop petite
        if self.value >= 100:
            self.value = 100
        if self.value <= 1:
            self.value = 1
        
        # apporte la variable de la taille de la brosse/tampon
        global taille_Tampon
        # ajuste la taille de la brosse/tampon en fonction de celle de la brosse/tampon
        taille_Tampon = self.value/100 * self.value_Max
        if taille_Tampon <= 1:
            taille_Tampon = 1
            
        # actualise self.x car la valeur a changée
        self.x = self.x_Depart + self.value
        
        # dessine le rail
        pygame.draw.rect(screen, self.rail_Color, [self.rail_x, self.rail_y, self.rail_w, self.rail_h])
        # dessine le curseur
        pygame.draw.rect(screen, self.color, [self.x - self.w/2, self.y_Depart, self.w, self.h])
        # dessine la représentation de la taille de la brosse/tampon
        pygame.draw.circle(screen, [255, 0, 0], [self.x_Depart + self.rail_w/2, self.rail_y + 130], taille_Tampon)        
        
    
    # si la souris est cliqué, si il se trouve près ou sur le curseur 
    def move_Curseur(self):
        if pygame.mouse.get_pressed()[0] == 1 and pygame.mouse.get_pos()[0] > self.x - self.w  and pygame.mouse.get_pos()[0] < self.x + self.w  and pygame.mouse.get_pos()[1] > self.y_Depart and pygame.mouse.get_pos()[1] < self.y_Depart + self.h  :
            # change la valeur du curseur
            self.value = (pygame.mouse.get_pos()[0] - self.x_Depart) 

# fonction retournant quand elle est appelée la taille de la brosse/tampon. Elle sert à la fin de drawing.py pour faire un tracé de la taille choisie
def fonction_Taille_Tampon():
    return taille_Tampon

