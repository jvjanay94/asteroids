import pygame
import random
from circleshape import CircleShape
from constants import *
from logger import log_state, log_event

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        log_event("asteroid_split")
        random_angle = random.uniform(20, 50)
        
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        f_piece = Asteroid(self.position.x, self.position.y, new_radius)
        s_piece = Asteroid(self.position.x, self.position.y, new_radius)
        
        f_piece.velocity = self.velocity.rotate(random_angle) * 1.2
        s_piece.velocity = self.velocity.rotate(-random_angle) * 1.2
        



