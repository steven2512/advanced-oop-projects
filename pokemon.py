from pokemon_base import *
import inspect

class Bulbasaur(Pokemon):
    def __init__(self):
        super().__init__()
        self.health = 45
        self.level = 1
        self.poketype = PokeType.GRASS
        self.battle_power = 14
        self.evolution_line = ["Bulbasaur", "Ivysaur", "Venusaur"]
        self.name = "Bulbasaur"
        self.experience = 0
        self.defence = 20
        self.speed = 4.5

class Charmander(Pokemon):
    def __init__(self):
        super().__init__()
        self.health = 39
        self.level = 1
        self.poketype = PokeType.FIRE
        self.battle_power = 22
        self.evolution_line = ["Charmander", "Charmeleon", "Charizard"]
        self.name = "Charmander"
        self.experience = 0
        self.defence = 10
        self.speed = 65

class Squirtle(Pokemon):
    def __init__(self):
        super().__init__()
        self.health = 44
        self.level = 1
        self.poketype = PokeType.WATER
        self.battle_power = 10
        self.evolution_line = ["Squirtle", "Wartortle", "Blastoise"]
        self.name = "Squirtle"
        self.experience = 0
        self.defence = 12
        self.speed = 43

class Caterpie(Pokemon):
    def __init__(self):
        super().__init__()
        self.health = 20
        self.level = 1
        self.poketype = PokeType.BUG
        self.battle_power = 7
        self.evolution_line = ["Caterpie", "Metapod", "Butterfree"]
        self.name = "Caterpie"
        self.experience = 0
        self.defence = 8
        self.speed = 30

class Weedle(Pokemon):
    def __init__(self):
        super().__init__()
        self.health = 25
        self.level = 1
        self.poketype = PokeType.BUG
        self.battle_power = 9
        self.evolution_line = ["Weedle", "Kakuna", "Beedrill"]
        self.name = "Weedle"
        self.experience = 0
        self.defence = 10
        self.speed = 50

class Pidgey(Pokemon):
    def __init__(self):
        super().__init__()
        self.health = 40
        self.level = 1
        self.poketype = PokeType.FLYING
        self.battle_power = 21
        self.evolution_line = ["Pidgey", "Pidgeotto", "Pidgeot"]
        self.name = "Pidgey"
        self.experience = 0
        self.defence = 8
        self.speed = 56

class Rattata(Pokemon):
    def __init__(self):
        super().__init__()
        self.health = 30
        self.level = 1
        self.poketype = PokeType.NORMAL
        self.battle_power = 15
        self.evolution_line = ["Rattata", "Raticate"]
        self.name = "Rattata"
        self.experience = 0
        self.defence = 5
        self.speed = 72

class Spearow(Pokemon):
    def __init__(self):
        super().__init__()
        self.health = 40
        self.level = 1
        self.poketype = PokeType.FLYING
        self.battle_power = 19
        self.evolution_line = ["Spearow", "Fearow"]
        self.name = "Spearow"
        self.experience = 0
        self.defence = 9
        self.speed = 70

class Ekans(Pokemon):
    def __init__(self):
        super().__init__()
        self.health = 35
        self.level = 1
        self.poketype = PokeType.POISON
        self.battle_power = 15
        self.evolution_line = ["Ekans", "Arbok"]
        self.name = "Ekans"
        self.experience = 0
        self.defence = 8
        self.speed = 55

class Pikachu(Pokemon):
    def __init__(self):
        super().__init__()
        self.health = 35
        self.level = 1
        self.poketype = PokeType.ELECTRIC
        self.battle_power = 30
        self.evolution_line = ["Pikachu", "Raichu"]
        self.name = "Pikachu"
        self.experience = 0
        self.defence = 15
        self.speed = 90

class Sandshrew(Pokemon):
    def __init__(self):
        super().__init__()
        self.health = 50
        self.level = 1
        self.poketype = PokeType.GROUND
        self.battle_power = 30
        self.evolution_line = ["Sandshrew", "Sandslash"]
        self.name = "Sandshrew"
        self.experience = 0
        self.defence = 20
        self.speed = 40

class NidoranM(Pokemon):
    def __init__(self):
        super().__init__()
        self.health = 46
        self.level = 1
        self.poketype = PokeType.POISON
        self.battle_power = 23
        self.evolution_line = ["Nidoran(M)", "Nidorino", "Nidoking"]
        self.name = "Nidoran(M)"
        self.experience = 0
        self.defence = 7
        self.speed = 41

