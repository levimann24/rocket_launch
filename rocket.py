import pygame


class Rocket:
    def __init__(self, rl_game):
        self.screen = rl_game.screen
        self.settings = rl_game.settings
        self.screen_rect = rl_game.screen_rect
        self.blue = rl_game.blue

        self.image = pygame.image.load('images/crew_dragon_v2.png')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        # calibrate where it needs to go
        self.rect.y += 10
        self.rect.x -= 15
        self.y = float(self.rect.y)

    def draw_rocket(self):
        self.screen.blit(self.image, self.rect)

    def move_rocket(self):
        self.y -= self.settings.speed
        self.rect.y = self.y
