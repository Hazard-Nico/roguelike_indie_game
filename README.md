# Roguelike Pygame Project

Here’s a breakdown of the key elements from your screenshot (which is from Dead Cells) that you might want to replicate in your Pygame roguelike:
## Visual Style
Pixel art graphics with vibrant colors and detailed backgrounds.
Foreground platforms and walls are dark and blocky, with clear separation from the background.
Lighting effects (glows, torches, windows).
## Level Structure
Multi-level platforms (vertical and horizontal movement).
Platforms, walls, and ladders/chains for climbing.
Some destructible or interactive objects (barrels, doors, etc.).
## Player and Enemies
Player character is clearly visible, with a distinct sprite.
Enemies and effects (blood splatter, damage numbers) are shown.
## HUD/UI
Bottom left: Weapon and skill slots, with icons and button hints.
Bottom center: Health bar with current/max HP.
Bottom right: Minimap, currency, and other stats.

## 1. Project Structure
Organize your code into modules:
* `main.py` (game loop)
* `settings.py` (constants/colors)
* `player.py` (player class)
* `enemy.py` (enemy class)
* `level.py` (level generation and tiles)
* `ui.py` (HUD and UI elements)
* `assets/` (for images, sprites, sounds)
## 2. Game World
* Use a tile-based system for platforms and walls.
* Store level layout as a 2D array or load from a file.
* Implement platform collision and support for verticality (jumping, climbing).
## 3. Player & Combat
* Player sprite with animation states (idle, run, attack, jump).
* Weapon system: allow equipping and switching weapons.
* Attack mechanics: melee and ranged.
## 4. Enemies
* Enemy sprites, movement, and AI.
* Health and damage system.
## 5. UI/HUD
* Draw weapon/skill slots, health bar, and minimap.
* Show damage numbers and effects.
