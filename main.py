import pygame
import os   # importing os to handle paths for assets
pygame.font.init()

# Variables
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My First Game")
WHITE = (255, 255, 255)
FPS = 60
VELOCITY = 5
BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)
BLACK = (0, 0, 0)
BULLET_VELOCITY = 7
MAX_BULLETS = 3
YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
HEALTH_FONT = pygame.font.SysFont('comicsans', 40)

# Images
YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    YELLOW_SPACESHIP_IMAGE, (55, 40)), 90)   # resizing image
RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    RED_SPACESHIP_IMAGE, (55, 40)), 270)
SPACE = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'space.png')), (WIDTH, HEIGHT))


def window_draw(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
    WIN.blit(SPACE, (0, 0))
    pygame.draw.rect(WIN, BLACK, BORDER)
    red_health_text = HEALTH_FONT.render("Health:" + str(red_health), 1, WHITE)
    yellow_health_text = HEALTH_FONT.render("Health:" + str(yellow_health), 1, WHITE)
    WIN.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10))
    WIN.blit(yellow_health_text, (10, 10))
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))  # drawing a surface onto the screen (text or image)
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet)
    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, RED, bullet)
    pygame.display.update()


def handle_yellow_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VELOCITY > 0:  # (wasd keys)
        yellow.x -= VELOCITY
    if keys_pressed[pygame.K_d] and yellow.x + VELOCITY + yellow.width < BORDER.x:   # wont let us move past the border
        yellow.x += VELOCITY
    if keys_pressed[pygame.K_w] and yellow.y - VELOCITY > 0:
        yellow.y -= VELOCITY
    if keys_pressed[pygame.K_s] and yellow.y + VELOCITY + yellow.height < HEIGHT - 20:
        yellow.y += VELOCITY


def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x += BULLET_VELOCITY
        if red.colliderect(bullet):  # collider
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)
    for bullet in red_bullets:
        bullet.x -= BULLET_VELOCITY
        if yellow.colliderect(bullet):  # collider
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)


def handle_red_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - VELOCITY > BORDER.x + BORDER.width:  # (wasd keys)
        red.x -= VELOCITY
    if keys_pressed[pygame.K_RIGHT] and red.x + VELOCITY + red.width < WIDTH:
        red.x += VELOCITY
    if keys_pressed[pygame.K_UP] and red.y - VELOCITY > 0:
        red.y -= VELOCITY
    if keys_pressed[pygame.K_DOWN] and red.y + VELOCITY + red.height < HEIGHT - 20:
        red.y += VELOCITY


def main():
    red = pygame.Rect(700, 300, 55, 40)
    yellow = pygame.Rect(100, 300, 55, 40)
    red_bullets = []
    yellow_bullets = []
    clock = pygame.time.Clock()
    red_health = 20
    yellow_health = 20
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LALT and len(yellow_bullets) < MAX_BULLETS:
                bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2 - 2, 10, 5)
                yellow_bullets.append(bullet)
            if event.key == pygame.K_RALT and len(red_bullets) < MAX_BULLETS:
                bullet = pygame.Rect(red.x, red.y + red.height// 2 - 2, 10, 5)
                red_bullets.append(bullet)

            if event.type == RED_HIT:
                red_health -= 1

            if event.type == YELLOW_HIT:
                yellow_health -= 1

        winner_text = ""
        if red_health <= 0:
            winner_text = "Yellow Wins!"

        if yellow_health <= 0:
            winner_text = "Red Wins!"

        if winner_text != "":
            pass

        keys_pressed = pygame.key.get_pressed()
        handle_yellow_movement(keys_pressed, yellow)
        handle_red_movement(keys_pressed, red)
        handle_bullets(yellow_bullets, red_bullets, yellow, red)
        window_draw(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health)
    pygame.quit()


if __name__ == "__main__":
    main()

