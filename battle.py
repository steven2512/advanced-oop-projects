from __future__ import annotations
from poke_team import Trainer, PokeTeam
from typing import Tuple
from battle_mode import BattleMode
from data_structures.queue_adt import *
from data_structures.array_sorted_list import *
from data_structures.sorted_list_adt import *
from data_structures.stack_adt import *
import math
import pdb

class Battle:
    """Unless stated otherwise, all methods in this classes are O(1) best/worst case."""
    def __init__(self, trainer_1: Trainer, trainer_2: Trainer, battle_mode: BattleMode, criterion = "health") -> None:
        self.trainer_1 = trainer_1
        self.trainer_2 = trainer_2
        self.battle_mode = battle_mode
        self.criterion = criterion
    
    def commence_battle(self) -> Trainer | None:
        #execute battle
        if self.battle_mode.value == 0:
            return self.set_battle()
        elif self.battle_mode.value == 1:
            return self.rotate_battle()
        else:
            return self.optimise_battle()
                    
    def _create_teams(self) -> None:
        """Best/worst case: O(TEAM_LIMIT)"""
        #pick the 2 teams through random mode
        self.trainer_1.pick_team()
        self.trainer_2.pick_team()
        #assemble team according to battle mode
        if self.battle_mode.value == 0:
            self.trainer_1.PokeTeam.assemble_team(BattleMode.SET)
            self.trainer_2.PokeTeam.assemble_team(BattleMode.SET)
        elif self.battle_mode.value == 1:
            self.trainer_1.PokeTeam.assemble_team(BattleMode.ROTATE)
            self.trainer_2.PokeTeam.assemble_team(BattleMode.ROTATE)
        else:
            self.trainer_1.PokeTeam.assemble_team(BattleMode.OPTIMISE)
            self.trainer_2.PokeTeam.assemble_team(BattleMode.OPTIMISE)
            #assign team based on criterion
            self.trainer_1.PokeTeam.assign_team(self.criterion)
            self.trainer_2.PokeTeam.assign_team(self.criterion)

    def set_battle(self) -> PokeTeam | None:
        """Worst/best case: O(round)"""
        #assign t1 and t2 as trainer1 and 2 teams
        t1 = self.trainer_1.PokeTeam.team
        t2 = self.trainer_2.PokeTeam.team
        #register Pokemons in the queue (unserved) of both teams to the Pokedex
        self.pokedex_reg()
        #serve Pokemon at front of the queue from each team
        p1 = t1.serve()
        p2 = t2.serve()
        round = 0
        while True:
            #These first if elif are for later evluation at the end of round
            if p1 is None and p2 is not None:
                #check if t1 is out of Pokemons
                if len(t1) == 0:
                    #append the last alive pokemon back in team at the end of battle
                    t2.rear -= t2.length+1
                    t2.append(p2)
                    break
                #if not then continue serving another Pokemon
                p1 = t1.serve()
                #trainer 2 registers new pokemon appeared in t1 to the Pokedex
                self.trainer_2.register_pokemon(p1)
            elif p1 is not None and p2 is None:
                #same process like above
                if len(t2) == 0:
                    #append the last alive pokemon back in team at the end of battle
                    t1.rear -= t1.length+1
                    t1.append(p1)
                    break 
                p2 = t2.serve()
                self.trainer_1.register_pokemon(p2)
            elif p1 is not None and p2 is not None:
                #both trainers register new Pokemon they see to the Pokedex
                self.trainer_1.register_pokemon(p2)
                self.trainer_2.register_pokemon(p1)
            else:
                #this is the case where both Pokemon died on the battlefield. So we serve new 2 pokemons and register Pokemons to the Pokedex
                p1 = t1.serve()
                p2 = t2.serve()
                self.trainer_1.register_pokemon(p2)
                self.trainer_2.register_pokemon(p1)
            #damage caluclation when p1 attacks p2 and vice versa
            dmg1 = self.cal_attack(p1,p2,self.trainer_1,self.trainer_2)
            dmg2 = self.cal_attack(p2,p1,self.trainer_2,self.trainer_1)

            #battle logic evaluation now begins
            if p1.speed > p2.speed:
                p2.defend(dmg1)
                if p2.is_alive():
                    p1.defend(dmg2)
                else:
                    p1.level_up()
                    round += 1
                    p2 = None
                    continue
            elif p1.speed < p2.speed:
                p1.defend(dmg2)
                if p1.is_alive():
                    p2.defend(dmg1)
                else:
                    p2.level_up()
                    round += 1
                    p1 = None
                    continue
            else:
                p1.defend(dmg2)
                p2.defend(dmg1)
            #evaluation after first attack
            if p1.is_alive() and not p2.is_alive():
                p1.level_up()
                p2 = None
                round += 1
                continue
            elif not p1.is_alive() and p2.is_alive():
                p2.level_up()
                round += 1
                p1 = None
                continue
            elif p1.is_alive() and p2.is_alive():
                p1.health -= 1
                p2.health -= 1
                if p1.is_alive() and not p2.is_alive():
                    p1.level_up()
                    p2 = None
                    round += 1
                    continue
                elif not p1.is_alive() and p2.is_alive():
                    p2.level_up()
                    p1 = None
                    round += 1
                    continue
                elif p1.is_alive() and p2.is_alive():
                   pass
                else:
                    p1 = None
                    p2 = None
            else:
                p1 = None
                p2 = None
            round += 1
        #final evaluation of the winner
        if len(t1) > 0 and len(t2) == 0:
            return self.trainer_1
        elif len(t2) > 0 and len (t1) == 0:
            return self.trainer_2
        else:
            return None
        
     def rotate_battle(self) -> PokeTeam | None:
        """Worst/best case: O(round)"""
        t1 = self.trainer_1.PokeTeam.team
        t2 = self.trainer_2.PokeTeam.team
        #register Pokemons in the queue (unserved) of both teams to the Pokedex
        self.pokedex_reg()
        # pdb.set_trace()
        p1 = t1.serve()
        p2 = t2.serve()
        #initial attack
        round = 0
        while True:
            if p1 is None and p2 is not None:
                #this dead_pokemon is for final evaluation after t1 has no Pokemons to play 
                dead_pokemon_1 = t1.array[t1.front-1]              
                if len(t1) == 0:
                    #append survived pokemon back after the last round
                    t2.append(p2)
                    self.trainer_1.PokeTeam.dead.push(dead_pokemon_1) 
                    break
                t2.append(p2)
                p2 = t2.serve()
                #when a Pokemon dies, it is added to the dead attribute of the trainer's Poketeam instance
                self.trainer_1.PokeTeam.dead.push(dead_pokemon_1)  
                p1 = t1.serve()
            elif p1 is not None and p2 is None:
                #same logic as above
                dead_pokemon_2 = t2.array[t2.front-1]
                if len(t2) == 0:
                    t1.append(p1)
                    self.trainer_2.PokeTeam.dead.push(dead_pokemon_2)
                    break
                t1.append(p1)
                p1 = t1.serve()
                self.trainer_2.PokeTeam.dead.push(dead_pokemon_2)
                p2 = t2.serve()
            elif p1 is not None and p2 is not None:
                #when both Pokemon doesn't die after the last fight
                if round != 0:
                    #apply when it's not round 0 when the battle start
                    t1.append(p1)
                    t2.append(p2)
                    p1 = t1.serve()
                    p2 = t2.serve()
            else:
                #these next 4 lines are for when both of them die in the last battle when both team have 1 Pokemon left
                dead_pokemon_1 = t1.array[t1.front-1]
                dead_pokemon_2 = t2.array[t2.front-1]
                self.trainer_1.PokeTeam.dead.push(dead_pokemon_1)
                self.trainer_2.PokeTeam.dead.push(dead_pokemon_2)
                #these are for when 2 pokemon dies together on the battlefield  
                p1 = t1.serve()
                p2 = t2.serve()
            #since it's a circular queue, Pokedex registration happen every round since a different Pokemon appear on battle each round
            self.trainer_1.register_pokemon(p2)
            self.trainer_2.register_pokemon(p1)
            #damage calculation
            dmg1 = self.cal_attack(p1,p2,self.trainer_1,self.trainer_2)
            dmg2 = self.cal_attack(p2,p1,self.trainer_2,self.trainer_1)

            #battle logic evaluation of p1 and p2
            if p1.speed > p2.speed:
                p2.defend(dmg1)
                if p2.is_alive():
                    p1.defend(dmg2)
                else:
                    p1.level_up()
                    round += 1
                    p2 = None
                    continue
            elif p1.speed < p2.speed:
                p1.defend(dmg2)
                if p1.is_alive():
                    p2.defend(dmg1)
                else:
                    p2.level_up()
                    round += 1
                    p1 = None
                    continue
            else:
                p1.defend(dmg2)
                p2.defend(dmg1)
            #evaluation after first attack
            if p1.is_alive() and not p2.is_alive():
                p1.level_up()
                p2 = None
                round += 1
                continue
            elif not p1.is_alive() and p2.is_alive():
                p2.level_up()
                round += 1
                p1 = None
                continue
            elif p1.is_alive() and p2.is_alive():
                p1.health -= 1
                p2.health -= 1
                if p1.is_alive() and not p2.is_alive():
                    p1.level_up()
                    p2 = None
                    round += 1
                    continue
                elif not p1.is_alive() and p2.is_alive():
                    p2.level_up()
                    p1 = None
                    round += 1
                    continue
                elif p1.is_alive() and p2.is_alive():
                   pass
                else:
                    p1 = None
                    p2 = None
            else:
                p1 = None
                p2 = None
            round += 1
        #final winner evaluation between trainer 1 and 2
        if len(t1) > 0 and len(t2) == 0:
            self.loser = self.trainer_2
            return self.trainer_1
        elif len(t2) > 0 and len (t1) == 0:
            self.loser = self.trainer_1
            return self.trainer_2
        else:
            return None
        
    def optimise_battle(self) -> PokeTeam | None:
        #logic is mostly similar to the last 2 battle modes
        """Worst/best case: O(round)"""
        #assign t1 and t2 as trainer1 and 2 teams
        t1 = self.trainer_1.PokeTeam.team
        t2 = self.trainer_2.PokeTeam.team
        #for extra access purposes during battle
        team1 = self.trainer_1.PokeTeam
        team2 = self.trainer_2.PokeTeam
        #register Pokemons in the queue (unserved) of both teams to the Pokedex
        self.pokedex_reg()
        p1 = t1.serve()
        p2 = t2.serve()
        round = 0
        while True:
            # pdb.set_trace()
            if p1 is None and p2 is not None:
                if len(t1) == 0:
                    t2.append(p2)
                    team2.assign_team(self.criterion)
                    t2 = self.trainer_2.PokeTeam.team
                    break
                t2.append(p2)
                #arrange team in ascending (or descending if applied special) based on the criterion
                team2.assign_team(self.criterion)
                t2 = self.trainer_2.PokeTeam.team
                #check if the order of team2 is set to descending during battle
                if team2.ascending == False:
                    team2.special(self.criterion)
                p2 = t2.serve()  
                p1 = t1.serve()
            elif p1 is not None and p2 is None:
                if len(t2) == 0:
                    t1.append(p1)
                    team1.assign_team(self.criterion)
                    t1 = self.trainer_1.PokeTeam.team
                    break
                t1.append(p1)
                #arrange team in ascending (or descending if applied special) based on the criterion
                team1.assign_team(self.criterion)
                t1 = self.trainer_1.PokeTeam.team
                #check if the order of team2 is set to descending during battle
                if team1.ascending == False:
                    team1.special(self.criterion)
                p1 = t1.serve()
                p2 = t2.serve()
            elif p1 is not None and p2 is not None:
                if round != 0:
                    t1.append(p1)
                    t2.append(p2)
                    #arrange team in ascending (or descending if applied special) based on the criterion
                    team1.assign_team(self.criterion)
                    team2.assign_team(self.criterion)
                    t1 = self.trainer_1.PokeTeam.team
                    t2 = self.trainer_2.PokeTeam.team
                    # pdb.set_trace()
                    if team1.ascending == False:
                        team1.special(self.criterion)
                    if team2.ascending == False:
                        team2.special(self.criterion)
                    p1 = t1.serve()
                    p2 = t2.serve()
                    # pdb.set_trace()
            else:
                print('Both DEAD')
                p1 = t1.serve()
                p2 = t2.serve()
            #pokedex registeration for both trainers
            self.trainer_1.register_pokemon(p2)
            self.trainer_2.register_pokemon(p1)
            #damage calculation of p1 on p2 and vice versa
            dmg1 = self.cal_attack(p1,p2,self.trainer_1,self.trainer_2)
            dmg2 = self.cal_attack(p2,p1,self.trainer_2,self.trainer_1)
            #battle logic evaluation of p1 and p2
            if p1.speed > p2.speed:
                p2.defend(dmg1)
                if p2.is_alive():
                    p1.defend(dmg2)
                else:
                    p1.level_up()
                    round += 1
                    p2 = None
                    continue
            elif p1.speed < p2.speed:
                p1.defend(dmg2)
                if p1.is_alive():
                    p2.defend(dmg1)
                else:
                    p2.level_up()
                    round += 1
                    p1 = None
                    continue
            else:
                p1.defend(dmg2)
                p2.defend(dmg1)
            #evaluation after first attack
            if p1.is_alive() and not p2.is_alive():
                p1.level_up()
                p2 = None
                round += 1
                continue
            elif not p1.is_alive() and p2.is_alive():
                p2.level_up()
                round += 1
                p1 = None
                continue
            elif p1.is_alive() and p2.is_alive():
                p1.health -= 1
                p2.health -= 1
                if p1.is_alive() and not p2.is_alive():
                    p1.level_up()
                    p2 = None
                    round += 1
                    continue
                elif not p1.is_alive() and p2.is_alive():
                    p2.level_up()
                    p1 = None
                    round += 1
                    continue
                elif p1.is_alive() and p2.is_alive():
                   pass
                else:
                    p1 = None
                    p2 = None
            else:
                p1 = None
                p2 = None
            round += 1
        #final winner evaluation between trainer 1 and 2
        if len(t1) > 0 and len(t2) == 0:
            return self.trainer_1
        elif len(t2) > 0 and len (t1) == 0:
            return self.trainer_2
        else:
            return None
    
    def cal_attack(self,p1,p2,trainer1,trainer2):
        attack_damage = math.ceil(p1.attack(p2) * (trainer1.get_pokedex_completion()/trainer2.get_pokedex_completion()))
        return attack_damage
    
    def pokedex_reg(self):
        """Worst/best: O(n+m) which n being the length of trainer 1 PokeTeam, and m being the length of trainer 2 PokeTeam"""
        for i in range(len(self.trainer_1.PokeTeam.team)):
            self.trainer_1.register_pokemon(self.trainer_1.PokeTeam.team.array[i])
        for j in range(len(self.trainer_2.PokeTeam.team)):
            self.trainer_2.register_pokemon(self.trainer_2.PokeTeam.team.array[j])



if __name__ == '__main__':
    t1 = Trainer('Ash')
    t2 = Trainer('Gary')
    b = Battle(t1, t2, BattleMode.ROTATE)
    b._create_teams()
    winner = b.commence_battle()

    if winner is None:
        print("Its a draw")
    else:
        print(f"The winner is {winner.get_name()}")