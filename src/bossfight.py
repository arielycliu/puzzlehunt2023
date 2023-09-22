import random
import art
from util import helper_functions as hp
from util.poke.pokebattle import battle as b
from fencing import fencing
import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"



def direct_dialogue(message, friend_name=None, wait=True):
    if friend_name:
        message = friend_name + ": " + message
    print(message)
    if wait:
        input(" ~ ")

def direct_ask_question(question, options):
    print(question)
    if options != "":
        for i in range(len(options)):
            print(f"   {i + 1}. {options[i]}")
    invalid = True
    while invalid:
        response = input("> ")
        if options == "" and response != "":
            invalid = False
        elif options == "" and response == "":
            print("Blank answers are not allowed here!")
        else:
            try:
                i = int(response)
                if i <= len(options):
                    response = options[i - 1]
            except:
                response = response.lower()
            if response in options:
                invalid = False
            else:
                print("Not an option here")
    return response


def restart(friendnames, player, playername, enemy, enemyname, pokemonfight):
    print("")
    print("You lost...")
    response = direct_ask_question("Try again?", ["yes", "no"])
    if response != "yes":
        print("I didn't raise no quitter!")
        restart(friendnames, player, playername, enemy, enemyname, pokemonfight)
    else:
        if pokemonfight:
            player.healAllpoke()
        bossfight(friendnames, player, playername, enemy, enemyname, pokemonfight)


def bossfight(friendnames, player, playername, enemy, enemyname, pokemonfight=True):
    if pokemonfight:
        print("")
        art.tprint("Fight!", "small")
        print("")
        print(f"{enemyname} pulls out two pokeballs and throws them down!")
        winner = b.duel(player, enemy)
        if winner != playername:
            restart(friendnames, player, playername, enemy, enemyname, pokemonfight)

    pokemonfight = False
    direct_dialogue("You may have won against my pokemon...", enemyname)
    direct_dialogue("But you will not win against me!", enemyname)
    print(f"{enemyname} pulls out a sabre stained with purple poison, and starts to run at you!")

    options = ["run away", "stab them"]
    response = direct_ask_question("You...", options)

    if response == "stab them":
        print(f"{enemyname} has priority, your attack has no effect")
        print("Your friends rush to your side as you bleed out")
        restart(friendnames, player, playername, enemy, enemyname, pokemonfight)
    else:
        won = fencing(playername, enemyname)
        if not won:
            restart(friendnames, player, playername, enemy, enemyname, pokemonfight)
        else:
            direct_dialogue("You won!")

            direct_dialogue("You need me alive...", enemyname)
            direct_dialogue("The treasure...", enemyname)
            direct_dialogue("You can't open it without me...", enemyname, wait=True)
            direct_dialogue(f"You hesitate, wondering if you should let {enemyname} live after all", wait=True)

            x = random.choice(friendnames)
            print(f"{x} stabs {enemyname} through the chest with a rusty sword")
            direct_dialogue(f"That's for stabbing my new girlfriend, dick", x)

            direct_dialogue("How am I supposed to open the treasure now!", playername)
            direct_dialogue("Do you really need him? Just solve the puzzle like you always do!", x)

            data = hp.get_dialogue_json("../dialogue/bossfight_d.json")
            hp.answer_puzzle(data)
            direct_dialogue("I love you too!")
            direct_dialogue("Happy Birthday Richard!!")

            print("")
            art.tprint("The End!", "colossal")
            print("")


if __name__ == '__main__':
    friendnames = ["Simon", "Vincent"]
    player = b.createtrainer("Richard")
    b.add_pokemon("garchomp", player, True)
    # b.add_pokemon("volcarona", player, False)
    k = b.create_enemy("Ryoto")
    bossfight(friendnames, player, "Richard", k, "Ryoto", False)
