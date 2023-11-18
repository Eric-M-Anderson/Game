import pygame
import button
pygame.font.init()


class Player:
    def __init__(self, w, name, colour, base_location_x, base_location_y):
        self.world = w
        self.name = name
        self.colour = colour
        self.money = 1000
        self.base_size = 16
        self.base_location_x = self.convert_to_pixels(base_location_x - 1)
        self.base_location_y = self.convert_to_pixels(base_location_y - 1)
        self.is_turn = False
        self.my_font = pygame.font.SysFont('Comic Sans MS', 50)

    def spawn_base(self, surface):
        pygame.draw.rect(surface, self.colour, pygame.Rect(self.base_location_x, self.base_location_y, self.base_size, self.base_size))
        pygame.display.update()

    def convert_to_pixels(self, tile_number):
        return (tile_number * self.world.get_tile_size()) + (self.world.get_tile_size() / 2) - self.base_size/2

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

    def turn(self, surface, player):
        text = self.my_font.render(f'$ {self.get_money()} ', True, self.colour, (0, 0, 0))
        surface.blit(text, (1680, 750))
        b = button.Button(surface, 1680, 850, text='Next Turn', command=lambda: self.end_turn(player))
        b.update()
