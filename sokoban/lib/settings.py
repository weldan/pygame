"""
settings
"""

import os

grid_setting = {
    'width': 79,
    'height': 59,
    'margin': 1,
    'colour': (255, 255, 255),
    'rowsize': 10,
    'columnsize': 10,
    'backgroundcolour': (0, 0, 0)    
}

window_setting = {
    'width': 800,
    'height': 600,
    'title': "Sokoban"
}

player_setting = {
    'image': os.path.join("data","stickmang.resized.jpg")
}
