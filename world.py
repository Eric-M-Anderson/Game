import pygame


class Tile:
    def __init__(self, surface, x, y, size, colour=(0, 0, 255)):
        """
        :param surface: Is the location the tile is drawn on. Also known as the game window
        :param x: The center x coordinate of the tile (int)
        :param y: The center y coordinate of the tile (int)
        :param size: The length in pixels of one side of the tile (int)
        :param colour: Sets the colour of the tile as a rgb value (tuple of ints)
        """

        self.surface = surface
        self.x = x
        self.y = y
        self.size = size
        self.colour = colour

        half_of_size = self.size / 2
        self.cx = self.x - half_of_size
        self.cy = self.y - half_of_size

        self.tile = ''

    def draw(self):
        self.tile = pygame.draw.rect(self.surface, self.colour, pygame.Rect(self.cx, self.cy, self.size, self.size))
        pygame.draw.rect(self.surface, (100, 100, 100), pygame.Rect(self.cx, self.cy, self.size, self.size), 1)
        if self.tile.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(self.surface, (255, 255, 255), pygame.Rect(self.cx, self.cy, self.size, self.size), 3)
        pygame.display.update()
