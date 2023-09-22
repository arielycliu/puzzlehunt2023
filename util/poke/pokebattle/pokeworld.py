from util.poke.pokebattle.attacklist import *


def deepcopy(actualAttack):
    if not actualAttack: return actualAttack
    newattack = Attack(actualAttack.name, actualAttack.attCategory, actualAttack.baseDamage, actualAttack.pLevel, actualAttack.maxcount, heal=actualAttack.heal, accuracy=actualAttack.accuracy, recoil=actualAttack.recoil)
    return newattack

small_pokemons = ['pikachu', 'charmander', 'squirtle', 'bulbasaur', 'caterpie', 'weedle', 'pidgey', 'ekans', 
                  'sandshrew', 'nidoran', 'clefairy', 'vulpix', 'jigglypuff', 'zubat',  'diglett', 'meowth', 'psyduck',  
                  'growlithe', 'abra', 'geodude', 'shellder', 'gastly', 'onix', 'cubone', 'koffing', 'horsea', 'staryu', 'scyther', 'magmar', 'magikarp', 
                  'eevee']

medium_pokemons = ['raichu', 'charmeleon', 'wartortle', 'ivysaur', 'metapod', 'kakuna', 'pidgeotto', 'arbok', 'sandslash', 
                   'nidorina', 'nidorino', 'clefable', 'ninetales',  'golbat',  'dugtrio', 
                   'persian', 'golduck',  'arcanine', 'kadabra', 'graveler', 'cloyster', 'haunter', 'weezing', 'marowak', 'seadra', 'starmie', 
                   'gyarados', 'vaporeon', 'jolteon', 'flareon']

large_pokemons = ['charizard', 'blastoise', 'venusaur', 'butterfree', 'beedrill', 'pidgeot', 'nidoqueen', 'nidoking', 'alakazam',  'gengar']

legendary_pokemons = ['zapdos', 'moltres', 'articuno', 'selmon jong un']



