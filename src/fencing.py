from random import randint
import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"


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


def fencing(playername, enemyname, runaway_count=0):
    if runaway_count >= 5:
        print(f"You're now cornered, there's nowhere to run or dodge!")
        print(f"{enemyname} takes advantage of this opportunity to stab you")
        return False

    move = randint(1, 10)
    if move == 10:
        print(f"{enemyname} tries to attack you but misses! You see an opening")
        options = ["run away", "stab them"]
        response = direct_ask_question("You...", options)

        if response == "stab them":
            success = randint(1, 10)
            if success > 1:
                print(f"You successfully hit them.")
                print(f"{enemyname}'s blade hits you but has no effect as you have priority")
                return True
            else:
                print(f"By some miracle, you miss!")
                print(f"{enemyname} parries your blade and stabs you in the chest")
                return False
        else:
            return fencing(playername, enemyname, runaway_count + 1)
    elif move == 8 or move == 9:
        print(f"{enemyname} stumbles over a rock! You see a potential opening")
        options = ["run away", "stab them"]
        response = direct_ask_question("You...", options)

        if response == "stab them":
            success = randint(1, 10)
            if success > 5:
                print(f"You successfully hit {enemyname}.")
                print(f"{enemyname}'s blade hits you but has no effect as you have priority")
                return True
            else:
                print(f"Unfortunately, you miss!")
                print(f"{enemyname} parries your blade and stabs you in the chest")
                return False
        else:
            return fencing(playername, enemyname, runaway_count + 1)
    elif move == 5 or move == 6 or move == 7:
        print(f"{enemyname} is running towards you at top speed!")
        options = ["run away", "stab them", "beat their blade"]
        response = direct_ask_question("You...", options)

        if response == "stab them":
            success = randint(1, 10)
            if success > 9:
                print(f"By some miracle, you successfully land a hit.")
                print(f"{enemyname}'s blade just barely misses your face")
                return True
            else:
                print(f"You hit {enemyname} but it has no effect")
                print(f"{enemyname} stabs you in the chest")
                return False
        elif response == "beat their blade":
            success = randint(1, 10)
            if success > 7:
                print(f"You successfully beat {enemyname}'s blade away and hit them.")
                return True
            else:
                print(f"{enemyname} managed to parry your blade first")
                print(f"{enemyname} stabs you in the chest")
                return False
        else:
            return fencing(playername, enemyname, runaway_count + 1)
    else:
        print(f"{enemyname} is about to slash you!")
        options = ["run away", "parry-riposte", "counter-attack"]
        response = direct_ask_question("You...", options)

        if response == "counter-attack":
            success = randint(1, 10)
            if success > 7:
                print(f"By some miracle, you manage to pull off a sky-hook.")
                print(f"{enemyname}'s blade just barely misses your torso")
                return True
            else:
                print(f"You hit {enemyname} but it has no effect")
                print(f"{enemyname} stabs you in the chest")
                return False
        elif response == "parry-riposte":
            success = randint(1, 10)
            if success >= 5:
                print(f"You successfully parry {enemyname}'s blade away and hit them in the torso.")
                return True
            else:
                print(f"{enemyname} avoided your parry")
                print(f"{enemyname} swiftly stabs you in the chest")
                return False
        else:
            return fencing(playername, enemyname, runaway_count + 1)