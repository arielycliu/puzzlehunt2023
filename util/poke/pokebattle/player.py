from time import sleep


def pprint(*args, **kwargs):
    print('\t\t', *args, **kwargs)
    

class PokemonTrainer(object):
    
    def __init__(self, name, currentLocation='Pallet Town', kind='player', startingPokemons=[], pokemonLimit=7, pokeballs=2, money=300, *args, **kwargs):
        self.name = name
        self.kind = kind
        self.pokemonInHand = startingPokemons
        self.pokemonLimit = pokemonLimit
        self.archivePokemons = []
        self.currentPokemon = None
        self.pokeballs = pokeballs
        self.currentLocation = currentLocation
        self.items = {}
        self.badges = []
        self.money = money
        
        
    def switchPokemon(self):
        if self.kind == 'player':
            pprint("Your Pokemons: ")
            sleep(0.2)
            nonzerohp = 0
            for index, pokemon in enumerate(self.pokemonInHand):
                pprint(index+1, end=') ')
                pokemon.printPokemon()
                if pokemon.health > 0: nonzerohp+=1
                sleep(0.2)
                
            pprint(f"Current Pokemon:"); sleep(0.2)
            self.currentPokemon.printPokemon()
            sleep(1)
            
            if nonzerohp == 0: return False
            chosen = False
            while not chosen:
                newCurrentPoke = int(input("\t\tWhich pokemon would you like to choose as current Pokemon? "))-1
                if 0 <= newCurrentPoke < len(self.pokemonInHand):
                    if self.pokemonInHand[newCurrentPoke].health > 0:
                        self.currentPokemon = self.pokemonInHand[newCurrentPoke]
                        pprint(f"You chose {self.currentPokemon.name}"); sleep(0.2)
                        chosen = True
                    else:
                        pprint(f"{self.pokemonInHand[newCurrentPoke].name}'s health is zero. You can't chose it"); sleep(0.2)
                else:
                    pprint(f"That is not a valid number. Please choose between 1 and {len(self.pokemonInHand)}"); sleep(0.2)
            
            return True        
        else:
            indexOfCurrent = self.pokemonInHand.index(self.currentPokemon)
            if indexOfCurrent == self.pokemonLimit - 1: return False
            
            self.currentPokemon = self.pokemonInHand[(indexOfCurrent+1)%len(self.pokemonInHand)]
            if self.currentPokemon.health <= 0: return False
        
            pprint(f"{self.name} Chose {self.currentPokemon.name}"); sleep(0.1)
            return True
            
    def healAllpoke(self):
        sleep(0.1)
        if self.kind == 'player':
            pprint("All your pokemons have been healed..."); sleep(0.2)
        for pokemon in self.pokemonInHand:
            pokemon.visitPokemonCentre()