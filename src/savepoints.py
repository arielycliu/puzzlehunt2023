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
            player = b.createtrainer(PLAYER_NAME)
        case 1:
            FRIENDS = graveyard()
        case 2:
            player = piano(FRIENDS, player)  # pokemon 1: garchomp
        case 3:
            k, player = potions(FRIENDS, player)  # pokemon 2: volcarona
            FRIENDS = FRIENDS.remove(k)
            enemy = b.create_enemy(k)
        case 4:
            player = chess(FRIENDS, k)  # pokemon 3: your choice
        case 5:
            dragon(FRIENDS)
        case 6:
            bossfight(player, k)
    SAVEPOINT += 1
