import pygame
from player import Player
from shadow import Shadow
from sound import SoundManager


#Game Class
class Game:

    def __init__(self):
        # definir si le jeu a demarer ou non
        self.is_playing = False

        #Generator player
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        #groupe d'ombre
        self.all_shadow = pygame.sprite.Group()
        self.pressed = {}
        #gerer le son
        self.sound_manager = SoundManager()

    def start(self):
        self.is_playing = True
        self.spawn_monster()
        self.spawn_monster()

    def game_over(self):
        # remettrele jeu a 0
        self.all_shadow = pygame.sprite.Group()
        self.player. health = self.player.max_health
        self.is_playing = False
        self.sound_manager.play('game_over')

    def update(self, screen):
        # apply Player
        screen.blit(self.player.image, self.player.rect)

        # actualiser la bar du joueur
        self.player.update_health_bar(screen)

        # Catch Projectile
        for projectile in self.player.all_projectile:
            projectile.move()
        # Catch shadow du jeu
        for shadow in self.all_shadow:
            shadow.forward()
            shadow.update_health_bar(screen)
            shadow.update_animation()
        # aplly projectile
        self.player.all_projectile.draw(screen)

        # appliquer l'ensemble des images de mon groupe de monstre
        self.all_shadow.draw(screen)

        # verification move
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        shadow = Shadow(self)
        self.all_shadow.add(shadow)
