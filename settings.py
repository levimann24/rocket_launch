import random


class Settings:

    def __init__(self):

        # screen settings
        self.WIDTH = 700
        self.HEIGHT = 900

        # clouds
        self.cloud_number = 10

        # set speed and movement of cloud
        self.speed = 5
        self.check_cloud_move = False

        # Exhaust settings
        self.e_x_speed = .5
        self.e_width = 10
        self.e_height = 10
        self.e_color = (150, 0, 0)
        self.e_number = 200

        # Star settings
        self.star_height = 1
        self.star_width = 1
        self.star_color = (230, 230, 230)
        self.stars_allowed = 1000
