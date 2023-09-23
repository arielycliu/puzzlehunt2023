from util.poke.pokebattle.player import PokemonTrainer
from util.poke.pokebattle.pokeworld import pokemonWorld
from util.poke.pokebattle.pokemon import Pokemon
from util.poke.pokebattle.citys_and_game import pokemon_duel
from copy import deepcopy


def printpokemon(player):
    for pokemon in player.pokemonInHand:
        pokemon.printPokemon()
    print("Current pokemon: ", end="")
    player.currentPokemon.printPokemon()


def print_options():
    count = 0
    for pokemon in pokemonWorld:
        if count >= 9:
            print(pokemon, end=", \n")
            count = 0
        else:
            print(pokemon, end=", ")
            count += 1


def check_pokemon(pokemon):
    if pokemon in pokemonWorld:
        return True
    else:
        return False


def createtrainer(name):
    player = PokemonTrainer(name)
    return player


def add_pokemon(pokemon_name, player, switchcur=False):
    pokedata = deepcopy(pokemonWorld[pokemon_name])
    playerPokemon = Pokemon(pokemon_name, pokedata, 12)
    player.pokemonInHand.append(playerPokemon)
    if switchcur:
        player.currentPokemon = playerPokemon
    return player


def create_enemy(enemyname):
    raichu = deepcopy(pokemonWorld['raichu-alola'])
    raichu = Pokemon('raichu-alola', raichu, level=0)
    raichu.npcPokemonReady(maxlevel=15)

    umbreon = deepcopy(pokemonWorld['umbreon'])
    umbreon = Pokemon('umbreon', umbreon, level=0)
    umbreon.npcPokemonReady(maxlevel=7)

    Enemy = PokemonTrainer(enemyname, kind='npc', money=1000, startingPokemons=[raichu, umbreon])
    Enemy.currentPokemon = raichu
    return Enemy


def duel(player, enemy):
    winner, player = pokemon_duel(player, enemy, battle='duel')
    print(f"{winner} wins!")
    return winner



