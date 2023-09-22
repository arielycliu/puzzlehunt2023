# https://github.com/hiimvincent/poke-battle-sim
# https://github.com/Sahil-k1509/cmd_pokemon
# https://github.com/nicolaslindbloomairey/pokemon-python

import poke_battle_sim as pb
pikachu = pb.Pokemon(name_or_id="Pikachu", ivs=[15, 15, 15], moves=["charm", "growl", "nuzzle", "leer"], gender="male", level=1)
ash = pb.Trainer('Ash', [pikachu])

starmie = pb.Pokemon(...)
misty = pb.Trainer('Misty', [starmie])

battle = pb.Battle(ashe, misty)
battle.start()
battle.turn()

print(battle.get_all_text())