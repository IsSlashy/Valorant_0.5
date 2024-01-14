import pygame
import animation
from projectile import Projectile

#Player Class
class Player(animation.AnimateSprite):

    def __init__(self, game):
        super().__init__('player')
        self.game = game
        self.health = 150
        self.max_health = 150
        self.attack = 25
        self.velocity = 8
        self.all_projectile = pygame.sprite.Group()
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 660

    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount
        else:
            # si le joueur n'a plus de points de vie
            self.game.game_over()

    def update(self):
        self.animate()

    def update_health_bar(self, surface):
        # Draw Bar
        pygame.draw.rect(surface, (60, 60, 60), [self.rect.x + 100, self.rect.y + 80, self.max_health, 3])
        pygame.draw.rect(surface, (111, 210, 45), [self.rect.x + 100, self.rect.y + 80, self.health, 3])

    def launch_projectile(self):
        #new instance
        self.all_projectile.add(Projectile(self))
        self.start_animation()
        self.game.sound_manager.play('tir')

    def move_right(self):
        #si le joueur n'est pas en collision avec l'ombre
        if not self.game.check_collision(self, self.game.all_shadow):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity