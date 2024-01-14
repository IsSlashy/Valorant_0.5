import pygame
import random
import animation
#Shadow class

class Shadow(animation.AnimateSprite):

    def __init__(self, game):
        super().__init__("Shadow")
        self.game = game
        self.health=100
        self.max_health=100
        self.attack=0.3
        self.rect = self.image.get_rect()
        self.rect.x = 1670 + random.randint(0,300)
        self.rect.y = 700
        self.velocity = random.randint (1,4)

    def damage(self, amount):
        #infliger les degats
        self.health -= amount


        #verifier le nombre de point de vie Negatif
        if self.health <= 0:
            # Réaparition
            self.rect.x =1670 + random.randint(0,300)
            self.velocity = random.randint (1,4)
            self.health =self.max_health

    def update_animation(self):
        self.animate()
    def update_health_bar(self, surface):
        #Draw Bar
        pygame.draw.rect(surface, (60, 60, 60), [self.rect.x + 120, self.rect.y + 50, self.max_health, 5])
        pygame.draw.rect(surface, (111, 210, 45),[self.rect.x + 120, self.rect.y + 50, self.health, 5])

    def forward(self):
        #deplacement uniquement sens collision
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        #si l'ombre est en collision avec le joueur
        else:
            #infliger des degats au joueur
            self.game.player.damage(self.attack)