import pygame, sys, random

pygame.init()

gameDisplay = pygame.display.set_mode((1280,800))

pygame.display.set_caption('Project Pong')

clock = pygame.time.Clock()

done = False

score_font = pygame.font.Font(None, 100)

player_score = 0
ai_score = 0

ball_speed_x = 6
ball_speed_y = 6
player_speed = 0
ai_speed = 6

def reset():
    global ball_speed_x, ball_speed_y
    ball.x = 640
    ball.y = random.randint(10, 100)
    ball_speed_x *= random.choice([-1, 1])
    ball_speed_y *= random.choice([-1, 1])


def ai_movement():
    global ai_speed
    ai.y += ai_speed
    

    if ball.centery <= ai.centery:
        ai_speed = -6
    if ball.centery >= ai.centery:
        ai_speed = 6
    
    if ai.top <= 0:
        ai.top = 0
    
    if ai.bottom >= 800:
        ai.bottom = 800

def player_movement():
    player.y += player_speed

    if player.top <= 0:
        player.top = 0
    
    if player.bottom >= 800:
        player.bottom = 800


def ball_movement():
    global ball_speed_x, ball_speed_y, ai_score, player_score
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.bottom >= 800:
        ball_speed_y *= -1

    if ball.top <= 0:
        ball_speed_y *= -1
    
    if ball.right >= 1280:
        ai_score += 1
        reset()

    if ball.left <= 0:
        player_score += 1
        reset()

    if ball.colliderect(player) or ball.colliderect(ai):
        ball_speed_x *= -1

ball = pygame.Rect(0, 0, 30, 30)
ball.center = (640, 400)

ai = pygame.Rect(0, 0, 20, 100)
ai.centery = (400)

player = pygame.Rect(0, 0, 20, 100)
player.midright = (1280, 400)


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_speed = -6
            if event.key == pygame.K_DOWN:
                player_speed = 6
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_speed = 0
            if event.key == pygame.K_DOWN:
                player_speed = 0

    

    ball_movement()
    player_movement()
    ai_movement()


    gameDisplay.fill('black')
    ai_scoreboard = score_font.render(str(ai_score), True, 'white')
    player_scoreboard = score_font.render(str(player_score), True, 'white')
    gameDisplay.blit(ai_scoreboard,(320, 20))
    gameDisplay.blit(player_scoreboard,(960, 20))
    pygame.draw.aaline(gameDisplay, 'white', (640, 0), (640, 800))
    pygame.draw.ellipse(gameDisplay, 'white', ball)
    pygame.draw.rect(gameDisplay, 'white', ai)
    pygame.draw.rect(gameDisplay, 'white', player)


    pygame.display.update()

    clock.tick(60)