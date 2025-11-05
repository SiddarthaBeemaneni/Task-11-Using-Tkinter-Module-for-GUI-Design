import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 150, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)

# Clock
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 28)

# Bird setup
bird_size = 30
bird_x = 80
bird_y = HEIGHT // 2
bird_velocity = 0
gravity = 0.6
jump_strength = -10

# Pipe setup
pipe_width = 60
pipe_gap = 150
pipe_list = []
pipe_speed = 4

# Score
score = 0

def create_pipe():
    height = random.randint(100, 400)
    top_pipe = pygame.Rect(WIDTH, 0, pipe_width, height)
    bottom_pipe = pygame.Rect(WIDTH, height + pipe_gap, pipe_width, HEIGHT)
    return top_pipe, bottom_pipe

# Add first pipe
pipe_list.extend(create_pipe())

# Game loop
running = True
while running:
    screen.fill(BLUE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Bird jump
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_velocity = jump_strength

    # Bird physics
    bird_velocity += gravity
    bird_y += bird_velocity
    bird = pygame.Rect(bird_x, int(bird_y), bird_size, bird_size)

    # Draw bird
    pygame.draw.rect(screen, RED, bird)

    # Move and draw pipes
    new_pipes = []
    for pipe in pipe_list:
        pipe.x -= pipe_speed
        if pipe.right > 0:
            new_pipes.append(pipe)
        pygame.draw.rect(screen, GREEN, pipe)

    pipe_list = new_pipes

    # Add new pipes
    if len(pipe_list) == 0 or pipe_list[-1].x < WIDTH - 200:
        pipe_list.extend(create_pipe())

    # Collision detection
    for pipe in pipe_list:
        if bird.colliderect(pipe):
            text = font.render("Game Over! Score: " + str(score), True, WHITE)
            screen.blit(text, (80, HEIGHT // 2))
            pygame.display.flip()
            pygame.time.wait(2000)
            running = False

    if bird.top <= 0 or bird.bottom >= HEIGHT:
        text = font.render("Game Over! Score: " + str(score), True, WHITE)
        screen.blit(text, (80, HEIGHT // 2))
        pygame.display.flip()
        pygame.time.wait(2000)
        running = False

    # Score update
    for pipe in pipe_list:
        if pipe.centerx == bird_x:
            score += 0.5  # +0.5 twice (top and bottom) → +1 total

    # Display score
    text = font.render("Score: " + str(int(score)), True, WHITE)
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
