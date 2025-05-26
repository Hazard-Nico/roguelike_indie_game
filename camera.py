# camera.py

import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

class Camera:
    def __init__(self, width, height):
        self.camera_rect = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, target):
        # Offset a rect or sprite by the camera position
        return target.rect.move(-self.camera_rect.x, -self.camera_rect.y)

    def update(self, target):
        # Center the camera on the target
        x = target.rect.centerx - SCREEN_WIDTH // 2
        y = target.rect.centery - SCREEN_HEIGHT // 2

        # Clamp the camera so it doesn't go outside the level
        x = max(0, min(x, self.width - SCREEN_WIDTH))
        y = max(0, min(y, self.height - SCREEN_HEIGHT))

        self.camera_rect = pygame.Rect(x, y, SCREEN_WIDTH, SCREEN_HEIGHT)