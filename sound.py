import pygame
class SoundManager:

    def __init__(self):
        self.sounds={

            'click':pygame.mixer.Sound("Valorant_Assets/sounds/click.ogg"),
            'game_over':pygame.mixer.Sound("Valorant_Assets/sounds/game_over.ogg"),
            'tir':pygame.mixer.Sound("Valorant_Assets/sounds/tir.ogg"),
        }

    def play(self, name):
        self.sounds[name].play()