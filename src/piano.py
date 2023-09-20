from util import helper_functions as hp


def piano():
    data = hp.get_dialogue_json("../dialogue/piano_d.json")
    blurbs = data["text"]
    for blurb in blurbs:
        if blurb["type"] == "dialogue":
            hp.print_text(blurb)
        elif blurb["type"] == "question":
            hp.ask_question(blurb)
        elif blurb["type"] == "puzzle":
            hp.answer_puzzle(blurb) 
    return


piano()


