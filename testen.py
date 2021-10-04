import sys
import pygame
import random

pygame.init()
screen = pygame.display.set_mode([600, 600])


class Settings:
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (210, 210, 210)


class Ship:
    def __init__(self):
        self.image = pygame.image.load('./SpaceInvadersShip.PNG')
        self.image_scale = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.direction = random.choice([left, right])
        self.length = 1

    def turn(self, point):
        print('t')



def handle_keys(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                ship.turn(right)
            elif event.key == pygame.K_a:
                ship.turn(left)
            elif event.key in (pygame.K_q, pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()


def run_game():
    ship = Ship()
    pygame.init()
    screen = pygame.display.set_mode((1000, 900))
    clock = pygame.time.Clock()
    pygame.display.set_caption('Alien invasion')
    bg_color = (0, 0, 0)

left = 300
right = 300
geschw = 3


go = True
    # Game
while go:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    gedrueckt = pygame.key.get_pressed()
    if gedrueckt[pygame.K_LEFT]:
        left -= geschw
    if gedrueckt[pygame.K_RIGHT]:
        right += geschw

    pygame.draw.rect(screen, (255, 255, 0), (left, right))

'''screen.fill(bg_color)
        screen.blit(ship.image_scale, (450, 650))
        pygame.display.flip()
        clock.tick(60)
        handle_keys(ship)'''

run_game()

