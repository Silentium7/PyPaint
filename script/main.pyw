# importe game
from game import Game
# importe la fonction de sauvegarde
from save_picture import save_picture
# import la fonction pour créer un dossier
from os import mkdir, listdir
# importe pygame
import pygame
pygame.init()

# si le dossier des sauvegardes n'existe pas, on le crée
if not("saves" in listdir()) : mkdir("saves")

# nomme la fenêtre
pygame.display.set_caption("PyPaint app")

# initialise la taille [1920, 1080]
taille = [500, 500]

# renitialise la fenetre quand elle est rendimentionnée
restart = True
while restart :
    
    #initialise la nouvelle taille
    screen = pygame.display.set_mode(taille,pygame.RESIZABLE)
    #initialise game
    game = Game(screen)

    # boucle
    running = True
    while running:
        
        # si la taille est changée, on renitialise la fenetre en recommancant la boucle principale
        if not (taille[0] == screen.get_width() and taille[1] == screen.get_height()):
            running = False
            # on récupère la nouvelle taille
            taille = screen.get_size()
        
        # update les objets
        game.update(screen)
        # update l'écran
        pygame.display.flip()
        
        # si on ferme la page le programme s'arrète
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                
                # stopper les deux boucles
                running = False
                restart = False
        
        
        
        # calcule si des touches sont préssés
        pressed = pygame.key.get_pressed()
        # si on fait ctrl + s, ca appelle la fonction enregistrer
        if pressed[pygame.K_s] and (pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]):
            save_picture(taille, screen)
    
# ferme pygame        
pygame.quit()