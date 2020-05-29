class Settings:

    def __init__(self):

        # screen settings
        self.WIDTH = 800
        self.HEIGHT = 1000
        self.red = 58
        self.green = 177
        self.blue = 255
        self.bg_color = (self.red, self.green, self.blue)  # (58, 177, 255)

        # clouds
        self.cloud_number = 25

        # set speed and movement of cloud
        self.speed = 5
        self.check_cloud_move = False
