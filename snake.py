#SNAKE GAME USING PYTHON

import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
light_gray = (200, 200, 200) 

width, height = 800, 600

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')


clock = pygame.time.Clock()
snake_speed = 15

block_size = 20

font_style = pygame.font.SysFont("Ariest", 40)
score_font = pygame.font.SysFont("comicsansms", 35)

def display_score(score):
    value = score_font.render(f"Your Score: {score}", True, yellow)
    screen.blit(value, [0, 0])

def draw_snake(block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, green, [x[0], x[1], block_size, block_size])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [width / 6, height / 3])

def game_loop():
    game_over = False
    game_close = False

    x1, y1 = width / 2, height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    food_x = round(random.randrange(0, width - block_size) / 20.0) * 20.0
    food_y = round(random.randrange(0, height - block_size) / 20.0) * 20.0

    while not game_over:

        while game_close:
            screen.fill(light_gray)  
            message("You lost! Press Q-Quit or C-Play Again", red)
            display_score(length_of_snake - 1)
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
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = block_size
                    x1_change = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        screen.fill(light_gray)  
        pygame.draw.rect(screen, red, [food_x, food_y, block_size, block_size])

        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        draw_snake(block_size, snake_list)
        display_score(length_of_snake - 1)

        pygame.display.update()

        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, width - block_size) / 20.0) * 20.0
            food_y = round(random.randrange(0, height - block_size) / 20.0) * 20.0
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Start the game
game_loop()
