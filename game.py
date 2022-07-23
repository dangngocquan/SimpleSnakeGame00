from random import random
import pygame
import sys

def display_snake():
    dis.fill(BLACK)
    for snake_block in snake_block_list:
        dis.blit(snake_body, (snake_block[0], snake_block[1]))

def display_food():
    dis.blit(food_block, (food_x, food_y))
    
pygame.init()

length = 1000
width = 600
snake_block_size = 20
speed = 20
snake_block_list = []

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
snake_body = pygame.image.load("assets\snake_body.png")
snake_body = pygame.transform.scale(snake_body, (snake_block_size, snake_block_size))

dis = pygame.display.set_mode((length, width))
pygame.display.update()
pygame.display.set_caption("Snake Game")

game_over = False

snake_head_x = 0
snake_head_y = 0
snake_block_list.append([snake_head_x, snake_head_y])

food_x = (round(random() * (length - snake_block_size)) // snake_block_size) * snake_block_size
food_y = (round(random() * (width - snake_block_size)) // snake_block_size) * snake_block_size
food_block = pygame.image.load("assets\\food.jpg")
food_block = pygame.transform.scale(food_block, (snake_block_size-2, snake_block_size - 2))

x_change = 0
y_change = 0

clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                x_change = 0
                y_change = -snake_block_size
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                x_change = 0
                y_change = snake_block_size
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                x_change = -snake_block_size
                y_change = 0
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                x_change = snake_block_size
                y_change = 0
    if snake_head_x == food_x and snake_head_y == food_y:
        last_snake_block = snake_block_list[len(snake_block_list) - 1]
        snake_block_list.append([last_snake_block[0] - snake_block_size, last_snake_block[1] - snake_block_size])
        food_x = (round(random() * (length - snake_block_size)) // snake_block_size) * snake_block_size
        food_y = (round(random() * (width - snake_block_size)) // snake_block_size) * snake_block_size
    snake_head_x += x_change
    snake_head_y += y_change
    snake_block_list.insert(0, [snake_head_x, snake_head_y])
    del snake_block_list[len(snake_block_list) - 1]
    display_snake()
    display_food()
    pygame.display.update()
    
    clock.tick(speed)
        
pygame.quit()
quit()




