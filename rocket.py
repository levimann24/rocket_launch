import pygame


class Rocket:
    def __init__(self, rl_game):
        self.screen = rl_game.screen
        self.settings = rl_game.settings
        self.screen_rect = rl_game.screen_rect

        self.image = pygame.image.load('images/crew_dragon.png')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.rect.y -= 40

    def draw_rocket(self):
        self.screen.blit(self.image, self.rect)
