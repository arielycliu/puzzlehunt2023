from util import helper_functions as hp
import art
import random
from util.poke import poke_display as ph
from util.poke.pokebattle import battle as b
import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"


def bonus_puzzle(player):
    bonus_data = hp.get_dialogue_json("../dialogue/chess_d_bonus.json")
    puzzle = bonus_data["bonus_puzzle"]
    hp.answer_puzzle(puzzle)
    pokemon_question = bonus_data["pokemon_question"]
    hp.print_text(pokemon_question)
    print("Here's what I have: ")
    b.print_options()
    pokemon_name = ph.get_name()
    b.add_pokemon(pokemon_name, player, False)
    print("-" * 100)
    print(f"{pokemon_name} acquired!")
    print("-" * 100)
    b.printpokemon(player)
    print("-" * 100)
    return player


def chess(friendnames, player):
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
            if response == "any other options?":
                print("Old man: Yes but you have to earn it. Solve the bonus puzzle and I’ll give you one. ")
                input(" ~ ")
                player = bonus_puzzle(player)
            elif response == "no":
                print("Old man: suit yourself...youngsters nowadays sure are full of themselves huh")
            else:
                print("Alright, I like your enthusiasm - good choice!")
                # ph.display("audino")
                b.add_pokemon("audino", player, False)
                print("-" * 100)
                print(f"Audino Acquired!")
                print("-" * 100)
                b.printpokemon(player)
                print("-" * 100)
        elif blurb["type"] == "puzzle":
            hp.answer_puzzle(blurb)
    return player


if __name__ == '__main__':
    player = b.createtrainer("Richard")
    bonus_puzzle(player)
    b.add_pokemon("garchomp", player, True)
    b.add_pokemon("volcarona", player, False)
    friendnames = ["Janice", "Samuel"]
    chess(friendnames, player)



