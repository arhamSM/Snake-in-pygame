import pygame
import random

# Define some colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# Define screen size
screen_width = 800
screen_height = 600

# Define block size
block_size = 20

# Define initial snake speed
snake_speed = 10

# Initialize Pygame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

# Define font for score display
font_style = pygame.font.SysFont(None, 25)

def display_score(score):
    value = font_style.render(f"Your Score: {score}", True, white)
    screen.blit(value, [0, 0])

def draw_snake(snake_list):
    for block in snake_list:
        pygame.draw.rect(screen, green, [block[0], block[1], block_size, block_size])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [screen_width / 6, screen_height / 3])

def game_loop():
    game_close = False
    game_over = False

    x1 = screen_width / 2
    y1 = screen_height / 2
    x1_change = 0
    y1_change = 0

    snake_list = []
    snake_length = 1

    food_x = round(random.randrange(0, screen_width - block_size) / block_size) * block_size
    food_y = round(random.randrange(0, screen_height - block_size) / block_size) * block_size

    clock = pygame.time.Clock()

    while not game_close:

        while game_over:
            screen.fill(black)
            message("You Lost! Press Q - Quit or C - Play Again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_close = True
                        game_over = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_close = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change != block_size:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change != -block_size:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change != block_size:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change != -block_size:
                    y1_change = block_size
                    x1_change = 0

        x1 += x1_change
        y1 += y1_change

        if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
            game_over = True

        screen.fill(black)
        pygame.draw.rect(screen, red, [food_x, food_y, block_size, block_size])

        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        for block in snake_list[:-1]:
            if block == snake_head:
                game_over = True

        draw_snake(snake_list)
        display_score(snake_length - 1)

        pygame.display.update()

        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, screen_width - block_size) / block_size) * block_size
            food_y = round(random.randrange(0, screen_height - block_size) / block_size) * block_size
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()
