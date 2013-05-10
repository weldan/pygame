"""
sokoban
"""

import lib.events as events
import lib.windows as windows
import lib.game as game

"""
run game
"""
def main():
    window = windows.sokoban_windows((800, 600), "Sokoban")
    window.create() 

    while True:
        sokoban_events = events.sokoban_events()
        sokoban_events.listen()

if __name__ == "__main__":
    main()
