from util import helper_functions as hp
import art
player_name = None


def intro():
    data = hp.get_dialogue_json("../dialogue/intro_d.json")
    blurbs = data["text"]
    for blurb in blurbs:
        if blurb["type"] == "dialogue":
            message = blurb["message"] if blurb["speaker"] == "narrator" else blurb["speaker"] + ": " + blurb["message"]
            hp.print_text(message, wait=False)
        elif blurb["type"] == "question_name":
            question = blurb["message"]
            options = blurb["options"]
            player_name = hp.ask_question(question, options)
            print(f"Welcome {player_name}")
        elif blurb["type"] == "question":
            question = blurb["message"]
            options = blurb["options"]
            response = hp.ask_question(question, options)
            if response == "yes":
                hp.tutorial()
            else:
                print("Alright, let's get started...")

    print("")
    art.tprint("Dreamscape", "colossal")
    print("")

