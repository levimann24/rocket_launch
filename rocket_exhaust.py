import pygame
from pygame import sprite
import random


class Exhaust(sprite.Sprite):
    """creates animated looking exhaust"""

    def __init__(self, rl_game):
        '''Initialized exhaust'''
        super().__init__()
        self.settings = rl_game.settings
        self.screen = rl_game.screen
        self.screen_rect = rl_game.screen_rect
        self.width = self.settings.e_width
        self.height = self.settings.e_height

        self.color_map = {
            'red': (150, 0, 0),
            'orange': (204, 102, 0),
            'white': (230, 230, 230)
        }
        self.pick = random.choice(['red', 'orange', 'white'])
        self.color = self.color_map[self.pick]
        # initialize
        self.rand = random.randint(-3, 3)

        self.rect = pygame.Rect(0, 0, self.width, self.height)

        self.rect.x = random.uniform(
            self.settings.WIDTH/2-80, self.settings.WIDTH/2)
        self.rect.y = random.randint(750, 780)

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.y_speed = random.randint(1, 5)

    def move_exhaust(self):
        if self.settings.check_cloud_move:
            self.y += self.y_speed
            self.rect.y = self.y

    def _custom_random(self, initial, final):
        exclude = [0]
        randInt = random.randint(initial, final)
        return self._custom_random if randInt in exclude else randInt

    def draw_exhaust(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
