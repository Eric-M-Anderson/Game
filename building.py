import pygame
import abc
import utilities


class Building(abc.ABC):
    def __init__(self, w_size, surface, x, y, ownership):
        self.w_size = w_size
        self.surface = surface
        self.x = x
        self.y = y
        self.ownership = ownership

    @abc.abstractmethod
    def set_owner(self, player):
        """Method documentation"""
        return

    @abc.abstractmethod
    def get_owner(self, player):
        """Method documentation"""
        return

    @abc.abstractmethod
    def update(self):
        """Method documentation"""
        return


class Base(Building):
    def __init__(self, w, surface, x, y, ownership, size=20, xy_is_grid=True):
        super().__init__(w, surface, x, y, ownership)
        self.w = w
        self.u = utilities.Utilities()
        self.surface = surface
        self.ownership = ownership
        self.size = size

        if xy_is_grid is False:
            self.location = self.u.center_square_tile_square(w, x, y, self.size, True)
        else:
            self.location = self.u.center_square_tile_square(w, x, y, self.size)

    def set_owner(self, player):
        pass

    def get_owner(self, player):
        pass

    def update(self):
        if self.ownership == 'Red_Player':
            pygame.draw.rect(self.surface, (255, 0, 0), pygame.Rect(self.location[0], self.location[1], self.size, self.size))
        elif self.ownership == 'Blue_Player':
            pygame.draw.rect(self.surface, (0, 0, 255), pygame.Rect(self.location[0], self.location[1], self.size, self.size))
        elif self.ownership == 'No_Player':
            pygame.draw.rect(self.surface, (50, 50, 50), pygame.Rect(self.location[0], self.location[1], self.size, self.size))


class LandFactory(Building):
    def __init__(self, w, surface, x, y, ownership, radius=10, xy_is_grid=True):
        super().__init__(w, surface, x, y, ownership)
        self.w = w
        self.u = utilities.Utilities()
        self.surface = surface
        self.ownership = ownership
        self.radius = radius
        if xy_is_grid is False:
            self.location = self.u.center_square_tile_circle(w, x, y, True)
        else:
            self.location = (x, y)
        # pygame.draw.rect(surface, self.colour, pygame.Rect(self.base_location_x, self.base_location_y, self.base_size, self.base_size))

    def set_owner(self, player):
        pass

    def get_owner(self, player):
        pass

    def update(self):
        if self.ownership == 'Red_Player':
            pygame.draw.circle(self.surface, (255, 0, 0), self.location, self.radius)
        elif self.ownership == 'Blue_Player':
            pygame.draw.circle(self.surface, (0, 0, 255), self.location, self.radius)
        elif self.ownership == 'No_Player':
            pygame.draw.circle(self.surface, (50, 50, 50), self.location, self.radius)

