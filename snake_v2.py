import pygame
import random

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Game variables
clock = pygame.time.Clock()
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
food_pos = [random.randrange(1, (WIDTH//10)) * 10, random.randrange(1, (HEIGHT//10)) * 10]
food_spawn = True
direction = 'RIGHT'
change_to = direction
speed = 15

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Control snake direction
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            elif event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            elif event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            elif event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # Ensure the snake can't move in the opposite direction
    if change_to == 'UP' and not direction == 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and not direction == 'LEFT':
        direction = 'RIGHT'

    # Move the snake
    if direction == 'UP':
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10
    if direction == 'RIGHT':
        snake_pos[0] += 10

    # Snake body growing mechanism
    snake_body.insert(0, list(snake_pos))
    if snake_pos == food_pos:
        food_spawn = False
    else:
        snake_body.pop()

    if not food_spawn:
        food_pos = [random.randrange(1, (WIDTH//10)) * 10, random.randrange(1, (HEIGHT//10)) * 10]
    food_spawn = True

    # Game over conditions
    if snake_pos[0] < 0 or snake_pos[0] > (WIDTH-10) or snake_pos[1] < 0 or snake_pos[1] > (HEIGHT-10):
        running = False

    for block in snake_body[1:]:
        if snake_pos == block:
            running = False

    # Fill screen
    screen.fill(BLACK)

    # Draw the snake
    for pos in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))

    # Draw the food
    pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    # Refresh game screen
    pygame.display.update()

    # Frame Per Second /Refresh Rate
    clock.tick(speed)

pygame.quit()
