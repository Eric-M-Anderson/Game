import pygame


class World:
    pass


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

        self.is_hovering = False

    def init_tile(self):
        # Draws the tile on the screen
        pygame.draw.rect(self.surface, self.colour, pygame.Rect(self.cx, self.cy, self.size, self.size))
        pygame.draw.rect(self.surface, (100, 100, 100), pygame.Rect(self.cx, self.cy, self.size, self.size), 1)
        pygame.display.update()

    def mouse_track(self):
        if self.cx < pygame.mouse.get_pos()[0] < self.x + self.size / 2 and self.cy < pygame.mouse.get_pos()[1] < self.y + self.size / 2:
            # Puts a highlight over the tile if the mouse is over it
            pygame.draw.rect(self.surface, (255, 255, 255), pygame.Rect(self.cx, self.cy, self.size, self.size), 3)
            self.is_hovering = True
            pygame.display.update()
        elif self.is_hovering is True:
            # Resets the tile to default if the mouse is not over it
            pygame.draw.rect(self.surface, self.colour, pygame.Rect(self.cx, self.cy, self.size, self.size))
            pygame.draw.rect(self.surface, (100, 100, 100), pygame.Rect(self.cx, self.cy, self.size, self.size), 1)

