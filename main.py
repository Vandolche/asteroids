import pygame
import sys

from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from circleshape import *
from shot import *


def main():
    pygame.init()
    print("Starting Asteroids!")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    delta_time = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)
    

    player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)
    field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0,0,0))
        for draw in drawable:
            draw.draw(screen)

        updatable.update(dt)
        
        for asteroid in asteroids:
            for shot in shots:
                if shot.collision(asteroid):
                    asteroid.split()
                if asteroid.collision(player):
                    print("Game over!")
                    sys.exit()

        pygame.display.flip()
        dt = delta_time.tick(60) / 1000

        



if __name__ == "__main__":
    main()