pokemonWorld = {
    'umbreon':     {'type': 'dark',      'evolveAt': None,   'evolveTo': None,           'baseDef': 110,  'baseSpeed': 65, 'startAttacks': [(growl), (bite), (swift), (tackle)],                       'learnableAttacks': [(quickattack), (thunderbolt), (agility), (irontail), (thunderpunch), (discharge), (bolttackle), (electroball), (catastropika)][::-1]       },

    'garchomp':     {'type': 'electric',      'evolveAt': None,   'evolveTo': None,           'baseDef': 95,  'baseSpeed': 102, 'startAttacks': [(earthquake), (stoneedge), (fireblast), (firefang)],                       'learnableAttacks': [(dig), (quickattack), (scratch), (mudslap)][::-1]       },
    'raichu-alola':     {'type': 'electric',      'evolveAt': None,   'evolveTo': None,           'baseDef': 50,  'baseSpeed': 110, 'startAttacks': [(thunderbolt), (psyshock), (tackle), (quickattack)],                       'learnableAttacks': [(quickattack), (thunderbolt), (agility), (irontail), (thunderpunch), (discharge), (bolttackle), (electroball), (catastropika)][::-1]       },
    'volcarona':     {'type': 'fire',      'evolveAt': None,   'evolveTo': None,           'baseDef': 65,  'baseSpeed': 100, 'startAttacks': [(flamethrower), (bugbuzz), (roost), (fireblast)],                       'learnableAttacks': [(quickattack), (thunderbolt), (agility), (irontail), (thunderpunch), (discharge), (bolttackle), (electroball), (catastropika)][::-1]       },
    'dragonite':     {'type': 'flying',      'evolveAt': None,   'evolveTo': None,           'baseDef': 95,  'baseSpeed': 80, 'startAttacks': [(fly), (earthquake), (airslash), (blizzard)],                       'learnableAttacks': [(quickattack), (thunderbolt), (agility), (irontail), (thunderpunch), (discharge), (bolttackle), (electroball), (catastropika)][::-1]       },
    'lugia':     {'type': 'psychic',      'evolveAt': None,   'evolveTo': None,           'baseDef': 130,  'baseSpeed': 110, 'startAttacks': [(roost), (whirlwind), (psychic), (icebeam)],                       'learnableAttacks': [(quickattack), (thunderbolt), (agility), (irontail), (thunderpunch), (discharge), (bolttackle), (electroball), (catastropika)][::-1]       },

    'pikachu':      {'type': 'electric',    'evolveAt': None,   'evolveTo': 'raichu',       'baseDef': 10,  'baseSpeed': 30, 'startAttacks': [(thundershock), (tackle), (electroball), (hyperbeam)],                'learnableAttacks': [(quickattack), (thunderbolt), (agility), (irontail), (thunderpunch), (discharge), (bolttackle), (electroball), (catastropika)][::-1]       },
    'charmander':   {'type': 'fire',        'evolveAt': 18,     'evolveTo': 'charmeleon',   'baseDef': 15,  'baseSpeed': 20, 'startAttacks': [(ember), (tackle), (flamethrower), (quickattack)],                     'learnableAttacks': [(swift), (flamethrower), (firepunch), (firespin), (shelltrap), (fireblast), (sacredfire)][::-1]       },
    'squirtle':     {'type': 'water',       'evolveAt': 18,     'evolveTo': 'wartortle',    'baseDef': 24,  'baseSpeed': 21, 'startAttacks': [(watergun), (tackle), (hydrovortex), (waterspout)],                    'learnableAttacks': [(headbutt), (bubblebeam), (mudslap), (hydropump), (watercannon), (hydrovortex)][::-1]         },
    'bulbasaur':    {'type': 'grass',       'evolveAt': 18,     'evolveTo': 'ivysaur',      'baseDef': 15,  'baseSpeed': 20, 'startAttacks': [(razorleaf), (tackle), None, None],                   'learnableAttacks': [(vinewhip), (disable), (stunspore), (gigadrain), (frenzy), (leafblade), (solarbeam)][::-1]         },           
    'oddish':       {'type': 'grass',       'evolveAt': 18,     'evolveTo': 'gloom',        'baseDef': 13,  'baseSpeed': 15, 'startAttacks': [(razorleaf), (tackle), None, None],                   'learnableAttacks': [(vinewhip), (quickattack), (stunspore), (leafblade), (solarbeam)][::-1]         },           
    'caterpie':     {'type': 'bug',         'evolveAt': 7,      'evolveTo': 'metapod',      'baseDef': 5,   'baseSpeed': 13, 'startAttacks': [(stringshot), (bugbite), (leechlife), None],  'learnableAttacks': [(tackle), (harden), (gust), (whirlwind), (wingattack)][::-1]        },           
    'weedle':       {'type': 'bug',         'evolveAt': 7,      'evolveTo': 'kakuna',       'baseDef': 5,   'baseSpeed': 13, 'startAttacks': [(poisonsting), (bugbite), (stinger), None],   'learnableAttacks': [(tackle), (poisonpowder), (gust), (leechlife), (wingattack)][::-1]        },           
    'pidgey':       {'type': 'flying',      'evolveAt': 16,     'evolveTo': 'pidgeotto',    'baseDef': 12,  'baseSpeed': 23, 'startAttacks': [(quickattack), (gust), None, None],                   'learnableAttacks': [(whirlwind), (agility), (sandattack), (wingattack), (fly), (aerialace), (airslash), (aeroblast)][::-1]       },           
    'ekans':        {'type': 'poison',      'evolveAt': 14,     'evolveTo': 'arbok',        'baseDef': 14,  'baseSpeed': 21, 'startAttacks': [(acid), (poisonsting), None, None],                   'learnableAttacks': [(poisonpowder), (quickattack), (tailwhip), (agility), (leechlife), (poisonfang), (gunkshot)][::-1]       },           
    'sandshrew':    {'type': 'ground',      'evolveAt': 18,     'evolveTo': 'sandslash',    'baseDef': 30,  'baseSpeed': 18, 'startAttacks': [(sandattack), (tackle), None, None],                  'learnableAttacks': [(dig), (quickattack), (scratch), (mudslap)][::-1]       },           
    'nidoran':      {'type': 'poison',      'evolveAt': 15,     'evolveTo': None,           'baseDef': 13,  'baseSpeed': 15, 'startAttacks': [(tackle), (poisonsting), None, None],                 'learnableAttacks': [(sandattack), (quickattack), (bite), (agility), (headbutt), (megahorn), (acid), (hyperbeam), (icebeam), (icepunch), (thunderbolt), (earthquake)][::-1]        },           
    'clefairy':     {'type': 'normal',      'evolveAt': None,   'evolveTo': None,           'baseDef': 19,  'baseSpeed': 16, 'startAttacks': [(growl), (pound), None, None],                        'learnableAttacks': [(sing)][::-1]        },           
    'vulpix':       {'type': 'fire',        'evolveAt': 18,     'evolveTo': 'ninetales',    'baseDef': 18,  'baseSpeed': 19, 'startAttacks': [(tackle), (ember), None, None],                       'learnableAttacks': [(flamethrower), (quickattack), (headbutt), (firespin), (scratch), (bite), (fireblast)][::-1]         },           
    'jigglypuff':   {'type': 'psychic',     'evolveAt': None,   'evolveTo': None,           'baseDef': 13,  'baseSpeed': 20, 'startAttacks': [(pound), (sing), None, None],                         'learnableAttacks': [(tackle), (heal), (headbutt), (infactuate), (cut), (curse), (ironpunch), (hyperbeam)][::-1]         },           
    'zubat':        {'type': 'flying',      'evolveAt': 14,     'evolveTo': 'golbat',       'baseDef': 14,  'baseSpeed': 23, 'startAttacks': [(poisonsting), (whirlwind), None, None],              'learnableAttacks': [(wingattack), (airslash), (quickattack), (poisonfang), (stinger)][::-1]        },           
    'diglett':      {'type': 'ground',      'evolveAt': 18,     'evolveTo': 'dugtrio',      'baseDef': 19,  'baseSpeed': 21, 'startAttacks': [(sandattack), (dig), None, None],                     'learnableAttacks': [(mudslap), (cut), (rockthrow), (headsmash), (stoneedge), (earthquake), (landwrath)][::-1]        },           
    'meowth':       {'type': 'normal',      'evolveAt': 18,     'evolveTo': 'persian',      'baseDef': 18,  'baseSpeed': 21, 'startAttacks': [(scratch), (tackle), (tailwhip), None],       'learnableAttacks': [(agility), (quickattack), (sandattack), (irontail), (bite), (feintattack), (hyperbeam)][::-1]      },           
    'psyduck':      {'type': 'water',       'evolveAt': 18,     'evolveTo': 'golduck',      'baseDef': 17,  'baseSpeed': 11, 'startAttacks': [(watergun), (tackle), None, None],                    'learnableAttacks': [(scratch), (bubblebeam), (agility), (psybeam), (confusion), (heal), (psyshock), (hyperbeam)][::-1]      },           
    'growlithe':    {'type': 'fire',        'evolveAt': 18,     'evolveTo': 'arcanine',     'baseDef': 19,  'baseSpeed': 23, 'startAttacks': [(tackle), (bite), None, None],                        'learnableAttacks': [(firespin), (scratch), (howl), (quickattack), (agility), (flamethrower), (sacredfire)][::-1]       },           
    'abra':         {'type': 'psychic',     'evolveAt': 12,     'evolveTo': 'kadabra',      'baseDef': 19,  'baseSpeed': 23, 'startAttacks': [(psybeam), (tailwhip), None, None],                   'learnableAttacks': [(disable), (heal), (irontail), (confusion), (shadowball), (dreameater), (psyshock), (futuresight)][::-1]       },           
    'geodude':      {'type': 'rock',        'evolveAt': 18,     'evolveTo': 'graveler',     'baseDef': 31,  'baseSpeed': 16, 'startAttacks': [(tackle), (rockthrow), None, None],                   'learnableAttacks': [(sandattack), (mudslap), (stoneedge), (rockwrecker), (headbutt), (headsmash), (earthquake)][::-1]         },           
    'shelldar':     {'type': 'water',       'evolveAt': 18,     'evolveTo': 'cloyster',     'baseDef': 19,  'baseSpeed': 16, 'startAttacks': [(watergun), (bubblebeam), None, None],                'learnableAttacks': [(bite), (icywind), (lick), (waterslap), (aurorabeam), (icebeam), (iceburn), (psyshock)][::-1]      },           
    'gastly':       {'type': 'ghost',       'evolveAt': 18,     'evolveTo': 'haunter',      'baseDef': 19,  'baseSpeed': 20, 'startAttacks': [(lick), (psybeam), None, None],                       'learnableAttacks': [(hide), (shadowball), (curse), (feintattack), (pursuit), (shadowpunch), (crunch), (dreameater), (futuresight)][::-1]       },           
    'onix':         {'type': 'rock',        'evolveAt': None,   'evolveTo': None,           'baseDef': 31,  'baseSpeed': 20, 'startAttacks': [(sandattack), (rockthrow), None, None],               'learnableAttacks': [(stoneedge), (irontail), (mudslap), (earthquake), (rockwrecker), (headsmash), (meteormash)][::-1]         },           
    'cubone':       {'type': 'ground',      'evolveAt': 28,     'evolveTo': 'marowak',      'baseDef': 20,  'baseSpeed': 16, 'startAttacks': [(growl), (boneclub), None, None],                     'learnableAttacks': [(tailwhip), (headbutt), (bonemerang)][::-1]         },           
    'koffing':      {'type': 'poison',      'evolveAt': 18,     'evolveTo': 'weezing',      'baseDef': 21,  'baseSpeed': 15, 'startAttacks': [(smokescreen), (tackle), None, None],                 'learnableAttacks': [(sandattack), (acid), (poisonfang), (poisonpowder), (sludgebomb), (gunkshot)][::-1]      },           
    'horsea':       {'type': 'water',       'evolveAt': 18,     'evolveTo': 'seadra',       'baseDef': 15,  'baseSpeed': 14, 'startAttacks': [(watergun), (bubblebeam), None, None],                'learnableAttacks': [(poisonsting), (waterslap), (hydropump), (watercannon), (icebeam)][::-1]         },           
    'staryu':       {'type': 'water',       'evolveAt': 16,     'evolveTo': 'starmie',      'baseDef': 13,  'baseSpeed': 15, 'startAttacks': [(watergun), (swift), None, None],                     'learnableAttacks': [(tackle), (bubblebeam), (quickattack), (hydropump), (watercannon), (waterspout), (hydrovortex)][::-1]        },           
    'scyther':      {'type': 'bug',         'evolveAt': None,   'evolveTo': None,           'baseDef': 17,  'baseSpeed': 33, 'startAttacks': [(quickattack), (cut), None, None],                    'learnableAttacks': [(agility), (razorleaf), (leechlife), (bugbite), (scratch), (stinger), (megahorn), (leafblade), (hyperbeam)][::-1]      },           
    'magmar':       {'type': 'fire',        'evolveAt': None,   'evolveTo': None,           'baseDef': 19,  'baseSpeed': 19, 'startAttacks': [(tackle), (ember), None, None],                       'learnableAttacks': [(flamethrower), (headbutt), (sandattack), (ironpunch), (firepunch), (firespin), (shelltrap), (sacredfire)][::-1]      },           
    'magikarp':     {'type': 'water',       'evolveAt': 12,     'evolveTo': 'gyarados',     'baseDef': 19,  'baseSpeed': 14, 'startAttacks': [(watergun), (swift), None, None],                     'learnableAttacks': [(tailwhip), (pound), (quickattack), (waterslap), (hydropump), (watercannon), (hydrovortex)][::-1]       },           
    'eevee':        {'type': 'normal',      'evolveAt': None,   'evolveTo': None,           'baseDef': 19,  'baseSpeed': 24, 'startAttacks': [(tackle), (swift), None, None],                       'learnableAttacks': [(quickattack), (bite), (agility), (scratch)][::-1]        }
}

for pokemon in pokemonWorld:
    startAttacks = pokemonWorld[pokemon].get('startAttacks', [])
    learnableAttacks = pokemonWorld[pokemon].get('learnableAttacks', [])
    for i in range(len(startAttacks)):
        startAttacks[i] = deepcopy(startAttacks[i])

    for i in range(len(learnableAttacks)):
        learnableAttacks[i] = deepcopy(learnableAttacks[i])

    if startAttacks:
        pokemonWorld[pokemon]['startAttacks'] = startAttacks
    if learnableAttacks:
        pokemonWorld[pokemon]['learnableAttacks'] = learnableAttacks