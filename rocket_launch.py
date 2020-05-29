import pygame
import sys
import settings
import rocket
import clouds
import sky


class RocketLaunch:
    def __init__(self):
        self.running = True
        self.settings = settings.Settings()
        self.WIDTH = self.settings.WIDTH
        self.HEIGHT = self.settings.HEIGHT
        self.bg_color = self.settings.bg_color

        # initialize screen
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Demo2 Launch")
        self.screen_rect = self.screen.get_rect()

        self.cloud_group = pygame.sprite.Group()
        self.create_clouds()
        self.rocket = rocket.Rocket(self)

    def on_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
                elif event.key == pygame.K_w:
                    self.settings.check_cloud_move = True

    def on_loop(self):
        self.update_clouds()

    def on_render(self):
        self.screen.fill(self.bg_color)
        self.cloud_group.draw(self.screen)
        self.rocket.draw_rocket()
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        while True:
            self.on_event()
            self.on_loop()
            self.on_render()
        self.on_cleanup()

    def create_clouds(self):
        while len(self.cloud_group) < self.settings.cloud_number:
            cloud = clouds.Clouds(self)
            self.cloud_group.add(cloud)

    def update_clouds(self):
        for cloud in self.cloud_group:
            cloud.cloud_movement()
        for cloud in self.cloud_group.copy():
            if cloud.rect.top >= self.settings.HEIGHT:
                self.cloud_group.remove(cloud)
        if len(self.cloud_group) < self.settings.cloud_number:
            self.create_clouds()


if __name__ == '__main__':
    rocket_launch = RocketLaunch()
    rocket_launch.on_execute()
