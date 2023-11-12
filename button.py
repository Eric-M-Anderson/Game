import pygame


class Button:
    def __init__(self, surface, x, y, width, height, colour=(100, 100, 200), h_colour=(200, 200, 200), t_colour=(255, 255, 255), text='Button',
                 font_type='Comic Sans MS', font_size=20, command=lambda: print("clicked right now")):
        self.surface = surface
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
        self.h_colour = h_colour
        self.t_colour = t_colour
        self.text = text
        self.font_type = font_type
        self.font_size = font_size
        self.font = pygame.font.SysFont(self.font_type, self.font_size)
        self.command = command
        self.pressed = False

        self.cx = self.x - self.width / 2
        self.cy = self.y - self.height / 2

    def update(self):
        if self.is_hovering():
            pygame.draw.rect(self.surface, self.h_colour, pygame.Rect(self.cx, self.cy, self.width, self.height))
            pygame.draw.rect(self.surface, self.colour, pygame.Rect(self.cx, self.cy, self.width, self.height), 1)
            self.check_if_click()
        else:
            pygame.draw.rect(self.surface, self.colour, pygame.Rect(self.cx, self.cy, self.width, self.height))
            pygame.draw.rect(self.surface, self.h_colour, pygame.Rect(self.cx, self.cy, self.width, self.height), 1)
        self.surface.blit(self.font.render(self.text, False, self.t_colour), (self.x - self.width / 4.5, self.y - self.height / 4))
        pygame.display.update()

    def is_hovering(self):
        if self.cx < pygame.mouse.get_pos()[0] < self.x + self.width / 2 and self.cy < pygame.mouse.get_pos()[1] < self.y + self.height / 2:
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
