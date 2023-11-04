# import pygame package
import pygame
import world
import player

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

count = 0
# Game loop
# keep game running till running is true
while running:

    if count == 0:
        # Draws the world for the first time
        w = world.World(surface, 1900, 980, 30)
        base_location_x = int(input(f"Where do you want your base on the x position: "))
        base_location_y = int(input(f"Where do you want your base on the y position: "))
        player1 = player.Player(w, 'Eric', (255, 0, 0), base_location_x, base_location_y)

    # Updates the mouse hovering Graphic
    for i in w.get_world_map():
        for j in i:
            j.mouse_track()

    player1.spawn_base(surface)

    # Check for event if user has pushed
    # any event in queue
    for event in pygame.event.get():

        # if event is of type quit then set
        # running bool to false
        if event.type == pygame.QUIT:
            running = False

    count += 1
