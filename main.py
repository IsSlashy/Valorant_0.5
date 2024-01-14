import pygame
import math
from game import Game
pygame.init()

# generer la fenetre de notre jeu
pygame.display.set_caption("Valorant 0.5")
screen = pygame.display.set_mode((1920, 1080))

# Bk Ground du jeu
background = pygame.image.load('Valorant_Assets/bg.png')

#Bannier
banner = pygame.image.load('Valorant_Assets/banner.png')
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 3)
#importation du button
play_button = pygame.image.load("Valorant_Assets/button.png")
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width()/3.33)
play_button_rect.y = math.ceil(screen.get_height()/2)
#Load Game
game = Game()

running = True

# boucle True
while running:

    # Apply Bkgd
    screen.blit(background, (0, -20))

    #verifier si le jeu a commencer
    if game.is_playing:
        #declancher les instruction
        game.update(screen)
    #verifier si le jeu na pas commencer
    else:
        #ajouter l'écran de bienvenue
        screen.blit(banner, (650, 50))
        screen.blit(play_button, (770, 500))

    # mise a jour de l'ecran
    pygame.display.flip()

    # si le joueur cette fenetre
    for event in pygame.event.get():
        # verification close window
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Closing Game")
        #Move detect
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            #detect Key Projectile
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # verification si la souris est en collision
            if play_button_rect.collidepoint(event.pos):
                # mettre le jeu en mode launch
                game.start()
                # jouer le son
                game.sound_manager.play('click')

