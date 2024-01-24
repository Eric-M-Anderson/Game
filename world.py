import pygame
import random
import math
import building


class World:
    def __init__(self, surface, width, height, tile_size):
        """
        :param surface: Is the location the tile is drawn on. Also known as the game window
        :param x: The center x coordinate of the tile (int)
        :param y: The center y coordinate of the tile (int)
        :param size: The length in pixels of one side of the tile (int)
        :param colour: Sets the colour of the tile as a rgb value (tuple of ints)
        :param ttype: the type of tile
        """
        self.surface = surface
        self.width = width
        self.height = height
        self.tile_size = tile_size
        self.map = self.init_map()
        self.init_world()

    @staticmethod
    def set_tile_type():
        # Randomly selects what a tile will be
        max_number = 99
        rand_num = random.randint(0, max_number)

        # If the random number is less than 5 the tile is water
        if rand_num < 5:
            return [(48, 159, 219), 'water']
        else:
            return [(16, 122, 44), 'grass']

    def init_map(self):
        # Creates the world map for the play through of the game
        # Contains the list of each world tile object. The first degree index represents a row in the map
        world_list = []

        # Sets the max world size by tiles
        max_width = math.floor(self.width / self.tile_size)
        max_height = math.floor(self.height / self.tile_size)

        # Tracks the tile y position
        y = self.tile_size / 2
        # Runs until the max rows are created
        for a in range(max_height):
            # Rests the working row to empty
            row = []
            # Tracks the tile y position
            x = self.tile_size / 2
            # Runs until the max columns are created
            for b in range(max_width):
                # Sets the type of each tile
                stt = self.set_tile_type()
                max_number = 99
                rand_num = random.randint(0, max_number)
                # If the random number is less than 2 the tile is has a factory on it
                if rand_num < 2:
                    row.append(Tile(self, self.surface, x, y, self.tile_size, stt[1], stt[0], True))
                else:
                    row.append(Tile(self, self.surface, x, y, self.tile_size, stt[1], stt[0]))
                x += self.tile_size
            # Adds a row to the world list
            world_list.append(tuple(row))
            y += self.tile_size
        return tuple(world_list)

    def init_world(self):
        for i in self.map:
            for j in i:
                j.update()

    def get_world_map(self):
        return self.map

    def get_tile_size(self):
        return self.tile_size


class Tile:
    def __init__(self, w, surface, x, y, size, ttype, colour=(0, 0, 255), has_building=False, btype='Factory'):
        """
        :param surface: Is the location the tile is drawn on. Also known as the game window
        :param x: The center x coordinate of the tile (int)
        :param y: The center y coordinate of the tile (int)
        :param size: The length in pixels of one side of the tile (int)
        :param colour: Sets the colour of the tile as a rgb value (tuple of ints)
        :param ttype: the type of tile
        """
        self.w = w
        self.surface = surface
        self.x = x
        self.y = y
        self.size = size
        self.colour = colour
        self.ttype = ttype
        self.btype = btype

        half_of_size = self.size / 2
        self.cx = self.x - half_of_size
        self.cy = self.y - half_of_size

        self.has_building = has_building
        self.building_owner = 'No_Player'
        self.is_hovering = False
        self.poi = None

        self.create_building()

    def update(self):
        # Draws the tile on the screen
        pygame.draw.rect(self.surface, self.colour, pygame.Rect(self.cx, self.cy, self.size, self.size))
        # pygame.draw.rect(self.surface, (100, 100, 100), pygame.Rect(self.cx, self.cy, self.size, self.size), 1)
        self.mouse_track()
        if self.has_building is True:
            self.poi.update()
        # pygame.display.update()

    def create_building(self):
        if self.has_building is True:
            if self.btype == 'Factory':
                self.poi = building.LandFactory(self.w, self.surface, self.x, self.y, self.building_owner, 10)
            if self.btype == 'Base':
                self.poi = building.Base(self.w, self.surface, self.x, self.y, self.building_owner)

    def mouse_track(self):
        if self.cx < pygame.mouse.get_pos()[0] < self.x + self.size / 2 and self.cy < pygame.mouse.get_pos()[1] < self.y + self.size / 2:
            self.is_hovering = True
        else:
            self.is_hovering = False
        if self.is_hovering is False:
            pygame.draw.rect(self.surface, (100, 100, 100), pygame.Rect(self.cx, self.cy, self.size, self.size), 1)
        elif self.is_hovering is True:
            pygame.draw.rect(self.surface, (255, 255, 255), pygame.Rect(self.cx, self.cy, self.size, self.size), 3)

    def get_has_building(self):
        return self.has_building

    def get_ttype(self):
        return self.ttype

    def on_click(self):
        pass

    def set_has_building(self, new_has_building):
        self.has_building = new_has_building

    def set_btype(self, new_btype):
        self.btype = new_btype

    def set_building_owner(self, new_building_owner):
        self.building_owner = new_building_owner

