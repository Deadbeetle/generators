from plants import Plant
from sys import argv

def main(*args):
    for arg in args:
        if arg == "plant":
            print(Plant(), "\n")

if __name__ == "__main__":
    main(*argv[1:])