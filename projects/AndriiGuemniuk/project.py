import pygame as pg
from random import randrange

pg.init()

WINDOW = 750
TILE_SIZE = 45
RANGE = (TILE_SIZE // 2, WINDOW - TILE_SIZE // 2, TILE_SIZE)
get_random_position = lambda: [randrange(int(TILE_SIZE // 2), int(WINDOW - TILE_SIZE // 2), int(TILE_SIZE)) for _ in range(2)]

# reset
def reset_game():
    snake = pg.rect.Rect(0, 0, TILE_SIZE - 2, TILE_SIZE - 2)
    snake.center = get_random_position()
    food = pg.rect.Rect(0, 0, TILE_SIZE - 2, TILE_SIZE - 2)
    food.center = get_random_position()
    return snake, [snake.copy()], 1, food, (0, 0), {pg.K_UP: 1, pg.K_DOWN: 1, pg.K_LEFT: 1, pg.K_RIGHT: 1}

# quit
def game_over():
    screen.fill('black')
    font = pg.font.Font(None, 46)
    text = font.render("Game Over", True, 'red')
    screen.blit(text, (WINDOW // 2 - text.get_width() // 2, WINDOW // 2 - text.get_height() // 2 - 10))
    text = font.render("Press C to Continue or Q to Quit", True, 'white')
    screen.blit(text, (WINDOW // 2 - text.get_width() // 2, WINDOW // 2 - text.get_height() // 2 + 10))
    pg.display.flip()
    pg.time.wait(500)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_q:
                    pg.quit()
                    exit()
                if event.key == pg.K_c:
                    return


# screen
screen, clock = pg.display.set_mode([WINDOW, WINDOW]), pg.time.Clock()
snake, segments, length, food, snake_dir, dirs = reset_game()
time, time_step = 0, 110

# main
while True:
    keys = {pg.K_UP: (0, -TILE_SIZE, {pg.K_UP: 1, pg.K_DOWN: 0, pg.K_LEFT: 1, pg.K_RIGHT: 1}),
            pg.K_DOWN: (0, TILE_SIZE, {pg.K_UP: 0, pg.K_DOWN: 1, pg.K_LEFT: 1, pg.K_RIGHT: 1}),
            pg.K_LEFT: (-TILE_SIZE, 0, {pg.K_UP: 1, pg.K_DOWN: 1, pg.K_LEFT: 1, pg.K_RIGHT: 0}),
            pg.K_RIGHT: (TILE_SIZE, 0, {pg.K_UP: 1, pg.K_DOWN: 1, pg.K_LEFT: 0, pg.K_RIGHT: 1})}
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        if event.type == pg.KEYDOWN and event.key in keys and dirs[event.key]:
            snake_dir, dirs = keys[event.key][:2], keys[event.key][2]

    screen.fill('black')

    # check borders and selfeating
    if snake.left < 0 or snake.right > WINDOW or snake.top < 0 or snake.bottom > WINDOW or pg.Rect.collidelist(snake, segments[ :-1]) != -1:
        game_over()
        snake, segments, length, food, snake_dir, dirs = reset_game()

    # check food touch
    if snake.center == food.center:
        food.center = get_random_position()
        length += 1

    # check food
    pg.draw.rect(screen, 'red', food)
    [pg.draw.rect(screen, 'green', segment) for segment in segments]

    # move snale
    time_now = pg.time.get_ticks()
    if time_now - time > time_step:
        time = time_now
        snake.move_ip(snake_dir)
        segments.append(snake.copy())
        segments = segments[-length:]

    pg.display.flip()
    clock.tick(60)
