from util import helper_functions as hp
import art
import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

def intro():
    data = hp.get_dialogue_json("../dialogue/intro_d.json")
    blurbs = data["text"]
    print("Welcome to Dreamscape")
    for blurb in blurbs:
        if blurb["type"] == "dialogue":
            hp.print_text(blurb)
        elif blurb["type"] == "question_name":
            player_name = hp.ask_question(blurb)
            print(f"Welcome {player_name}")
        elif blurb["type"] == "question":
            response = hp.ask_question(blurb)
            if response == "yes":
                hp.tutorial()
            else:
                print("Alright, let's get started...")
                input(" ~ ")
                break

    print("")
    art.tprint("Dreamscape", "colossal")
    print("")
    return player_name


if __name__ == '__main__':
    intro()