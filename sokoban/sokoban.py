"""
sokoban

note:
"
ni mende belum siap, 
nak map screen pun taktau lagi. 
akan diupdate dari masa ke semasa
"
- weldan, may 10, 2013
"""
import events
import windows
import game

"""
run game
"""
def main():
    window = windows.sokoban_windows((400, 300), "Sokoban")
    window.create() 

    while True:
        sokoban_events = events.sokoban_events()
        sokoban_events.listen()

if __name__ == "__main__":
    main()
