import pygame

# importe la classe Colors
from colors import Colors

# impore la fonction qui dessine les couleurs
from write_Color import write_Color

# importe le curseur
from curseur import Curseur

# importe le stylo
from stylo import Stylo

# importe le seau
from seau import Seau

class Barre_Outils(pygame.sprite.Sprite):
    
    def __init__(self, screen):
        super().__init__()
        self.color_Background = [200,200,200]
        self.color_Séparation = [150,150,150]
        self.largeur = 200
        
        # charge le curseur
        self.curseur = Curseur(screen)
        
        # charge le stylo
        self.stylo = Stylo(screen)
        
        # charge le seau
        self.seau = Seau(screen)
    
    def draw(self,screen):
        # dessine la surface et sa limite de séparation
        pygame.draw.rect(screen,self.color_Background,[screen.get_width()-self.largeur,0,screen.get_width(),screen.get_height()])
        pygame.draw.line(screen, self.color_Séparation, [screen.get_width()-self.largeur,0], [screen.get_width()-self.largeur,screen.get_height()], 5)
        
        
        # x y de la pallette
        x_Palette = screen.get_width() - 174
        y_Palette = 27
        
        # dessine les couleurs
        black   = write_Color(0,0,0, x_Palette, y_Palette, screen,5, 'black')
        gray_1  = write_Color(85,85,85, x_Palette + 10 + 30, y_Palette, screen, 5, 'gray_1')
        gray_2  = write_Color(170,170,170, x_Palette + 20 + 60, y_Palette, screen, 5, 'gray_2')
        white   = write_Color(255,255,255, x_Palette + 30 + 90, y_Palette, screen, 5, 'white')
        
        brown   = write_Color(255/2,0,0, x_Palette, y_Palette + 10 + 30, screen, 5, 'brown')
        red     = write_Color(255,0,0, x_Palette + 10 + 30, y_Palette + 10 + 30, screen, 5, 'red')
        orange  = write_Color(255,85,0, x_Palette + 20 + 60, y_Palette + 10 + 30, screen, 5, 'orange')
        yellow  = write_Color(255,255,0, x_Palette + 30 + 90, y_Palette + 10 + 30, screen, 5, 'yellow')
        
        
        green_1 = write_Color(0,127,0, x_Palette, y_Palette + 20 + 60, screen, 5, 'green_1')
        cyan_1  = write_Color(0,127,127, x_Palette + 10 + 30, y_Palette + 20 + 60, screen, 5, 'cyan_1')
        green_2 = write_Color(0,255,0, x_Palette + 20 + 60, y_Palette + 20 + 60, screen, 5, 'green_2')
        cyan_2  = write_Color(0,255,255, x_Palette + 30 + 90, y_Palette + 20 + 60, screen, 5, 'cyan_2')
        
        violet  = write_Color(127,0,255, x_Palette, y_Palette + 30 + 90, screen, 5, 'violet')
        blue    = write_Color(0,0,255, x_Palette + 10 + 30, y_Palette + 30 + 90, screen, 5, 'blue')
        pink    = write_Color(255,127,127, x_Palette + 20 + 60, y_Palette + 30 + 90, screen, 5, 'pink')
        magenta = write_Color(255,0,255, x_Palette + 30 + 90, y_Palette + 30 + 90, screen, 5, 'magenta')
        
        # dessine le curseur
        self.curseur.draw(screen)
        
        # dessine l'outil stylo
        #self.stylo.draw(screen, x_Palette, y_Palette + 450, 60, 60)
        
        # dessine l'outil seau
        #self.seau.draw(screen, x_Palette + 60 + 30, y_Palette + 450, 60, 60)