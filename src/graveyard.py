from util import helper_functions as hp
import art


def graveyard():
    # print("")
    # art.tprint("Friendly Graveyard", "small")
    # print("")
    friend_names = []
    data = hp.get_dialogue_json("../dialogue/grave_d.json")
    blurbs = data["text"]
    for blurb in blurbs:
        if blurb["type"] == "dialogue":
            hp.print_text(blurb)
        elif blurb["type"] == "friend_question":
            friend_names.append(hp.ask_question(blurb))
        elif blurb["type"] == "question":
            hp.ask_question(blurb)
        elif blurb["type"] == "puzzle":
            hp.answer_puzzle(blurb)
    return friend_names


if __name__ == '__main__':
    graveyard()


