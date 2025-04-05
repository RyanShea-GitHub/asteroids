import pygame
from constants import *    
from player import Player
from asteroid import Asteroid
from asteroidsfield import AsteroidField
from circleshape import *

def main():  
    pygame.init()
    time = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()


    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    AsteroidField()
  
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)

        screen.fill("black")
         
        for sprite in drawable:
            sprite.draw(screen)
        
        pygame.display.flip()

        dt = time.tick(60) / 1000
        print(f"dt: {dt}")
        print(f"rotation: {player.rotation}")
        print(updatable, drawable)

 
if __name__ == "__main__":
    main()
        

