import pygame
import sys

WIDTH = 800
HEIGHT = 600
BOX_SIZE = 50

screen = pygame.display.set_mode((WIDTH, HEIGHT))

player = pygame.Rect(100, 100, BOX_SIZE, BOX_SIZE)
boxes = []
boxes.append(pygame.Rect(200, 200, BOX_SIZE, BOX_SIZE))
boxes.append(pygame.Rect(300, 300, BOX_SIZE, BOX_SIZE))

while True:
    # Check for events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    # Update the game state.
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        player.x -= BOX_SIZE
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        player.x += BOX_SIZE
    if pygame.key.get_pressed()[pygame.K_UP]:
        player.y -= BOX_SIZE
    if pygame.key.get_pressed()[pygame.K_DOWN]:
        player.y += BOX_SIZE
    # Check for collisions.
    for box in boxes:
        if player.colliderect(box):
            # Check if the player is pushing a box.
            if player.x < box.x:
                # The player is pushing the box to the left.
                box.x -= BOX_SIZE
            elif player.x > box.x:
                # The player is pushing the box to the right.