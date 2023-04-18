import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 400
window_height = 400
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("GUI-Snake")

# Define the colors used in the game
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Set up the snake and food
snake_block_size = 10
snake_speed = 15
font_style = pygame.font.SysFont(None, 30)

def snake(snake_block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, black, [x[0], x[1], snake_block_size, snake_block_size])

def message(msg, color):
    message = font_style.render(msg, True, color)
    window.blit(message, [window_width / 6, window_height / 3])

def gameLoop():
    game_over = False
    game_close = False

    blue = (0, 0, 255)
    yellow = (255, 255, 102)

    x1 = window_width / 2
    y1 = window_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, window_width - snake_block_size) / 10.0) * 10.0
    foody = round(random.randrange(0, window_height - snake_block_size) / 10.0) * 10.0

    # Start the game loop
    while not game_over:
        while game_close == True:
            window.fill(white)
            message("You lost! Q to Quit / C to Play Again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block_size
                    x1_change = 0

        if x1 >= window_width or x1 < 0 or y1 >= window_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        window.fill(blue)

        pygame.draw.rect(window, yellow, [foodx, foody, snake_block_size, snake_block_size])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)

        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        snake(snake_block_size, snake_List)
        pygame.display.update()

        # Check for collision with the food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, window_width - snake_block_size) / 10.0) * 10.0
            foody = round(random.randrange(0, window_height - snake_block_size) / 10.0) * 10.0
            Length_of_snake += 1

        # Set the snake speed
        clock = pygame.time.Clock()
        clock.tick(snake_speed)

    # Quit Pygame and exit the program
    pygame.quit()
    quit()

gameLoop()
