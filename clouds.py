import pygame
from pygame import sprite
import random


class Clouds(sprite.Sprite):

    def __init__(self, rl_game):
        super().__init__()
        self.screen = rl_game.screen
        self.settings = rl_game.settings

        # load images
        self.color_map = {
            'gray': 'images/cloud_gray.png',
            # 'white': 'images/cloud_white.png',
            'reg': 'images/cloud.png'
        }
        self.pick = random.choice(['gray', 'reg'])  # , 'white'])
        self.rand_cloud = self.color_map[self.pick]
        self.image = pygame.image.load(self.rand_cloud)
        self.rect = self.image.get_rect()

        self.x = random.randint(1, self.settings.WIDTH - self.rect.width)
        self.y = random.randint(-1500, -500)

        self.rect.x = self.x
        self.rect.y = self.y

    def cloud_movement(self):
        if self.settings.check_cloud_move:
            self.y += self.settings.speed
        self.rect.y = self.y
