import pygame
from pygame import Vector2


class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x: float, y: float, radius: float):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position: Vector2 = pygame.Vector2(x, y)
        self.velocity: Vector2 = pygame.Vector2(0, 0)
        self.radius: float = radius

    def draw(self, screen: pygame.Surface):
        # to be overridden by subclass
        pass

    def update(self, dt: float):
        # to be overridden by subclass
        pass