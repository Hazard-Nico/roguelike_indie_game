# level.py

import pygame
import random
from settings import TILE_SIZE, BROWN, YELLOW, ORANGE, PURPLE, CYAN, MAGENTA

LEVEL_WIDTH_TILES = 36
LEVEL_HEIGHT_TILES = 12

ITEM_EFFECTS = {
    "health": {"color": CYAN, "effect": "health", "amount": 20},
    "speed": {"color": MAGENTA, "effect": "speed", "amount": 2}
}

def generate_random_level():
    level = []
    for row in range(LEVEL_HEIGHT_TILES):
        if row == 0 or row == LEVEL_HEIGHT_TILES - 1:
            level.append("1" * LEVEL_WIDTH_TILES)
        else:
            row_str = ""
            for col in range(LEVEL_WIDTH_TILES):
                if col == 0 or col == LEVEL_WIDTH_TILES - 1:
                    row_str += "1"
                else:
                    r = random.random()
                    if r < 0.05:
                        row_str += "L"
                    elif r < 0.10:
                        row_str += "D"
                    elif r < 0.13:
                        row_str += "I"  # Generic item
                    elif r < 0.16:
                        row_str += "E"
                    elif r < 0.30 and row > 2:
                        row_str += "1"
                    else:
                        row_str += "0"
            level.append(row_str)
    return level

LEVEL_MAP = generate_random_level()
LEVEL_WIDTH = len(LEVEL_MAP[0]) * TILE_SIZE
LEVEL_HEIGHT = len(LEVEL_MAP) * TILE_SIZE

class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(BROWN)
        self.rect = self.image.get_rect(topleft=(x, y))

class Ladder(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect(topleft=(x, y))

class Destructible(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(ORANGE)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.health = 3

    def take_damage(self):
        self.health -= 1
        if self.health <= 0:
            self.kill()

class Item(pygame.sprite.Sprite):
    def __init__(self, x, y, item_type="health"):  # Default to health item
        super().__init__()
        self.item_type = item_type
        self.color = ITEM_EFFECTS[item_type]["color"]
        self.effect = ITEM_EFFECTS[item_type]["effect"]
        self.amount = ITEM_EFFECTS[item_type]["amount"]  # Add this line
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(self.color)
        self.rect = self.image.get_rect(topleft=(x, y))

def create_level():
    tiles = pygame.sprite.Group()
    ladders = pygame.sprite.Group()
    destructibles = pygame.sprite.Group()
    items = pygame.sprite.Group()
    enemy_positions = []
    for row_idx, row in enumerate(LEVEL_MAP):
        for col_idx, cell in enumerate(row):
            x = col_idx * TILE_SIZE
            y = row_idx * TILE_SIZE
            if cell == "1":
                tiles.add(Tile(x, y))
            elif cell == "L":
                ladders.add(Ladder(x, y))
            elif cell == "D":
                destructibles.add(Destructible(x, y))
            elif cell == "I":
                # Randomly choose an item type
                item_type = random.choice(list(ITEM_EFFECTS.keys()))
                items.add(Item(x, y, item_type))
            elif cell == "E":
                enemy_positions.append((x, y))
    return tiles, ladders, destructibles, items, enemy_positions