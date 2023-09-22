from math import floor, log10
from random import random, randint
from time import sleep
from util.poke.pokebattle.pokemonStrengthChart import typeAdantages, typeDisadantages


def pprint(*args, **kwargs):
    print('\t\t', *args, **kwargs)


class Pokemon(object):
	__slots__ = 'name', 'categories', 'level', 'health', 'maxHealth', 'experience', 'nextLevelAt', 'attacks', 'learnableAttacks', 'defence', 'speed', 'evolveAt', 'evolveTo', 'newAttackAt', 'basedef', 'baseSpeed'
	experienceChart = [0] + [5 + 2 * (i + 1) ** 2 for i in range(100)]
	learningCheckpoints = [2, 7, 10, 15, 18, 23, 30, 39, 46, 55, 60, 64, 67, 72, 78, 89, 95, 100]

	def __init__(self, name, pokedata, level=0, *args, **kwargs):
		self.name = name
		self.newAttackAt = 0
		self.categories = pokedata['type']
		self.level = level
		self.maxHealth = 15 + floor(log10(self.level * 23 + 1) * self.level ** 1.7)
		self.health = self.maxHealth
		self.basedef = pokedata['baseDef']
		self.baseSpeed = pokedata['baseSpeed']
		self.defence = pokedata['baseDef']
		self.speed = pokedata['baseSpeed']
		self.evolveAt = pokedata['evolveAt']
		self.evolveTo = pokedata['evolveTo']
		self.experience = 0
		self.nextLevelAt = self.experienceChart[self.level + 1]
		self.attacks = pokedata['startAttacks'][:]
		self.learnableAttacks = pokedata['learnableAttacks'][:]

	def attack(self, enemyPokemon, attackUsedInd):
		attackUsed = self.attacks[attackUsedInd]
		pprint()
		pprint(f"{self.name} used {attackUsed.name}")
		sleep(0.2)
		attackType = attackUsed.attCategory
		enemyType = enemyPokemon.categories

		chanceToMiss = random()
		if attackUsed.name == 'agility':
			if self.speed < self.baseSpeed + 10:
				self.speed += floor(random()*2 + random()*1)
				pprint(f"{self.name}'s speed increased to {self.speed}"); sleep(0.2)
			else:
				pprint("Can't increase speed anymore at this level..."); sleep(0.2)
		elif attackUsed.name == 'howl':
			if chanceToMiss < attackUsed.accuracy:
				initialHealth = enemyPokemon.health
				enemyPokemon.health -= 0.95*enemyPokemon.health
				enemyPokemon.health = max(0, enemyPokemon.health)
				pprint(f"Health reduced by {initialHealth - enemyPokemon.health}"); sleep(0.2)
			else:
				pprint(f"{self.name} missed..."); sleep(0.2)
		elif attackUsed.name == 'harden':
			if self.defence < self.basedef + 9:
				self.defence += floor(random()*2 + random()*1)
				pprint(f"{self.name}'s defence increased to {self.defence}"); sleep(0.2)	
			else:
				pprint("Can't increase defence anymore at this level..."); sleep(0.2)

		elif chanceToMiss < attackUsed.accuracy:

			if attackUsed.name != 'Heal':
				criticalChance = random()
				initialHealth = enemyPokemon.health

				if criticalChance >= 0.92:
					pprint("Critical Hit...")
					sleep(0.2)
					enemyPokemon.health -= floor((0.3+random()*0.2)*attackUsed.damage)

				if enemyType in typeAdantages[attackType]:
					pprint("It's Super Effective !!")
					sleep(0.2)
					enemyPokemon.health -= floor((0.6+random()*0.8)*attackUsed.damage)

				elif enemyType in typeDisadantages[attackType]:
					pprint("It's not very effective !!")
					sleep(0.2)
					enemyPokemon.health += floor((0.2+random()*0.5)*attackUsed.damage)

				enemyPokemon.health -= floor(attackUsed.damage*((2.71823)**(-0.0056*enemyPokemon.defence)))
				enemyPokemon.health = max(0, enemyPokemon.health)
				pprint(f"Health reduced by {initialHealth - enemyPokemon.health}")

				if attackUsed.recoil != 0:
					sleep(0.2)
					pprint(f"{self.name} got a recoil of {-floor(attackUsed.recoil)}"); sleep(0.2)
					self.health += floor(attackUsed.recoil)
					self.health = max(0, self.health)
     
				if attackUsed.heal != 0:
					sleep(0.2)
					self.health = min(self.maxHealth, self.health + attackUsed.heal)
					pprint(f"{self.name} healed some portion of it's health..."); sleep(0.2)

			else:
				self.health = min(self.maxHealth, self.health + attackUsed.heal)
				pprint(f"{self.name} healed some portion of it's health..."); sleep(0.2)

		else:
			pprint(f"{self.name} missed...\n"); sleep(0.2)
		self.attacks[attackUsedInd].count -= 1

	def printPokemon(self):
		pprint(f"Name: {self.name}\tLevel: {self.level}\tHP: {self.health}/{self.maxHealth}"); sleep(0.1)
	
	
	def displayStats(self, trainer="player's", detailed=False):
		if trainer == "player's":
			pprint(f"+---------------------------------------------+"); sleep(0.1);
			pprint(f"{trainer} {self.name}"); sleep(0.1)
			pprint(f"Type: {self.categories}"); sleep(0.1)
			pprint(f"Level: {self.level}"); sleep(0.1)
			pprint(f"Health: {self.health}/{self.maxHealth}"); sleep(0.1)
			pprint(f"Defense: {self.defence}"); sleep(0.1)
			pprint(f"Speed: {self.speed}"); sleep(0.1)
			# pprint(f"Experience: {self.experience}/{self.nextLevelAt}"); sleep(0.3)
			pprint(f"Attacks: ");
			i=0
			for attack in self.attacks:
				if attack != None:
					pprint(f"{i+1}) {attack.name:20} :  {attack.count} left"); sleep(0.1)
					if detailed: 
						pprint()
						attack.printAttack()
						pprint()
				else:
					pprint(f"{i+1}) {attack}")
				i+=1
				sleep(0.4)
			pprint()
			pprint(f"+---------------------------------------------+"); sleep(0.2); pprint()
		else:
			pprint(f"+---------------------------------------------+"); sleep(0.1); pprint()
			pprint(f"{trainer} {self.name}"); sleep(0.1)
			pprint(f"Type: {self.categories}")
			sleep(0.1)
			pprint(f"Level: {self.level}")
			sleep(0.1)
			pprint(f"Health: {self.health}/{self.maxHealth}")
			sleep(0.1)
			pprint(f"+---------------------------------------------+"); sleep(0.1); pprint()

	def updateLevel(self, playertype=None):
		self.level += 1
		self.maxHealth = 15 + floor(log10(self.level * 23 + 1) * self.level ** 1.7)
		self.health = self.maxHealth
		self.defence += randint(0, 5)
		self.speed += randint(0, 5)
		self.basedef = self.defence
		self.baseSpeed = self.speed
		if playertype is None:
			self.experience = self.experience - self.nextLevelAt
		else:
			self.experience = randint(0, self.nextLevelAt)
		self.nextLevelAt = self.experienceChart[self.level + 1] if self.level < 100 else None
		if playertype is None:
			pprint(f"{self.name} levelled up...\n");
			sleep(0.3)
			pprint(f"Current level: {self.level}");
			sleep(0.3)
			pprint(f"Max Health increased to {self.maxHealth}");
			sleep(0.3)
			pprint(f"Defence increased to {self.defence}");
			sleep(0.3)
			pprint(f"Speed increased to {self.speed}\n");
			sleep(0.3)

	def npcPokemonReady(self, maxlevel):
		for _ in range(maxlevel):
			self.updateLevel(playertype='npc')

	def visitPokemonCentre(self):
		self.health = self.maxHealth
		for attack in self.attacks:
			if attack is not None:
				attack.count = attack.maxcount
