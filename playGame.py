import sys
from ui import UI

def start():
    sys.stdout.write("\033[;1m")
    inpt = None
    print('What size to be the board? ')
    while inpt == None:
        try:
            inpt = int(input(": "))
        except Exception as e:
            print(e)
            inpt = None
    ui = UI(inpt)
    ui.gameUI()

start()