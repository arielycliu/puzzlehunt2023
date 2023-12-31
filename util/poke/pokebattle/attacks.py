from random import random, randint
from math import floor


def pprint(*args, **kwargs):
    print('\t\t', *args, **kwargs)
    

class Attack(object):
    __slots__ = 'name', 'attCategory', 'pLevel', 'recoil', 'heal', 'damage', 'baseDamage', 'accuracy', 'count', 'maxcount', 'increasable'
    
    def __init__(self, name, attCategory, baseDamage, pokemonLevel, baseCount, increasable=1,recoil=0, heal=0, accuracy=1, *args, **kwargs):
        self.name = name
        self.attCategory = attCategory
        self.pLevel = pokemonLevel
        self.baseDamage = baseDamage
        self.recoil = - recoil
        self.maxcount = baseCount
        self.count = self.maxcount
        self.heal = heal
        self.increasable = increasable
        self.accuracy = accuracy
        self.damage = self.calcDamage()
        
    def updateAttack(self, newLevel, newRecoil=0, newHeal=0, baseDamage=-1):
        self.pLevel = newLevel
        self.recoil = - (newRecoil*self.pLevel + self.recoil)
        self.heal = newHeal*self.pLevel + self.heal
        self.maxcount = self.maxcount + min(2, max(0, randint(0, 1)), randint(0, 1))
        self.count = self.maxcount
        self.damage = self.calcDamage(baseDamage)
        
    def calcDamage(self, baseDamage=-1):
        if self.name in ['howl', 'sing', 'heal', 'hide', 'agility', 'harden', 'infactuate']: 
            return 0
        if baseDamage == -1:
            return floor(self.baseDamage + 5*(self.pLevel/2 + (1 - random())/3)**(1.2))
        else:
            return floor(baseDamage + 5*(self.pLevel/2 + (1 - random())/3)**(1.2))

    def printAttack(self):
        pprint('|----------------------------------------------------------------------------')
        pprint(f"| Attack: {self.name:15} | Type:   {self.attCategory:10} | Damage: {self.damage:5} | Count: {self.count:3}")
        pprint(f"| Heal:   {self.heal:15} | Recoil: {self.recoil:10} | Accuracy: {self.accuracy}")
        pprint('|----------------------------------------------------------------------------')
