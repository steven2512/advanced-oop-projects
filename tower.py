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