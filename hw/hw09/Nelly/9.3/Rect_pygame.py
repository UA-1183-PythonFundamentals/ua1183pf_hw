import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Move Rectangle Game")

# Set up colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Set up rectangle properties
rect_width = 50
rect_height = 50
rect_x = (screen_width - rect_width) // 2
rect_y = (screen_height - rect_height) // 2
rect_speed = 5

# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key press handling
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        rect_x = max(0, rect_x - rect_speed)
    if keys[pygame.K_RIGHT]:
        rect_x = min(screen_width - rect_width, rect_x + rect_speed)
    if keys[pygame.K_UP]:
        rect_y = max(0, rect_y - rect_speed)
    if keys[pygame.K_DOWN]:
        rect_y = min(screen_height - rect_height, rect_y + rect_speed)

    # Fill the background with white
    screen.fill(WHITE)

    # Draw the rectangle
    pygame.draw.rect(screen, BLUE, (rect_x, rect_y, rect_width, rect_height))

    # Update the display
    pygame.display.update()

    # Control the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit()