from PIL import Image
from random import randint
from os import listdir
import pygame

# fonction sauvegarder
def save_picture(taille, screen):
    
    
    
    
    # crée la nouvelle image
    image = Image.new('RGB', (taille[0]-202, taille[1]))
    
    # ajoute les pixels de l'image
    for y in range(0,image.height):
        for x in range(0,image.width):
            r = screen.get_at((x, y))[0]
            g = screen.get_at((x, y))[1]
            b = screen.get_at((x, y))[2]
            image.putpixel((x,y), (r, g, b))
    
    # enregistre
    chaine = "saves/save_" + str(len(listdir("saves"))+1) + ".png"
    image.save(chaine, "PNG")
    