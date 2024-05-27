import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

WIDTH = 800
HEIGHT = 600

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rectangle Movement")

rect_x = 100
rect_y = 100
rect_width = 50
rect_height = 50
rect = pygame.Rect(rect_x, rect_y, rect_width, rect_height)

speed = 5

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  if rect.left < 0:
    rect.left = 0  
  elif rect.right > WIDTH:
    rect.right = WIDTH  
  if rect.top < 0:
    rect.top = 0  
  elif rect.bottom > HEIGHT:
    rect.bottom = HEIGHT  

  screen.fill(BLACK)

  pygame.draw.rect(screen, WHITE, rect)

  pygame.display.flip()

pygame.quit()