import pygame
import sys

# Initialize PyGame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Shrinking Circle Outline")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Initial radius and position
radius = 100
center = (250, 250)

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill(WHITE)

    # Draw the circle outline
    if radius > 0:
        pygame.draw.circle(screen, BLUE, center, radius, 2)  # Width of 2 for outline
        radius -= 1  # Decrease the radius to shrink the circle

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(30)
