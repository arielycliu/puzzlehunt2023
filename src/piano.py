from util import helper_functions as hp
import art
import random


def piano(friendnames):
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
        elif blurb["type"] == "question":
            hp.ask_question(blurb)
        elif blurb["type"] == "puzzle":
            hp.answer_puzzle(blurb)
    return

friendnames = ["Richard", "Alex", "Sam"]

piano(friendnames)


