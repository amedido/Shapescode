import pygame
import time
import random

pygame.init()

# Set the width and height of each grid location
width, height = 30, 30

# Set the number of grid locations
num_of_grid = 20

# Set the size of the window
window_size = width * num_of_grid

# Define colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Initialize the game window
game_window = pygame.display.set_mode((window_size, window_size))
pygame.display.set_caption("Snake Game")

# Set the clock
clock = pygame.time.Clock()

font_style = pygame.font.SysFont(None, 50)

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    game_window.blit(mesg, [window_size / 6, window_size / 3])

def game_loop():
    game_over = False
    game_close = False

    # Set the initial position of the snake head
    x1 = window_size / 2
    y1 = window_size / 2

    # Set the initial change in position
    x1_change = 0
    y1_change = 0

    # Initialize the snake list and length
    snake_list = []
    length_of_snake = 1

    # Set the initial position of the food
    foodx = round(random.randrange(0, window_size - width) / width) * width
    foody = round(random.randrange(0, window_size - height) / height) * height

    while not game_over:

        while game_close:
            game_window.fill(black)
            message("You lost! Press C-Continue or Q-Quit", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -width
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = width
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -height
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = height
                    x1_change = 0

        # Check if the snake has gone off the screen
        if x1 >= window_size or x1 < 0 or y1 >= window_size or y1 < 0:
            game_close = True

        # Update the position of the snake head
        x1 += x1_change
        y1 += y1_change

        # Set the color of the game window
        game_window.fill(blue)

        # Draw the food
        pygame.draw.rect(game_window, green, [foodx, foody, width, height])

        # Add the new position of the head to the snake list
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        # Check if the length of the snake list is greater than the length of the snake
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Check if the snake has hit itself
        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        # Draw the snake
        for block in snake_list:
            pygame.draw.rect(game_window, black, [block[0], block[1], width, height])

        # Update the display
        pygame.display.update()

        # Check if the snake has eaten the food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, window_size - width) / width) * width
            foody = round(random.randrange(0, window_size - height) / height) * height
            length_of_snake += 1

        # Set the speed of the snake
        clock.tick(length_of_snake)

    # Quit the game
    pygame.quit()

# Run the game
game_loop()