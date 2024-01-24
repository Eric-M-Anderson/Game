import pygame
import button
import utilities
pygame.font.init()


class Player:
    def __init__(self, w, surface, name, colour, base_location_x, base_location_y):
        self.u = utilities.Utilities()
        self.w = w
        self.surface = surface
        self.name = name
        self.colour = colour
        self.money = 1000
        self.base_size = 16
        self.base_location_x = base_location_x - 1  # self.u.center_square_tile_square(w, base_location_x, base_location_y, self.base_size)[0]
        self.base_location_y = base_location_y - 1  # self.u.center_square_tile_square(w, base_location_x, base_location_y, self.base_size)[1]
        self.is_turn = False
        self.my_font = pygame.font.SysFont('Comic Sans MS', 50)
        self.total_turns = 0
        self.spawn_base()

    def spawn_base(self):
        tile = self.w.get_world_map()[self.base_location_y][self.base_location_x]
        tile.set_has_building(True)
        tile.set_btype('Base')
        tile.set_building_owner(self.name)
        tile.create_building()
        # pygame.draw.rect(self.surface, self.colour, pygame.Rect(self.base_location_x, self.base_location_y, self.base_size, self.base_size))
        # pygame.display.update()

    def convert_to_pixels(self, tile_number):
        return (tile_number * self.w.get_tile_size()) + (self.w.get_tile_size() / 2) - self.base_size/2

    def get_money(self):
        return self.money

    def increase_money(self, m_increase):
        self.money += m_increase

    def get_is_turn(self):
        return self.is_turn

    def set_is_turn(self, is_turn):
        self.is_turn = is_turn

    def end_turn(self, player):
        self.is_turn = False
        player.set_is_turn(True)
        self.increase_money(100)
        self.total_turns += 1

    def turn(self, surface, player):
        text = self.my_font.render(f'$ {self.get_money()} ', True, self.colour, (0, 0, 0))
        surface.blit(text, (1680, 750))
        b = button.Button(surface, 1680, 850, text='Next Turn', command=lambda: self.end_turn(player))
        b.update()
