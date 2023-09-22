from util.poke.pokebattle.player import PokemonTrainer
from util.poke.pokebattle.pokeworld import pokemonWorld
from util.poke.pokebattle.pokemon import Pokemon
from util.poke.pokebattle.citys_and_game import pokemon_duel
from copy import deepcopy


def print_options():
    for pokemon in pokemonWorld:
        print(pokemon, end=", ")
    print("that's all I have!")

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
    playerPokemon = Pokemon(pokemon_name, pokedata, 1) # 15
    player.pokemonInHand.append(playerPokemon)
    if switchcur:
        player.currentPokemon = playerPokemon
    return player


def create_enemy(enemyname):
    raichu = deepcopy(pokemonWorld['raichu-alola'])
    raichu = Pokemon('raichu-alola', raichu, level=0)
    raichu.npcPokemonReady(maxlevel=14)

    umbreon = deepcopy(pokemonWorld['umbreon'])
    umbreon = Pokemon('umbreon', umbreon, level=0)
    umbreon.npcPokemonReady(maxlevel=13)

    Enemy = PokemonTrainer(enemyname, kind='npc', money=1000, startingPokemons=[umbreon])
    Enemy.currentPokemon = Enemy.pokemonInHand[0]
    return Enemy


def duel(player, enemy):
    winner, player = pokemon_duel(player, enemy, battle='duel')
    print(f"{winner} wins!")
    return winner
