import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
BLACK = (0, 0, 0)
COLORS = [
    (255, 0, 0),  # Red
    (0, 255, 0),  # Green
    (0, 0, 255),  # Blue
    (255, 255, 0),  # Yellow
    (255, 0, 255),  # Magenta
    (0, 255, 255),  # Cyan
]

# Create screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Bouncing DVD Logo")

# Load or create a "DVD" logo (you can replace this with an image)
logo_width, logo_height = 100, 50
dvd_logo = pygame.Surface((logo_width, logo_height))
dvd_logo.fill(random.choice(COLORS))
pygame.draw.rect(dvd_logo, BLACK, dvd_logo.get_rect(), 5)

# Initial position and speed
x, y = random.randint(0, SCREEN_WIDTH - logo_width), random.randint(0, SCREEN_HEIGHT - logo_height)
speed_x, speed_y = 3, 3

# Clock for controlling frame rate
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update position
    x += speed_x
    y += speed_y


    # Bounce off edges
    if x <= 0 or x + logo_width >= SCREEN_WIDTH:
        speed_x = -speed_x
        dvd_logo.fill(random.choice(COLORS))  # Change color on bounce
    if y <= 0 or y + logo_height >= SCREEN_HEIGHT:
        speed_y = -speed_y
        dvd_logo.fill(random.choice(COLORS))  # Change color on bounce

    # Draw everything
    screen.fill(BLACK)
    pygame.draw.circle(screen, (255, 0, 0), (250, 250), 50, 5)
    screen.blit(dvd_logo, (x, y))
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

pygame.quit()
