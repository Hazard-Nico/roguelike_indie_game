# player.py

import pygame
from settings import TILE_SIZE, RED, SCREEN_WIDTH, SCREEN_HEIGHT

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(RED)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.vel_y = 0
        self.speed = 5
        self.jump_power = -15
        self.on_ground = False
        self.on_ladder = False
        self.health = 100
        self.max_health = 100

    def update(self, tiles, ladders, destructibles, items, jump_pressed):
        keys = pygame.key.get_pressed()
        dx = 0
        dy = 0

        if keys[pygame.K_LEFT]:
            dx = -self.speed
        if keys[pygame.K_RIGHT]:
            dx = self.speed

        # Ladder check
        self.on_ladder = False
        for ladder in ladders:
            if self.rect.colliderect(ladder.rect):
                self.on_ladder = True
                break

        if self.on_ladder:
            self.vel_y = 0
            if keys[pygame.K_UP]:
                dy = -self.speed
            if keys[pygame.K_DOWN]:
                dy = self.speed
        else:
            self.vel_y += 1
            if self.vel_y > 10:
                self.vel_y = 10
            dy += self.vel_y

        # Collision with platforms
        self.on_ground = False
        self.rect.x += dx
        for tile in tiles:
            if self.rect.colliderect(tile.rect):
                if dx > 0:
                    self.rect.right = tile.rect.left
                if dx < 0:
                    self.rect.left = tile.rect.right

        self.rect.y += dy
        for tile in tiles:
            if self.rect.colliderect(tile.rect):
                if dy > 0:
                    self.rect.bottom = tile.rect.top
                    self.vel_y = 0
                    self.on_ground = True
                if dy < 0:
                    self.rect.top = tile.rect.bottom
                    self.vel_y = 0

        if jump_pressed and not self.on_ladder and self.on_ground:
            self.vel_y = self.jump_power

        # Destructible interaction
        if keys[pygame.K_e]:
            for obj in destructibles:
                if self.rect.colliderect(obj.rect):
                    obj.take_damage()

        # Item pickup
        for item in items:
            if self.rect.colliderect(item.rect):
                self.apply_item_effect(item)
                item.kill()

        # Keep player within screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.on_ground = True

    def apply_item_effect(self, item):
        if item.item_type == "health":
            self.health = min(self.max_health, self.health + item.amount)
        elif item.item_type == "speed":
            self.speed += item.amount