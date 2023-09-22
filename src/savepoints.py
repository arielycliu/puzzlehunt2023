from src.intro import intro
from src.graveyard import graveyard
from piano import piano
from potions import potions
from chess import chess
from dragon import dragon
from bossfight import bossfight
from util.poke.pokebattle import battle as b
import random
SAVEPOINT = 0
PLAYER_NAME = ""
FRIENDS = []
import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

while True:
    match SAVEPOINT:
        case 0:
            PLAYER_NAME = intro()
            PLAYER = b.createtrainer(PLAYER_NAME)
        case 1:
            FRIENDS = graveyard()
        case 2:
            PLAYER = piano(FRIENDS, PLAYER)  # pokemon 1: garchomp
        case 3:
            ENEMYNAME, PLAYER = potions(FRIENDS, PLAYER)  # pokemon 2: volcarona
            FRIENDS = FRIENDS.remove(ENEMYNAME)
            ENEMY = b.create_enemy(ENEMYNAME)
        case 4:
            PLAYER = chess(FRIENDS, PLAYER_NAME)  # pokemon 3: your choice
        case 5:
            dragon(FRIENDS)
        case 6:
            bossfight(FRIENDS, PLAYER, PLAYER_NAME, ENEMY, ENEMYNAME, pokemonfight=True)
    SAVEPOINT += 1
