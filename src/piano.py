from util import helper_functions as hp
import art
import random
from util.poke import poke_display as ph
from util.poke.pokebattle import battle as b
import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

def piano(friendnames, player):
    print("")
    art.tprint("Melody Valley", "small")
    print("")
    data = hp.get_dialogue_json("../dialogue/piano_d.json")
    blurbs = data["text"]
    for blurb in blurbs:
        if blurb["type"] == "dialogue":
            hp.print_text(blurb)
        elif blurb["type"] == "friend_dialogue":
            hp.friend_print_text(blurb, random.choice(friendnames))
        elif blurb["type"] == "puzzle":
            hp.answer_puzzle(blurb)
        elif blurb["type"] == "pokemon":
            hp.print_text(blurb)
            # ph.display("garchomp")
            player = b.add_pokemon("garchomp", player, True)
            print("Garchomp acquired!")
    return player


if __name__ == '__main__':
    player = b.createtrainer("Richard")
    friendnames = ["Richard", "Alex", "Sam"]
    piano(friendnames, player)


