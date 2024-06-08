import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Paddle settings
PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100
PADDLE_VELOCITY = 7

# Ball settings
BALL_RADIUS = 10
BALL_VELOCITY_X = 5
BALL_VELOCITY_Y = 5

# Font settings
FONT = pygame.font.SysFont('comicsans', 50)

# Game modes
SINGLE_PLAYER = 1
TWO_PLAYER = 2

# Player scores
player1_score = 0
player2_score = 0

# Function to draw paddles, ball, and scores
def draw(paddle1, paddle2, ball, p1_score, p2_score):
    WIN.fill(BLACK)
    pygame.draw.rect(WIN, WHITE, paddle1)
    pygame.draw.rect(WIN, WHITE, paddle2)
    pygame.draw.ellipse(WIN, WHITE, ball)
    p1_score_text = FONT.render(f"{p1_score}", 1, WHITE)
    p2_score_text = FONT.render(f"{p2_score}", 1, WHITE)
    WIN.blit(p1_score_text, (WIDTH//4 - p1_score_text.get_width()//2, 20))
    WIN.blit(p2_score_text, (3*WIDTH//4 - p2_score_text.get_width()//2, 20))
    pygame.display.update()

# Function to handle ball movement and collisions
def ball_movement(ball, ball_vel, paddle1, paddle2, scores, mode):
    global player1_score, player2_score
    ball.x += ball_vel[0]
    ball.y += ball_vel[1]

    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_vel[1] = -ball_vel[1]

    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        ball_vel[0] = -ball_vel[0]

    if ball.left <= 0:
        player2_score += 1
        ball_restart(ball, ball_vel)
    if ball.right >= WIDTH:
        player1_score += 1
        ball_restart(ball, ball_vel)

    if mode == SINGLE_PLAYER:
        paddle2_ai(ball, paddle2)

def ball_restart(ball, ball_vel):
    ball.x = WIDTH // 2 - BALL_RADIUS
    ball.y = HEIGHT // 2 - BALL_RADIUS
    ball_vel[0] = random.choice((BALL_VELOCITY_X, -BALL_VELOCITY_X))
    ball_vel[1] = random.choice((BALL_VELOCITY_Y, -BALL_VELOCITY_Y))

def paddle2_ai(ball, paddle2):
    if paddle2.centery < ball.centery:
        paddle2.y += PADDLE_VELOCITY
    if paddle2.centery > ball.centery:
        paddle2.y -= PADDLE_VELOCITY

def handle_paddle_movement(keys, paddle1, paddle2, mode):
    if keys[pygame.K_w] and paddle1.top > 0:
        paddle1.y -= PADDLE_VELOCITY
    if keys[pygame.K_s] and paddle1.bottom < HEIGHT:
        paddle1.y += PADDLE_VELOCITY

    if mode == TWO_PLAYER:
        if keys[pygame.K_UP] and paddle2.top > 0:
            paddle2.y -= PADDLE_VELOCITY
        if keys[pygame.K_DOWN] and paddle2.bottom < HEIGHT:
            paddle2.y += PADDLE_VELOCITY

# Function to display the title slides
def show_titles():
    titles = [
        "SOFTSERVE ACADEMY PRESENT",
        "PING PONG GAME",
        "written by Igor Kurilov",
        "move paddle for player1 is W and S",
        "move paddle for player2 is up and down arrows"
        "written by Igor Kurilov"
    ]
    
    for title in titles:
        WIN.fill(BLACK)
        title_text = FONT.render(title, 1, WHITE)
        WIN.blit(title_text, (WIDTH//2 - title_text.get_width()//2, HEIGHT//2 - title_text.get_height()//2))
        pygame.display.update()
        time.sleep(2)  # Display each title for 2 seconds


def main():
    global player1_score, player2_score

    # Show the titles before the game starts
    show_titles()

    # Initialize paddles and ball
    paddle1 = pygame.Rect(20, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
    paddle2 = pygame.Rect(WIDTH - 40, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
    ball = pygame.Rect(WIDTH//2 - BALL_RADIUS, HEIGHT//2 - BALL_RADIUS, BALL_RADIUS*2, BALL_RADIUS*2)
    ball_vel = [random.choice((BALL_VELOCITY_X, -BALL_VELOCITY_X)), random.choice((BALL_VELOCITY_Y, -BALL_VELOCITY_Y))]

    clock = pygame.time.Clock()
    run = True

    # Game mode selection
    mode = None
    while mode is None:
        WIN.fill(BLACK)
        mode_text = FONT.render("Press 1 for Single Player, 2 for Two Players", 1, WHITE)
        WIN.blit(mode_text, (WIDTH//2 - mode_text.get_width()//2, HEIGHT//2 - mode_text.get_height()//2))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    mode = SINGLE_PLAYER
                if event.key == pygame.K_2:
                    mode = TWO_PLAYER

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        handle_paddle_movement(keys, paddle1, paddle2, mode)
        ball_movement(ball, ball_vel, paddle1, paddle2, (player1_score, player2_score), mode)
        draw(paddle1, paddle2, ball, player1_score, player2_score)

    pygame.quit()

if __name__ == "__main__":
    main()
