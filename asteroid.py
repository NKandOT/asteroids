import random
import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        Draw = pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        move = self.velocity * dt
        self.position += move

    def split(self):
        self.kill()
        if self.radius > ASTEROID_MIN_RADIUS:
            log_event("asteroid_split")            
            direction = random.uniform(20,50)
            velo_1 = self.velocity.rotate(direction)
            velo_2 = self.velocity.rotate(-direction)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            child_1 = Asteroid(self.position[0], self.position[1], new_radius)
            child_2 = Asteroid(self.position[0], self.position[1], new_radius)
            child_1.velocity = velo_1 * 1.2
            child_2.velocity = velo_2 * 1.2
        else: return
