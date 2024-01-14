import pygame

#definir une classe qui va s'occuper des animations
class AnimateSprite(pygame.sprite.Sprite):

    #definir les chosesàfaireàla création de l'entité
    def __init__(self, sprite_name):
        super().__init__()
        self.image = pygame.image.load(f'Valorant_Assets/{sprite_name}.png')
        self.current_image = 0  #commencer l'animàtion a l'image 0
        self.images = self.animations.get('shadow')
        self.animations = False

    # definir une methode pour démarrer l'animation
    def start_animation(self):
        self.animation = True

    #definir une methode pour animer le sprite
    def animate(self):

        #passer a l'image suivante
        self.current_image += 1

        # verifier si onaatteint la fin de l'animation
        if self.current_image >= len(self.images):
            # remettre l'animation au départ
            self.current_image = 0

        #modifier
        self.image = self.images[self.current_image]

    # definition de la fonction du sprite
    def load_animation_images(sprite_name):
    # charger les images
        images = []
        # recuperation du chemain des sprite
        path = f"Valorant_Assets/{sprite_name}/{sprite_name}"


        # boucler chaque image
        for num in range(1, 9):
            image_path = path + str(num) + '.png'
            pygame.image.load(image_path)
            images.append(pygame.image.load(image_path))

        # renvoyer le contenu de la liste des image
        return images

    # definir un dictionnaire qui va contenire les image charger
    # shadow -> [...shadow1.png]
    animations = {
        'shadow': load_animation_images('shadow')

        }
