from util import helper_functions as hp
import art
import random


def direct_dialogue(message, friend_name=None, wait=True):
    if friend_name:
        message = friend_name + ": " + message
    print(message)
    if wait:
        input(" ~ ")


def potions(friendnames):
    print("")
    art.tprint("The Last Drop", "small")
    print("")
    data = hp.get_dialogue_json("../dialogue/potions_d.json")
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
        elif blurb["type"] == "plotpoint":
            k = random.choice(friendnames)
            direct_dialogue(f"{k} comes back with a drink for you and sits down across from you.", wait=False)
            direct_dialogue(f"You both take sips from your drinks, waiting for the other two to join you.")
            direct_dialogue("All of a sudden, you start to feel dizzy and you rest your head on the table.")
            direct_dialogue(f"{k} leans in looking concerned. They whisper in your ear...")
            direct_dialogue("I can't afford rent either...", friend_name=k)
            direct_dialogue("If this level of poison in your veins, you'll be dead in 10")
            direct_dialogue("In honor of our past friendship, "
                            "I’ll give you a free health potion...hidden among poison of course.")
            direct_dialogue("I also added more fiber to the ones with poison. "
                            "That way when you die, you’ll finally be able to expel picture perfect poops.")
            direct_dialogue("I guess this is goodbye...I'll see you around...")
            direct_dialogue("In the graveyard.")
    return k


if __name__ == '__main__':
    friendnames = ["Richard", "Alex", "Sam"]
    potions(friendnames)


