'''
This file keeps all of the constant variables in one
place.
PyLint demands that I put all globals in uppercase.
'''
import pygame


# Display properties
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

# Create a display surface
GAME_DISPLAY = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

# Get the backgroun
BACKGROUND = pygame.Surface((GAME_DISPLAY.get_width(), GAME_DISPLAY.get_height()))

# Create a clock
CLOCK = pygame.time.Clock()


# Color hex values
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
ALPHA_COLOR = (255, 0, 195) # Pink background color for transparency

# String constants
GAME_NAME = 'Our Python Game'
FONT = "freesansbold.ttf"

# Image constants
PLAYER_SPRITE_WIDTH = 32
PLAYER_SPRITE_HEIGHT = 32

# Gameplay constants
SPRITE_BASE_SPEED = 5

# Sprite paths
S_PLAYER = "resources/sprites/s_player.png"