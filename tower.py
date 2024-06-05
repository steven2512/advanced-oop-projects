from poke_team import Trainer, PokeTeam
from enum import Enum
from data_structures.stack_adt import ArrayStack
from data_structures.queue_adt import CircularQueue
from data_structures.array_sorted_list import ArraySortedList
from data_structures.sorted_list_adt import ListItem
from typing import Tuple
from battle import *
from battle_mode import *
import random

class BattleTower:
    """Unless stated otherwise, all methods in this classes are O(1) best/worst case."""
    MIN_LIVES = 1
    MAX_LIVES = 3
    def __init__(self) -> None:
        self.player_trainer = None
        self.enemy_trainers = None
        self.battle = None
        self.wins = 0

    # Hint: use random.randint() for randomisation
    def set_my_trainer(self, trainer: Trainer) -> None:
        self.player_trainer = trainer
        self.player_trainer.lives = random.randint(self.MIN_LIVES, self.MAX_LIVES)
        

    def generate_enemy_trainers(self, num_teams: int) -> None:
        """Worst/best: O(num_teams)"""
        #create a queue for storing enemy trainers
        self.enemy_trainers = CircularQueue(num_teams)
        #add enemy trainers into the queue 
        for i in range(num_teams):
            enemy_trainer = Trainer(f'{i+1}')
            enemy_trainer.pick_team()
            enemy_trainer.PokeTeam.assemble_team(BattleMode.ROTATE)
            enemy_trainer.lives = random.randint(self.MIN_LIVES, self.MAX_LIVES)
            # pdb.set_trace()
            self.enemy_trainers.append(enemy_trainer)
        
            

    def battles_remaining(self) -> bool:
        if self.player_trainer.lives == 0 or len(self.enemy_trainers) == 0:
            return False
        return True

    def next_battle(self) -> Tuple[Trainer, Trainer, Trainer, int, int]:    
        #serve enemy_trainer at the beginning of every round
        enemy_trainer = self.enemy_trainers.serve() 
        #regenerate both teams before every round
        self.player_trainer.PokeTeam.regenerate_team(BattleMode.ROTATE)
        enemy_trainer.PokeTeam.regenerate_team(BattleMode.ROTATE)
        #2 teams of both trainers go into battle
        self.battle = Battle(self.player_trainer,enemy_trainer,BattleMode.ROTATE)
        winner = self.battle.commence_battle()
        loser = self.battle.loser
        #winner and loser evaluation for appropriate lives addition and subtraction
        if winner.name == self.player_trainer.name:
            enemy_trainer.lives -= 1
            self.wins +=1
        elif winner.name == enemy_trainer.name:
            self.player_trainer.lives -= 1
        else:
            self.player_trainer.lives -= 1
            enemy_trainer.lives -= 1
        #append enenmy trainer to the back of the queue if they still have lives larger than 0
        if enemy_trainer.lives > 0:
            self.enemy_trainers.append(enemy_trainer)
        #create a data structure of Array for temporarily strong the battle tower result
        result_temp = ArrayR(5)
        result_temp[0]= f'{winner.name} defeated {loser.name}'
        result_temp[1] = f'{winner.name}'
        result_temp[2] = f'{loser.name}'
        result_temp[3] = f'{self.player_trainer.lives}'
        result_temp[4] = f'{enemy_trainer.lives}'
        result = tuple(result_temp)
        return result
        
    def enemies_defeated(self) -> int:
        return self.wins