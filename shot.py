import pygame
from constants import SHOT_RADIUS
from circleshape import CircleShape

class Shot(CircleShape):

    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw (self, screen):
        Draw = pygame.draw.circle(screen, "white", self.position, self.radius, SHOT_RADIUS)

    def update(self, dt):
        move = self.velocity * dt
        self.position += move

