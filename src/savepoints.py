from src.intro import intro
from src.graveyard import graveyard
from piano import piano
# from potions import potions
# from chess import chess
# from dragon import dragon
from bossfight import bossfight
import random
SAVEPOINT = 0
PLAYER_NAME = ""
FRIENDS = []

while True:
    match SAVEPOINT:
        case 0:
            PLAYER_NAME = intro()
        case 1:
            FRIENDS = graveyard()
            k = random.choice(FRIENDS)
        case 2:
            piano()
        case 3:
            potions()
        case 4:
            chess()
        case 5:
            dragon()
        case 6:
            bossfight()
    SAVEPOINT += 1
