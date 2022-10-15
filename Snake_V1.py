# Snake Game in Python
# Version 1

# Import necessary libraries
import pygame
import time
import random

# Initialize pygame engine
pygame.init()

# Set RGB values
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Set display width and height
dis_width = 600
dis_height = 600

# Pygame display
dis = pygame.display.set_mode((dis_width, dis_height)) # Set display height and width
pygame.display.set_caption('Snake Game') # Set title

# Set clock object
clock = pygame.time.Clock()

# Set block size
snake_block = 10

# Set snake size
snake_speed = 15

# Set needed font and size styles
font_style = pygame.font.SysFont(None,30)
score_font = pygame.font.SysFont(None,35)

# Define function to display your score
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])

# Define Function to draw current snake
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])

# Display message function - use after losing
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 5, dis_height / 2])

# Game loop function
def gameLoop():
    game_over = False
    game_close = False

    # Set relevant game coordinates and values and defaults
    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    # Starting snake length
    snake_List = [] # Used for drawing
    Length_of_snake = 1

    # Food coordinates
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            dis.fill(black)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            # Detect if q or c is typed
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        # Detect and iterate game events
        for event in pygame.event.get():
            # Detect if game is quit
            if event.type == pygame.QUIT:
                game_over = True

            # Detect key presses and update direction
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Detect if snake went off screen, and quit if it is
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        # Update snake coordinates
        x1 += x1_change
        y1 += y1_change

        # Set background as black
        dis.fill(black)

        # Draw snake food
        pygame.draw.rect(dis, blue, [foodx, foody, snake_block, snake_block])

        # Define snake head and add to list
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)

        # Make sure lengths are equal
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # Quit game if you turn in on yourself
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        # Draw snake from function defined above
        our_snake(snake_block, snake_List)

        # Print Score
        Your_score(Length_of_snake - 1)

        # Update display
        pygame.display.update()

        # Detect if food is eaten by snake
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        # Line up FPS with snake speed
        clock.tick(snake_speed)

    # Un-initialize pygame and quit program
    pygame.quit()
    quit()

# Run game loop function
gameLoop()
