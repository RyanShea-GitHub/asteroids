import pygame
from constants import *    
from player import *
from circleshape import *

def main():  
    pygame.init()
    time = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
  
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)    
        screen.fill("black")
        drawable.draw(screen)
        
        pygame.display.flip()

        dt = time.tick(60) / 1000
        print(f"dt: {dt}")
        print(f"rotation: {player.rotation}")

 
if __name__ == "__main__":
    main()
        

