import pygame
import os   # importing os to handle paths for assets

pygame.init()

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My First Game")
WHITE = (255, 255, 255)
FPS = 60
VELOCITY = 5


YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    YELLOW_SPACESHIP_IMAGE, (55, 40)), 90)   # resizing image
RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    RED_SPACESHIP_IMAGE, (55, 40)), 270)


def window_draw(red, yellow):
    WIN.fill(WHITE)
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))  # drawing a surface onto the screen (text or image)
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    pygame.display.update()


def handle_yellow_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a]:  # (wasd keys)
        yellow.x -= VELOCITY
    if keys_pressed[pygame.K_d]:
        yellow.x += VELOCITY
    if keys_pressed[pygame.K_w]:
        yellow.y -= VELOCITY
    if keys_pressed[pygame.K_s]:
        yellow.y += VELOCITY


def handle_red_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT]:  # (wasd keys)
        red.x -= VELOCITY
    if keys_pressed[pygame.K_RIGHT]:
        red.x += VELOCITY
    if keys_pressed[pygame.K_UP]:
        red.y -= VELOCITY
    if keys_pressed[pygame.K_DOWN]:
        red.y += VELOCITY


def main():
    red = pygame.Rect(700, 300, 55, 40)
    yellow = pygame.Rect(100, 300, 55, 40)
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        handle_yellow_movement(keys_pressed, yellow)
        handle_red_movement(keys_pressed, red)
        window_draw(red, yellow)
    pygame.quit()


if __name__ == "__main__":
    main()

