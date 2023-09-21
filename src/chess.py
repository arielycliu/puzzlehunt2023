from util import helper_functions as hp
import art
import random


def chess(friendnames, k):
    bonus = False
    print("")
    art.tprint("Fields of Valour", "small")
    print("")
    data = hp.get_dialogue_json("../dialogue/chess_d.json")
    blurbs = data["text"]
    for blurb in blurbs:
        if blurb["type"] == "dialogue":
            hp.print_text(blurb)
        elif blurb["type"] == "friend_dialogue":
            hp.friend_print_text(blurb, random.choice(friendnames))
        elif blurb["type"] == "question":
            response = hp.ask_question(blurb)
            if response == "Got any other Pokemon options?":
                bonus = True
        elif blurb["type"] == "puzzle":
            hp.answer_puzzle(blurb)
        elif blurb["type"] == "bonus_puzzle" and bonus == True:
            hp.answer_puzzle(blurb)
        elif blurb["type"] == "pokemon_question" and bonus == True:
            response = hp.ask_question(blurb)
    return


if __name__ == '__main__':
    friendnames = ["Richard", "Alex"]
    k = "Jackie"
    chess(friendnames, k)


