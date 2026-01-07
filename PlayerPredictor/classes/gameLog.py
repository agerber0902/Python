#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  6 12:22:14 2026

GameLog Data Class - contains the game log object
GameLog - list of games

@author: andrewgerber
"""

from dataclasses import dataclass, field
from .game import Game
from utils import isValidType
from typing import List, Dict

MAX_RUSHING_STAT_NAMES = ["rush_att", "rush_yds", "rush_td", "rush_long", "rush_yrds_per_attempt"]
MAX_RECEIVING_STAT_NAMES = ["targets", "rec", "rec_yds", "rec_yds_per_rec", "rec_td", "rec_long", "rec_yrds_per_tgt"]
MAX_STAT_NAMES = ["yds_per_touch", "yds_from_scrimage", "rush_receive_td", "fumbles"]

TOTAL_RUSHING_STAT_NAMES = ["rush_att", "rush_yds", "rush_td"]
TOTAL_RECEIVING_STAT_NAMES = ["targets", "rec", "rec_yds", "rec_td"]

@dataclass
class GameLog:
    games: list[Game] = field(default_factory=list)
    rushingTotals: Dict[str, int] = field(default_factory=dict)
    receivingTotals: Dict[str, int] = field(default_factory=dict)    
    
    def __post_init__(self):
        # Compute totals for all rush stats
        for stat_name in TOTAL_RUSHING_STAT_NAMES:
            self.rushingTotals[stat_name] = sum(
                int(getattr(g, stat_name, 0) or 0)
                for g in self.games
            )
        
        # Compute totals for all rec stats
        for stat_name in TOTAL_RECEIVING_STAT_NAMES:
            self.receivingTotals[stat_name] = sum(
                int(getattr(g, stat_name, 0) or 0)
                for g in self.games
            )
                    
    #   Retun the game from games input with the max value for stat_name input
    def stat_max(self, stat_name: str) -> list[Game]:
        try:
            if not isValidType(stat_name, str):
                raise TypeError("Stat Name is not valid.")
            
            #   Get the max value
            max_value = max(
                self.games,
                key=lambda game: getattr(game, stat_name, 0) or 0,
                default=None
            )
            
            # Return all games that match the max, ordered by date
            return sorted(
                (
                    game for game in self.games
                    if (getattr(game, stat_name, 0) or 0) == max_value
                ),
                key=lambda game: game.date
            )
            
        except:
            print(f"An error occured getting stat max for {stat_name}")
            return None

    #   Game Log Totals
    def stat_total(self, stat_name: str) -> int:
        if not isValidType(stat_name, str):
            print(f"Stat Name is not valid: {stat_name}")
            return 0
        
        return sum(
            getattr(g, stat_name, 0) or 0
            for g in self.games
        )
