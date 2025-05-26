# main.py

import pygame
import sys
from settings import *
from level import create_level, LEVEL_WIDTH, LEVEL_HEIGHT
from player import Player
from enemy import Enemy
from camera import Camera

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

tiles, ladders, destructibles, items, enemy_positions = create_level()
player = Player(100, 100)
enemies = pygame.sprite.Group()
for pos in enemy_positions:
    enemies.add(Enemy(*pos))
all_sprites = pygame.sprite.Group(player)
camera = Camera(LEVEL_WIDTH, LEVEL_HEIGHT)

def game_loop():
    running = True
    while running:
        jump_pressed = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    jump_pressed = True

        player.update(tiles, ladders, destructibles, items, jump_pressed)
        for enemy in enemies:
            enemy.update(tiles, player)
        camera.update(player)
        
        # Player attacks enemy (press F)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_f]:
            for enemy in enemies:
                if player.rect.colliderect(enemy.rect):
                    enemy.take_damage(1)

        # Player picks up item
        for item in items:
            if player.rect.colliderect(item.rect):
                item.kill()  # Remove item
                # You can add inventory logic here
        
        # Enemy attacks player
        for enemy in enemies:
            if player.rect.colliderect(enemy.rect):
                # Add a cooldown or invincibility timer for fairness!
                player.health -= 1
                if player.health <= 0:
                    running = False

        # Draw background
        screen.fill(SKY)

        # Draw level with camera offset
        for tile in tiles:
            screen.blit(tile.image, camera.apply(tile))
        for ladder in ladders:
            screen.blit(ladder.image, camera.apply(ladder))
        for obj in destructibles:
            screen.blit(obj.image, camera.apply(obj))
        for sprite in all_sprites:
            screen.blit(sprite.image, camera.apply(sprite))
        for item in items:
            screen.blit(item.image, camera.apply(item))
        for enemy in enemies:
            screen.blit(enemy.image, camera.apply(enemy))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    game_loop()