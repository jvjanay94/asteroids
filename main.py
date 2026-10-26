import pygame
import sys 
from constants import *
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


# or import everything: from module_name import *
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(x = SCREEN_WIDTH/2, y = SCREEN_HEIGHT/2)
    
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = (updatable,)
    aster = AsteroidField()

    shots = pygame.sprite.Group()
    Shot.containers = (shots, drawable, updatable)


    while (True):
        dt = clock.tick(60)/1000
        
        for event in pygame.event.get():
            pass
        updatable.update(dt)
        for aster in asteroids:
            if aster.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        screen.fill("black")
        for roid in asteroids:
            for sho in shots:
                if roid.collides_with(sho):
                    log_event("asteroid_shot")
                    roid.split()
                    pygame.sprite.Sprite.kill(sho)
        for drawable_sprite in drawable:
            drawable_sprite.draw(screen)
        pygame.display.flip()
        log_state()        
        print(dt)
    
    
    # print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    # print(f"Screen width: {SCREEN_WIDTH}\nScreen height: 720")

    


if __name__ == "__main__":
    main()