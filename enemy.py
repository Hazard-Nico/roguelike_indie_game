# enemy.py

import pygame
import random
from settings import TILE_SIZE, PURPLE

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(PURPLE)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 2
        self.direction = random.choice(["left", "right"])
        self.move_counter = 0
        self.move_threshold = 60
        self.health = 3
        self.aggro_range = TILE_SIZE * 5  # 5 tiles

    def update(self, tiles, player):
        # AI: Chase player if close, else patrol
        distance_x = player.rect.centerx - self.rect.centerx
        distance_y = player.rect.centery - self.rect.centery
        abs_distance = abs(distance_x)

        old_x = self.rect.x

        if abs_distance < self.aggro_range and abs(distance_y) < TILE_SIZE * 2:
            # Chase player horizontally
            if distance_x > 0:
                self.rect.x += self.speed
                self.direction = "right"
            elif distance_x < 0:
                self.rect.x -= self.speed
                self.direction = "left"
        else:
            # Patrol
            dx = self.speed if self.direction == "right" else -self.speed
            self.rect.x += dx

        # Collision with tiles
        for tile in tiles:
            if self.rect.colliderect(tile.rect):
                self.rect.x = old_x
                self.direction = "left" if self.direction == "right" else "right"
                break

        # Occasionally change direction if not chasing
        if abs_distance >= self.aggro_range:
            self.move_counter += 1
            if self.move_counter >= self.move_threshold:
                self.direction = "left" if self.direction == "right" else "right"
                self.move_counter = 0

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.kill()