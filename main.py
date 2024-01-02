# import pygame package
import pygame
import world
import player
import button
import building

# initializing imported module
pygame.init()

# displaying a window of height
# 500 and width 400
surface = pygame.display.set_mode((1860, 980))
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
        w = world.World(surface, 1900, 750, 30)
        """while True:
            base_location_x = int(input(f"Where do you want your base on the x position: "))
            base_location_y = int(input(f"Where do you want your base on the y position: "))

            world_map = w.get_world_map()
            if world_map[base_location_y - 1][base_location_x - 1].get_ttype() == 'grass':
                break"""
        base_location_x1 = 4
        base_location_y1 = 4
        player1 = player.Player(w, 'Red_Player', (255, 0, 0), base_location_x1, base_location_y1)
        player1.set_is_turn(True)

        base_location_x2 = 59
        base_location_y2 = 21
        player2 = player.Player(w, 'Blue_Player', (0, 0, 255), base_location_x2, base_location_y2)
        lf = building.LandFactory(w, surface, 10, 20, 'No_Player')

    lf.update()

    # Updates the mouse hovering Graphic
    for i in w.get_world_map():
        for j in i:
            j.mouse_track()

    player1.spawn_base(surface)
    player2.spawn_base(surface)

    if player1.get_is_turn() is True:
        player1.turn(surface, player2)
    elif player2.get_is_turn() is True:
        player2.turn(surface, player1)

    # Check for event if user has pushed
    # any event in queue
    for event in pygame.event.get():

        # if event is of type quit then set
        # running bool to false
        if event.type == pygame.QUIT:
            running = False

    count += 1
