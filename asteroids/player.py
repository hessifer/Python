import pygame
from pygame import Vector2

from circleshape import CircleShape
from constants import PLAYER_RADIUS as PR

class Player(CircleShape):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        super().__init__(self.x, self.y, PR)
        self.rotation: int = 0

    def triangle(self):
        forward: Vector2 = pygame.Vector2(0, 1).rotate(self.rotation)
        right: Vector2 = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a: Vector2 = self.position + forward * self.radius
        b: Vector2 = self.position - forward * self.radius - right
        c: Vector2 = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen: pygame.display):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)