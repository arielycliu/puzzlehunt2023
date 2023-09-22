from util import helper_functions as hp
import art
import random
import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"


def direct_dialogue(message, friend_name=None, wait=True):
    if friend_name:
        message = friend_name + ": " + message
    print(message)
    if wait:
        input(" ~ ")


def dragon(friendnames):
    print("")
    art.tprint("The Dragon Den", "small")
    print("")
    data = hp.get_dialogue_json("../dialogue/dragon_d.json")
    blurbs = data["text"]
    for blurb in blurbs:
        if blurb["type"] == "dialogue":
            hp.print_text(blurb)
        elif blurb["type"] == "friend_dialogue":
            hp.friend_print_text(blurb, random.choice(friendnames))
    return


if __name__ == '__main__':
    friendnames = ["Richard", "Sam"]
    dragon(friendnames)


