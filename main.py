# import pygame package
import pygame
import world
import random
import math

# initializing imported module
pygame.init()

# displaying a window of height
# 500 and width 400
surface = pygame.display.set_mode((1900, 980))
# surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

# Setting name for window
pygame.display.set_caption('Game Name')

# creating a bool value which checks
# if game is running
running = True


def set_tile_type():
    types = ['water', 'grass', 'grass', 'grass', 'grass', 'grass']
    tile_type = types[random.randint(0, 5)]
    if tile_type == 'water':
        return 48, 159, 219
    elif tile_type == 'grass':
        return 16, 122, 44


def init_world(world_surface, width, height, tile_size):
    world_list = []
    max_width = math.floor(width / tile_size)
    max_height = math.floor(height / tile_size)
    y = tile_size / 2
    for a in range(max_height):
        row = []
        x = tile_size / 2
        for b in range(max_width):
            row.append(world.Tile(world_surface, x, y, tile_size, set_tile_type()))
            x += tile_size
        world_list.append(tuple(row))
        y += tile_size
    return tuple(world_list)


world_map = init_world(surface, 1900, 980, 30)
count = 0
# Game loop
# keep game running till running is true
while running:
    count += 1

    for i in world_map:
        for j in i:
            j.draw()
    # Check for event if user has pushed
    # any event in queue
    for event in pygame.event.get():

        # if event is of type quit then set
        # running bool to false
        if event.type == pygame.QUIT:
            running = False
