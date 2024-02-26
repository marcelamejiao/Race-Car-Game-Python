import pygame
from pygame.locals import *
import random

# Screen size
size = width, height = (1200, 800)
# Road size
road_width = int(width/1.6)
# Road mark
roadmark_width = int(width/80)
right_lane = width/2 + road_width/4
left_lane = width/2 - road_width/4

speed = 1

# Initialize the game
pygame.init()
running = True

# Set screen size
screen = pygame.display.set_mode(size)
# Background color
screen.fill((60, 220, 0))
# Screen title
pygame.display.set_caption("Marcela's car game")

# Apply changes
pygame.display.update()

# Load user car image
blue_car = pygame.image.load("blue-car.png")
# Fetch the location of the image
blue_car_location = blue_car.get_rect()
# Locate the car on the screen
blue_car_location.center = left_lane, height * 0.8

# Load opponent car image
red_car = pygame.image.load("red-car.png")
# Fetch the location of the image
red_car_location = red_car.get_rect()
# Locate the car on the screen
red_car_location.center = right_lane, height * 0.2

counter = 0
# Game loop
while running:
    counter += 1
    if counter == 2000:
        speed += 0.25
        counter = 0
        print("level up! ", speed)
    # Animate opponent car
    # To move the car in the Y axis we need to select the second part of the tuple
    red_car_location[1] += speed
    if red_car_location[1] > height:
        if random.randint(0, 1) == 0:
            red_car_location.center = right_lane, -200
        else:
            red_car_location.center = left_lane, -200
    # End game
    if blue_car_location[0] == red_car_location[0] and red_car_location[1] > blue_car_location[1] - 250:
        print("SORRY YOU LOST!")
        print("GAME OVER! :(")
        break

    for event in pygame.event.get():
        # Add first event listener
        if event.type == QUIT:
            running = False
        # Add second event listener
        if event.type == KEYDOWN:
            # Move the car to the left side
            if event.key in [K_a, K_LEFT]:
                blue_car_location = blue_car_location.move([-int(road_width/2), 0])
                # Move the car to the left side
            if event.key in [K_d, K_RIGHT]:
                blue_car_location = blue_car_location.move([int(road_width / 2), 0])

    # Draw road
    pygame.draw.rect(
        screen,
        (50, 50, 50),
        # Coordinates:
        (width / 2 - road_width / 2, 0, road_width, height))

    # Draw center roadmark
    pygame.draw.rect(
        screen,
        (255, 240, 60),
        # Coordinates
        (width / 2 - roadmark_width / 2, 0, roadmark_width, height))

    # Draw left side roadmark
    pygame.draw.rect(
        screen,
        (255, 255, 255),
        # Coordinates
        (width / 2 - road_width / 2 + roadmark_width * 2, 0, roadmark_width, height))

    # Draw right side roadmark
    pygame.draw.rect(
        screen,
        (255, 255, 255),
        # Coordinates
        (width / 2 + road_width / 2 - roadmark_width * 3, 0, roadmark_width, height))

    # Operation of bitmap images, draw the car
    screen.blit(blue_car, blue_car_location)
    screen.blit(red_car, red_car_location)
    pygame.display.update()

# End the game
pygame.quit()
