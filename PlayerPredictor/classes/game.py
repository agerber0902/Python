#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 18 11:57:52 2026

Game Data Class with Naming Conventions

@author: andrewgerber
"""
#Define Imports
from dataclasses import dataclass
from datetime import date
from typing import Optional
from .stats.passingGameStat import PassingGameStat
from .stats.rushingGameStat import RushingGameStat
from .stats.receivingGameStat import ReceivingGameStat
from .stats.totalGameStat import TotalGameStat

#Define Consts
GAME_NAMING_CONVENTIONS = {
    "team_name_abbr" : "team",
    "game_location": "location",
    "opp_name_abbr": "opp",
    "game_result": "result"
    }

@dataclass
class Game(PassingGameStat, RushingGameStat, ReceivingGameStat, TotalGameStat):
    
    # Game meta data
    date: Optional[date] = None
    team_name_abbr: str = ""
    game_location: str  = "" # HOME / AWAY
    opp_name_abbr: str  = ""
    game_result: str    = ""   #"W, 20-13"
    
    # Initialize all inherited stat classes
    def __post_init__(self, passing_stats, rushing_stats, receiving_stats, total_stats):
        #Passing Stats
        self.passing_stats = passing_stats
        
        #Rushing Stats
        self.rushing_stats = rushing_stats
        
        #Receiving Stats
        self.receiving_stats = receiving_stats
        
        #Total Stats
        self.total_stats = total_stats
    
    @property
    def game_string(self):
        opp_string: str = f"@ {self.opp_name_abbr}" if self.game_location.upper() == "AWAY" else f"vs {self.opp_name_abbr}" 
        return f"{self.date} {opp_string}"