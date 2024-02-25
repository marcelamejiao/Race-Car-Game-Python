import pygame
from pygame.locals import *

# Screen size
size = width, height = (1200, 800)
# Road size
road_width = int(width/1.6)
# Road mark
roadmark_width = int(width/80)

# Initialize the game
pygame.init()
running = True

# Set screen size
screen = pygame.display.set_mode(size)
# Background color
screen.fill((60, 220, 0))
# Screen title
pygame.display.set_caption("Marcela's car game")
# Draw road
pygame.draw.rect(
    screen,
    (50, 50, 50),
    # Coordinates:
    (width/2 - road_width/2, 0, road_width, height))

# Draw center roadmark
pygame.draw.rect(
    screen,
    (255, 240, 60),
    # Coordinates
    (width/2 - roadmark_width/2, 0, roadmark_width, height))

# Draw left side roadmark
pygame.draw.rect(
    screen,
    (255, 255, 255),
    # Coordinates
    (width/2 - road_width/2 + roadmark_width * 2, 0, roadmark_width, height))

# Draw right side roadmark
pygame.draw.rect(
    screen,
    (255, 255, 255),
    # Coordinates
    (width/2 + road_width/2 - roadmark_width * 3, 0, roadmark_width, height))


# Apply changes
pygame.display.update()

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

# End the game
pygame.quit()