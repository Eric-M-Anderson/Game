import pygame
import random
import math


class World:
    def __init__(self, world_surface, width, height, tile_size):
        self.world_surface = world_surface
        self.width = width
        self.height = height
        self.tile_size = tile_size
        self.map = self.init_map()
        self.init_world()

    @staticmethod
    def set_tile_type():
        types = ['water', 'grass', 'grass', 'grass', 'grass', 'grass']
        tile_type = types[random.randint(0, 5)]
        if tile_type == 'water':
            return [(48, 159, 219), 'water']
        elif tile_type == 'grass':
            return [(16, 122, 44), 'grass']

    def init_map(self):
        world_list = []
        max_width = math.floor(self.width / self.tile_size)
        max_height = math.floor(self.height / self.tile_size)
        y = self.tile_size / 2
        for a in range(max_height):
            row = []
            x = self.tile_size / 2
            for b in range(max_width):
                stt = self.set_tile_type()
                row.append(Tile(self.world_surface, x, y, self.tile_size, stt[1], stt[0]))
                x += self.tile_size
            world_list.append(tuple(row))
            y += self.tile_size
        return tuple(world_list)

    def init_world(self):
        for i in self.map:
            for j in i:
                j.init_tile()

    def get_world_map(self):
        return self.map

    def get_tile_size(self):
        return self.tile_size


class Tile:
    def __init__(self, surface, x, y, size, ttype, colour=(0, 0, 255)):
        """
        :param surface: Is the location the tile is drawn on. Also known as the game window
        :param x: The center x coordinate of the tile (int)
        :param y: The center y coordinate of the tile (int)
        :param size: The length in pixels of one side of the tile (int)
        :param colour: Sets the colour of the tile as a rgb value (tuple of ints)
        :param ttype: the type of tile
        """

        self.surface = surface
        self.x = x
        self.y = y
        self.size = size
        self.colour = colour
        self.ttype = ttype

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
            self.is_hovering = False

    def get_ttype(self):
        return self.ttype

    def on_click(self):
        pass

