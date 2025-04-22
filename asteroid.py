import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else: 
            rand_angle = random.uniform(20, 50)
            rotation1 = self.velocity.rotate(rand_angle)
            rotation2 = self.velocity.rotate(-rand_angle)
            new_rad = self.radius - ASTEROID_MIN_RADIUS

            ast1 = Asteroid(self.position.x, self.position.y, new_rad)
            ast2 = Asteroid(self.position.x, self.position.y, new_rad)
            ast1.velocity = rotation1 * 1.2
            ast2.velocity = rotation2




