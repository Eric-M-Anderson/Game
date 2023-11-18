import pygame


class Button:
    def __init__(self, surface, x, y, colour=(100, 100, 200), h_colour=(200, 200, 200), t_colour=(255, 255, 255), ht_colour=(0, 0, 0), text='Button',
                 font_type='Comic Sans MS', font_size=20, command=lambda: print("clicked right now")):
        self.surface = surface
        self.x = x
        self.y = y
        self.colour = colour
        self.h_colour = h_colour
        self.t_colour = t_colour
        self.ht_colour = ht_colour
        self.text = f' {text} '
        self.font_type = font_type
        self.font_size = font_size
        self.font = pygame.font.SysFont(self.font_type, self.font_size)
        self.need_space = self.font.size(self.text)
        self.command = command
        self.pressed = False

    def update(self):
        if self.is_hovering():
            font = self.font.render(self.text, True, self.ht_colour, self.h_colour)
            self.check_if_click()
        else:
            font = self.font.render(self.text, True, self.t_colour, self.colour)
        self.surface.blit(font, (self.x, self.y))
        pygame.display.update()

    def is_hovering(self):
        if self.x < pygame.mouse.get_pos()[0] < (self.x + self.need_space[0]) and self.y < pygame.mouse.get_pos()[1] < (self.y + self.need_space[1]):
            return True
        else:
            return False

    def check_if_click(self):
        if self.is_hovering():
            if pygame.mouse.get_pressed()[0] and self.pressed is False:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONUP:
                        self.command()
                        self.pressed = True
            if pygame.mouse.get_pressed()[0] == 0:
                self.pressed = False
