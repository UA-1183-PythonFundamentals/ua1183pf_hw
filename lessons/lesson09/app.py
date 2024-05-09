import pygame
from random import randint
from pygame import Rect
pygame.init()


gameDisplay = pygame.display.set_mode((800,600))


pygame.display.set_caption('Super Puper Game')
def get_random_color():
    return (
        randint(0, 255),
        randint(0, 255),
        randint(0, 255)
    )


POINTS = []

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
# Loop until the user clicks the close button.
done = False

is_keydown = False

font = pygame.font.SysFont('Calibri', 25, True, False)

tank = [10, 10]

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
            # --- Game logic should go here
            # --- Drawing code should go here
            # First, clear the screen to white. Don't put other drawing commands
            # above this, or they will be erased with this command.
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.dict.get("pos")
            button = event.dict.get("button")
            if button == 1:
                POINTS.append(pos)
            
            elif button == 3:
                p = POINTS.pop()
        if event.type == pygame.KEYDOWN:
            key = event.dict.get("key")
            is_keydown = key

            if key == 1073741906 and tank[1] > 0:
                tank[1] -= 10
            elif key == 1073741903:
                tank[0] += 10
            elif key == 1073741905 and tank[1] < 580:
                tank[1] += 10
            elif key == 1073741904:
                tank[0] -= 10
        if event.type == pygame.KEYUP:
            is_keydown = False
    
    
    
    if is_keydown:
        if key == 1073741906 and tank[1] > 0:
            tank[1] -= 10
        elif key == 1073741903:
            tank[0] += 10
        elif key == 1073741905 and tank[1] < 580:
            tank[1] += 10
        elif key == 1073741904:
            tank[0] -= 10

    gameDisplay.fill(WHITE)


    if len(POINTS) > 2:
        # print(POINTS)
        pygame.draw.polygon(gameDisplay, get_random_color(), POINTS, width=10)

        for point in POINTS:
            text = font.render(f"({point[0]}, {point[1]})",True, BLACK)

            gameDisplay.blit(text, point)
    
    pygame.draw.rect(gameDisplay, BLACK, Rect(tank[0], tank[1], 20, 20), width=0)
    pygame.draw.rect(gameDisplay, BLACK, Rect(tank[0]+20, tank[1]+8, 10, 4), width=0)

        # --- Go ahead and update the screen with what we've drawn.
    pygame.display.update()
    # --- Limit to 60 frames per second
    clock.tick(30)