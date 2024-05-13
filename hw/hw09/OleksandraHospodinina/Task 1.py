import pygame
import random


pygame.init()

WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT = pygame.font.Font(None, 36)
TARGET_NUMBER = random.randint(1, 100)
TRIES = 10

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Guess the Number")

def draw_text(text, x, y):
    surface = FONT.render(text, True, BLACK)
    screen.blit(surface, (x, y))

def game():
    attempts = 0
    input_box = pygame.Rect(250, 200, 140, 32)
    input_text = ''
    clock = pygame.time.Clock()

    while True:
        screen.fill(WHITE)
        draw_text("Guess the Number (1-100)", 250, 50)
        draw_text("Attempts left: {}".format(TRIES - attempts), 250, 100)
        pygame.draw.rect(screen, BLACK, input_box, 2)
        draw_text(input_text, input_box.x + 5, input_box.y + 5)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

                if event.key == pygame.K_RETURN:
                    try:
                        guess = int(input_text)
                        attempts += 1
                        if guess < TARGET_NUMBER:
                            draw_text("The guessed number is higher!", 250, 250)
                        elif guess > TARGET_NUMBER:
                            draw_text("the guessed number is less!", 250, 250)
                        else:
                            draw_text("You guessed!", 150, 250)
                            pygame.display.flip()
                            pygame.time.wait(60)
                            return
                        if attempts == TRIES:
                            draw_text("Out of attempts! The number was {}.".format(TARGET_NUMBER), 150, 250)
                            pygame.display.flip()
                            pygame.time.wait(60)
                            return
                    except ValueError:
                        draw_text("Invalid input! Please enter a number.", 150, 250)
                if event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

        pygame.display.flip()
        clock.tick(60)


game()
