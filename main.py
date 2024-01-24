# import pygame package
import pygame
import world
import player
import button
import building
import unit

# initializing imported module
pygame.init()

# displaying a window of height
# 1860 and width 980
surface = pygame.display.set_mode((1860, 980))
# surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

# Setting name for game window
pygame.display.set_caption('Game Name')

# A variable to check if the game is running
running = True

# Represents the game ticks
tick = 0

# This is the main game loop and will run until False
while running:

    # Looks for user events like key presses
    for event in pygame.event.get():

        # Only runs once when the game starts
        if tick == 0:

            # Generates the world
            w = world.World(surface, 1900, 750, 30)

            # Generates a unit and puts it in the world
            u = unit.Unit(w, surface, 4, 4, 'Red_Player', 0, 0, 0, 0)

            """while True:
                base_location_x = int(input(f"Where do you want your base on the x position: "))
                base_location_y = int(input(f"Where do you want your base on the y position: "))

                world_map = w.get_world_map()
                if world_map[base_location_y - 1][base_location_x - 1].get_ttype() == 'grass':
                    break"""

            # The variables tha represent the x and y location of player one's base
            base_location_x1 = 4
            base_location_y1 = 4

            # Generates player 1 and puts a base in the world
            player1 = player.Player(w, surface, 'Red_Player', (255, 0, 0), base_location_x1, base_location_y1)
            # Sets it to player one's turn
            player1.set_is_turn(True)

            # The variables tha represent the x and y location of player two's base
            base_location_x2 = 59
            base_location_y2 = 21

            # Generates player 2 and puts a base in the world
            player2 = player.Player(w, surface, 'Blue_Player', (0, 0, 255), base_location_x2, base_location_y2)
            # lf = building.LandFactory(w, surface, 10, 20, 'No_Player')

        # Updates the mouse hovering Graphic
        for i in w.get_world_map():
            for j in i:
                j.update()

        # Spawns/Updates player one's base
        # player1.spawn_base(surface)
        # Spawns/Updates player two's base
        # player2.spawn_base(surface)

        # Controls which player can make actions
        if player1.get_is_turn() is True:
            # Checks for player one to make key presses to move a unit
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    u.move_x(-1)
                if event.key == pygame.K_RIGHT:
                    u.move_x(1)
                if event.key == pygame.K_UP:
                    u.move_y(-1)
                if event.key == pygame.K_DOWN:
                    u.move_y(1)
                u.update()
            player1.turn(surface, player2)
        elif player2.get_is_turn() is True:
            player2.turn(surface, player1)

        u.update()

        # if the event is quit the variable running is set to false
        if event.type == pygame.QUIT:
            running = False

        # Increases the game tick tracker
        tick += 1
        pygame.display.update()
