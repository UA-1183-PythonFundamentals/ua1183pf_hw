import pygame

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Screen dimensions (adjust these as needed)
WIDTH = 800
HEIGHT = 600

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rectangle Movement")

# Define the rectangle (adjust position and size)
rect_x = 100
rect_y = 100
rect_width = 50
rect_height = 50
rect = pygame.Rect(rect_x, rect_y, rect_width, rect_height)

# Movement speed
speed = 5

# Game loop
running = True
while running:
  # Handle events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

    # Handle key presses (optional for movement control)
    # if event.type == pygame.KEYDOWN:
    #   # Add logic for movement based on key presses (e.g., arrow keys)
    #     pass

  # Check for boundary collisions with the rectangle
  if rect.left < 0:
    rect.left = 0  # Clamp the left edge to 0
  elif rect.right > WIDTH:
    rect.right = WIDTH  # Clamp the right edge to the screen width

  if rect.top < 0:
    rect.top = 0  # Clamp the top edge to 0
  elif rect.bottom > HEIGHT:
    rect.bottom = HEIGHT  # Clamp the bottom edge to the screen height

  # Fill the screen with black
  screen.fill(BLACK)

  # Draw the rectangle
  pygame.draw.rect(screen, WHITE, rect)

  # Update the display
  pygame.display.flip()

# Quit Pygame
pygame.quit()