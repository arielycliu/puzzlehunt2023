from time import sleep
from random import randint


def pprint(*args, **kwargs):
    print('\t\t', *args, **kwargs)


def pokemon_duel(player, opponent, battle='wild'):
    battleOver = False
    
    if battle != 'wild': opp = opponent.name + "'s"
    else: opp = 'wild'
    
    while not battleOver:
        
        if battle != 'wild': opponent.currentPokemon.displayStats(trainer=opp)
        else: opponent.displayStats(trainer=opp)
        # pprint()
        player.currentPokemon.displayStats()
        
        pprint('\n')
        pprint("(F)ight"); sleep(0.1)
        pprint("(S)witch pokemon"); sleep(0.1)

        invalid = True
        while invalid:
            pprint("What would you like to do? ")
            pprint(" > ", end="")
            whatTodo = input()

            if whatTodo.lower() in ['s', 'f']: break
            else: pprint("Invalid option, try again...")
            
        if whatTodo in ['s', 'S']:
            if not player.switchPokemon():
                battleOver = True
                pprint();
                pprint("You lost...")
                pprint("Press Enter to Continue", end=' ');     input()
                return (opponent.name, player)

        i = 0
        attackInd = randint(0, len(opponent.currentPokemon.attacks)-i-1)
        while opponent.currentPokemon.attacks[attackInd] is None:
            attackInd = randint(0, len(opponent.currentPokemon.attacks)-i-1)
            i+=1
        attackOpp = opponent.currentPokemon.attacks[attackInd]

        if whatTodo not in ['f', 'F']:
            opponent.currentPokemon.attack(player.currentPokemon, attackInd)
            if player.currentPokemon.health <= 0:
                pprint(f"{player.currentPokemon.name} fainted..."); sleep(0.3)
                if not player.switchPokemon():
                    pprint();
                    pprint("You lost...")
                    pprint("Press Enter to Continue", end=' ');
                    input()
                    return (opponent.name, player)

        else:
            pprint("Choose Your Attack: ", end=' '); sleep(0.2)
            attackpl = int(input()) - 1
            while True:
                if attackpl not in [0, 1, 2, 3]:
                    sleep(0.2)
                    pprint("Invalid choice... Choose again : ", end='')
                    attackpl = int(input())-1
                elif player.currentPokemon.attacks[attackpl] is None:
                    sleep(0.2)
                    pprint("You haven't learnt any attack for that slot... Choose again: ", end='')
                    attackpl = int(input())-1
                elif player.currentPokemon.attacks[attackpl].count == 0:
                    sleep(0.2)
                    pprint("You can't use that attack anymore... Choose again: ", end='')
                    attackpl = int(input())-1
                else:
                    sleep(0.2)
                    break

            attackplayer = player.currentPokemon.attacks[attackpl]
            if attackplayer.name == 'quick attack' and attackOpp.name != 'quick attack':
                player.currentPokemon.attack(opponent.currentPokemon, attackpl)
                sleep(0.2)
                if opponent.currentPokemon.health > 0:
                    opponent.currentPokemon.attack(player.currentPokemon, attackInd)

                if player.currentPokemon.health <= 0:
                    pprint(f"{player.currentPokemon.name} fainted..."); sleep(1)
                    if not player.switchPokemon():
                        pprint();
                        pprint("You lost...")
                        pprint("Press Enter to Continue", end=' ');
                        input()
                        return (opponent.name, player)

            elif attackplayer.name != 'quick attack' and attackOpp.name == 'quick attack':
                opponent.currentPokemon.attack(player.currentPokemon, attackInd)
                sleep(0.2)

                if player.currentPokemon.health > 0:
                    player.currentPokemon.attack(opponent.currentPokemon, attackpl)

                if player.currentPokemon.health <= 0:
                    pprint(f"{player.currentPokemon.name} fainted..."); sleep(1)
                    if not player.switchPokemon():
                        pprint();
                        pprint("You lost...")
                        pprint("Press Enter to Continue", end=' ');
                        input()
                        return (opponent.name, player)

            else:
                if player.currentPokemon.speed >= opponent.currentPokemon.speed:
                    player.currentPokemon.attack(opponent.currentPokemon, attackpl)
                    sleep(0.2)
                    if opponent.currentPokemon.health > 0:
                        opponent.currentPokemon.attack(player.currentPokemon, attackInd)

                    if player.currentPokemon.health <= 0:
                        pprint(f"{player.currentPokemon.name} fainted..."); sleep(1)
                        if not player.switchPokemon():
                            pprint();
                            pprint("You lost...")
                            pprint("Press Enter to Continue", end=' ');
                            input()
                            return (opponent.name, player)
                else:
                    opponent.currentPokemon.attack(player.currentPokemon, attackInd)
                    sleep(0.2)
                    if player.currentPokemon.health > 0:
                        player.currentPokemon.attack(opponent.currentPokemon, attackpl)

                    if player.currentPokemon.health <= 0:
                        pprint(f"{player.currentPokemon.name} fainted..."); sleep(1)
                        if not player.switchPokemon():
                            pprint();
                            pprint("You lost...")
                            pprint("Press Enter to Continue", end=' ');
                            input()
                            return (opponent.name, player)

        if opponent.currentPokemon.health <= 0:
            sleep(0.2)
            pprint(f"{opponent.name}'s {opponent.currentPokemon.name} fainted")
            # player.currentPokemon.gain_exp(opponent.currentPokemon, battletype=battle); sleep(0.2)
            if not opponent.switchPokemon():
                sleep(0.2)
                pprint("You won the battle!\n"); sleep(0.2)
                battleOver = True
                pprint("Press Enter to Continue", end=' ');
                input()
                return (player.name, player)
        sleep(0.2)

