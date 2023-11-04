import pygame


class Player:
    def __init__(self, w, name, colour, base_location_x, base_location_y):
        self.world = w
        self.name = name
        self.colour = colour
        self.money = 1000
        self.base_size = 16
        self.base_location_x = self.convert_to_pixels(base_location_x - 1)
        self.base_location_y = self.convert_to_pixels(base_location_y - 1)

    def spawn_base(self, surface):
        pygame.draw.rect(surface, self.colour, pygame.Rect(self.base_location_x, self.base_location_y, self.base_size, self.base_size))
        pygame.display.update()

    def convert_to_pixels(self, tile_number):
        return (tile_number * self.world.get_tile_size()) + (self.world.get_tile_size() / 2) - self.base_size/2
