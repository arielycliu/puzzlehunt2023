from util import helper_functions as hp


def graveyard():
    data = hp.get_dialogue_json("../dialogue/grave_d.json")
    dialogue = data["text"]


graveyard()
