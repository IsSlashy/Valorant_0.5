import pygame

# Projectile Class
class Projectile(pygame.sprite.Sprite):

    #Constructeur
    def __init__(self,player):
        super().__init__()
        self.velocity = 40
        self.player = player
        self.image = pygame.image.load('Valorant_Assets/projectile.png')
        self.image = pygame.transform.scale(self.image,(200,200))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 80

    def remove(self):
        self.player.all_projectile.remove(self)

    def move(self):
     self.rect.x += self.velocity

    #Verifier la collision avec l'ombre
     for shadow in self.player.game.check_collision(self, self.player.game.all_shadow):
        # delete projectile
        self.remove()
        # infliger
        shadow.damage(self.player.attack)

    #verif projectile
     if self.rect.x > 1920:
        # Delete projectile
        self.player.all_projectile.remove(self)