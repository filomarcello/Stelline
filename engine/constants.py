""" created 05/09/2016
author: marcello
version: 0.1
"""

import os

# names

GAME_NAME = 'Stelline!'


# colors

BLACK = '#000000'
WHITE = '#ffffff'


# paths

IMAGES_DIR_NAME = 'images'
IMAGES_PATH = os.path.join(os.path.dirname(os.getcwd()), IMAGES_DIR_NAME)

# space objects

MIN_PLANETS = 0
MAX_PLANETS = 15

MIN_SYSTEMS = 10
MAX_SYSTEMS = 20