import random
import os
import pygame
from pygame.constants import QUIT, K_DOWN, K_UP, K_LEFT, K_RIGHT

#Step 1. Initializing PyGame
pygame.init()
FPS = pygame.time.Clock()
HEIGHT = 800
WIDTH = 1200

FONT = pygame.font.SysFont('Verdana', 20)

COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_BLUE = (0, 0, 255)
COLOR_RED = (255, 0, 0)

# Step 2. Setting up Display Parameters
main_display = pygame.display.set_mode((WIDTH, HEIGHT))

# Loading and scaling the background image
bg = pygame.transform.scale(pygame.image.load('background.png'), (WIDTH, HEIGHT))
bgx1 = 0
bgx2 = bg.get_width()
bg_move = 3

# Setting up player image and parameters
IMAGE_PATH = "goose"
PLAYER_IMAGES = os.listdir(IMAGE_PATH)

player_size = (20, 20)

# Step 3. Setting Up player Parameters
player = pygame.transform.scale(pygame.image.load('player.png').convert_alpha(), player_size) #pygame.Surface(player_size)
player_rect = pygame.Rect(100, int(HEIGHT/2), *player_size)
player_move_down = [0, 4]
player_move_right = [4, 0]
player_move_up = [0, -4]
player_move_left = [-4, 0]

# Step 4. Function to create Enemy
def create_enemy():
    enemy = pygame.image.load('enemy.png').convert_alpha() #pygame.Surface(enemy_size)
    enemy_size = enemy.get_size()
    enemy_rect = pygame.Rect(WIDTH, random.randint(0, HEIGHT - enemy_size[1]), *enemy_size)
    enemy_move = [random.randint(-8, -4), 0]
    return [enemy, enemy_rect, enemy_move]

# Step 5. Function to create Bonus
def create_bonus():
    bonus = pygame.image.load('bonus.png').convert_alpha()
    bonus_size = bonus.get_size()
    bonus_rect = pygame.Rect(random.randint(0, WIDTH - bonus_size[1]), 0 - bonus_size[1], *bonus_size)
    bonus_move = [1, random.randint(4, 8)]
    return [bonus, bonus_rect, bonus_move]

# Step 6. Setting Up PyGame Events
CREATE_ENEMY= pygame.USEREVENT + 2
pygame.time.set_timer(CREATE_ENEMY, 1500)

CREATE_BONUS = pygame.USEREVENT + 2
pygame.time.set_timer(CREATE_BONUS, 1500)
CHANGE_IMAGE = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_IMAGE, 200)

enemies = []

bonuses = []

score = 0

image_index = 0

plaing = True

# Step 7. Main Game Loop
while plaing:
    FPS.tick(120)
    for event in pygame.event.get():
        #Step8.Handling Events
        if event.type == QUIT:
            plaing = False
        if event.type == CREATE_ENEMY:
            enemies.append(create_enemy())
        if event.type == CREATE_BONUS:
            bonuses.append(create_bonus())
        if event.type == CHANGE_IMAGE:
            player = pygame.image.load(os.path.join(IMAGE_PATH, PLAYER_IMAGES[image_index]))
            image_index +=1
            if image_index >= len(PLAYER_IMAGES):
                image_index = 0

    # Step 8. Moving Background
    bgx1 -= bg_move
    bgx2 -= bg_move

    if bgx1 < -bg.get_width():
        bgx1 = bg.get_width()

    if bgx2 < -bg.get_width():
        bgx2 = bg.get_width()

    main_display.blit(bg, (bgx1, 0))
    main_display.blit(bg, (bgx2, 0))

    keys = pygame.key.get_pressed()
    # Step 10. Player Movement
    if keys[K_DOWN] and player_rect.bottom < HEIGHT:
        player_rect = player_rect.move(player_move_down)

    if keys[K_RIGHT] and player_rect.right < WIDTH:
        player_rect = player_rect.move(player_move_right)

    if keys[K_UP] and player_rect.top > 0:
        player_rect = player_rect.move(player_move_up)

    if keys[K_LEFT] and player_rect.left > 0:
        player_rect = player_rect.move(player_move_left)

    for enemy in enemies:
        enemy[1] = enemy[1].move(enemy[2])
        main_display.blit(enemy[0], enemy[1])
        if player_rect.colliderect(enemy[1]):
            plaing = False

    # Step 11. Updating Enemy and Bonus Positions
    for bonus in bonuses:
        bonus[1] = bonus[1].move(bonus[2])
        main_display.blit(bonus[0], bonus[1])
        if player_rect.colliderect(bonus[1]):
            score += 1
            bonuses.pop(bonuses.index(bonus))
#Step10. Rendering
    main_display.blit(FONT.render(str(score), True, COLOR_WHITE), (WIDTH-50, 20))
    main_display.blit(player, player_rect)


    pygame.display.flip()
 # Step 11. Cleaning Up
    for enemy in enemies:
        if enemy[1].left < 0:
            enemies.pop(enemies.index(enemy))

    for bonus in bonuses:
        if bonus[1].bottom > HEIGHT:
            bonuses.pop(bonuses.index(bonus))


