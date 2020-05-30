import pygame


class LaunchPad:
    def __init__(self, rl_game):
        self.screen = rl_game.screen
        self.settings = rl_game.settings
        self.screen_rect = rl_game.screen_rect

        self.image = pygame.image.load('images/tower_v2.png')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.rect.y -= 20  # calibrate where it needs to go
        self.y = float(self.rect.y)

    def draw_tower(self):
        if self.rect.y < self.settings.HEIGHT:
            self.screen.blit(self.image, self.rect)

    def move_tower(self):
        if self.settings.check_cloud_move:
            self.y += self.settings.speed
            self.rect.y = self.y
