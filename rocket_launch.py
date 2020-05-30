import pygame
import sys
import settings
import rocket
import clouds
import star
import rocket_exhaust
import time
import launch_pad


class RocketLaunch:
    def __init__(self):
        self.running = True
        self.settings = settings.Settings()
        self.WIDTH = self.settings.WIDTH
        self.HEIGHT = self.settings.HEIGHT
        self.red = 58
        self.green = 177
        self.blue = 255
        self.bg_color = (self.red, self.green, self.blue)
        # self.bg_color = self.settings.bg_color

        # initialize screen
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Demo2 Launch")
        self.screen_rect = self.screen.get_rect()
        self.stars = star.pygame.sprite.Group()
        self.create_stars()
        # create Clouds
        self.cloud_group = pygame.sprite.Group()
        self.create_clouds()
        # create Rocket
        self.rocket = rocket.Rocket(self)
        # create exhaust
        self.exhaust_group = pygame.sprite.Group()
        self.create_exhaust()
        # create tower
        self.tower = launch_pad.LaunchPad(self)
        # fps
        self.FPS = 60
        self.clock = pygame.time.Clock()

# ---------------------------------------------

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

        self.update_stars()
        self.update_clouds()
        self.update_exhaust()
        if self.settings.check_cloud_move:
            self.change_sky_color()
        self.tower.move_tower()
        self.update_rocket()

    def on_render(self):
        self.screen.fill(self.bg_color)
        for star in self.stars.sprites():
            star.draw_star()
        self.cloud_group.draw(self.screen)
        for exhaust in self.exhaust_group.sprites():
            exhaust.draw_exhaust()
        self.tower.draw_tower()
        self.rocket.draw_rocket()
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        while True:
            self.clock.tick(self.FPS)
            self.on_event()
            self.on_loop()
            self.on_render()
        self.on_cleanup()

# ---------------------------------------------
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
        if len(self.cloud_group) < self.settings.cloud_number and self.blue > 100:
            self.create_clouds()

# ---------------------------------------------
    def create_exhaust(self):
        while len(self.exhaust_group) < self.settings.e_number:
            exhaust = rocket_exhaust.Exhaust(self)
            self.exhaust_group.add(exhaust)

    def update_exhaust(self):
        for exhaust in self.exhaust_group:
            exhaust.move_exhaust()
        for exhaust in self.exhaust_group:
            if exhaust.rect.top >= self.settings.HEIGHT:
                self.exhaust_group.remove(exhaust)
        if len(self.exhaust_group) < self.settings.e_number and self.blue > 50:
            self.create_exhaust()

# ---------------------------------------------
    def change_sky_color(self):
        color_change = .15
        if self.red >= 0:
            self.red -= color_change
        if self.blue >= 0:
            self.blue -= color_change
        if self.green >= 0:
            self.green -= color_change
        self.bg_color = (self.red, self.green, self.blue)
# ---------------------------------------------

    def create_stars(self):
        if self.blue < 100:
            while len(self.stars) < self.settings.stars_allowed:
                star_i = star.Star(self)
                self.stars.add(star_i)

    def update_stars(self):
        for star in self.stars:
            star.move_star()
        for star in self.stars:
            if star.rect.top >= self.settings.HEIGHT:
                self.stars.remove(star)

        if len(self.stars) < self.settings.stars_allowed:
            self.create_stars()
# ---------------------------------------------

    def update_rocket(self):
        if self.blue <= 0:
            self.rocket.move_rocket()
        if self.rocket.rect.bottom <= 0:
            sys.exit()


if __name__ == '__main__':
    rocket_launch = RocketLaunch()
    rocket_launch.on_execute()
