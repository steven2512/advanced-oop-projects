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