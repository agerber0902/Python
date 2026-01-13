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
from scraper.utils import isValidType
from typing import List, Dict

MAX_PASSING_STAT_NAMES = ["pass_att", "pass_cmp", "pass_yds", "pass_td", "pass_int", "pass_long"]
MAX_RUSHING_STAT_NAMES = ["rush_att", "rush_yds", "rush_td", "rush_long"]
MAX_RECEIVING_STAT_NAMES = ["targets", "rec", "rec_yds", "rec_yds_per_rec", "rec_td", "rec_long"]
MAX_STAT_NAMES = ["yds_per_touch", "yds_from_scrimage", "rush_receive_td", "fumbles"]

TOTAL_PASSING_STAT_NAMES = ["pass_att", "pass_cmp", "pass_yds", "pass_td", "pass_int"]
TOTAL_RUSHING_STAT_NAMES = ["rush_att", "rush_yds", "rush_td"]
TOTAL_RECEIVING_STAT_NAMES = ["targets", "rec", "rec_yds", "rec_td"]

@dataclass
class GameLog:
    games: list[Game] = field(default_factory=list)
    
    #   Totals
    passingTotals: Dict[str, int] = field(default_factory=dict)
    rushingTotals: Dict[str, int] = field(default_factory=dict)
    receivingTotals: Dict[str, int] = field(default_factory=dict) 
    
    #   Maxes
    passingMaxes: List[Dict[str, object]] = field(default_factory=list)
    rushingMaxes: List[Dict[str, object]] = field(default_factory=list)
    receivingMaxes: List[Dict[str, object]] = field(default_factory=list)
    
    def __post_init__(self):
        
        #   Set Totals
        self.set_rush_totals()
        self.set_rec_totals()
        self.set_pass_totals()
        
        #   Set Max values
        self.set_pass_maxes()
        self.set_rush_maxes()
        self.set_rec_maxes()          
        
    #   Compute maxes for all rush stats
    def set_pass_maxes(self):
        for stat_name in MAX_PASSING_STAT_NAMES:
            max_games = self.stat_max(stat_name)
    
            if not max_games:
                continue
    
            max_value = getattr(max_games[0], stat_name, 0) or 0
            game_dates = [g.date for g in max_games]  # or g.date, or index
    
            self.passingMaxes.append({
                stat_name: max_value,
                "game_dates": game_dates
            })

    #   Compute maxes for all rush stats
    def set_rush_maxes(self):
        for stat_name in MAX_RUSHING_STAT_NAMES:
            max_games = self.stat_max(stat_name)
    
            if not max_games:
                continue
    
            max_value = getattr(max_games[0], stat_name, 0) or 0
            game_dates = [g.date for g in max_games]  # or g.date, or index
    
            self.rushingMaxes.append({
                stat_name: max_value,
                "game_dates": game_dates
            })

    #   Compute maxes for all rec stats
    def set_rec_maxes(self):
        for stat_name in MAX_RECEIVING_STAT_NAMES:
            max_games = self.stat_max(stat_name)
    
            if not max_games:
                continue
    
            max_value = getattr(max_games[0], stat_name, 0) or 0
            game_dates = [g.date for g in max_games]  # or g.date, or index
    
            self.receivingMaxes.append({
                stat_name: max_value,
                "game_dates": game_dates
            })
    
    #   Compute totals for all passing stats
    def set_pass_totals(self):
        for stat_name in TOTAL_PASSING_STAT_NAMES:
            self.passingTotals[stat_name] = sum(
                int(getattr(g, stat_name, 0) or 0)
                for g in self.games
            )
            
    #   Compute totals for all rush stats
    def set_rush_totals(self):
        for stat_name in TOTAL_RUSHING_STAT_NAMES:
            self.rushingTotals[stat_name] = sum(
                int(getattr(g, stat_name, 0) or 0)
                for g in self.games
            )
    
    #   Compute totals for all rec stats
    def set_rec_totals(self):
        for stat_name in TOTAL_RECEIVING_STAT_NAMES:
            self.receivingTotals[stat_name] = sum(
                int(getattr(g, stat_name, 0) or 0)
                for g in self.games
            )
                        
    #   Retun the game from games input with the max value for stat_name input
    def stat_max(self, stat_name: str) -> list[Game]:
        if not isValidType(stat_name, str):
            raise TypeError("Stat Name is not valid.")
    
        if not self.games:
            return []
    
        #   Find Max Value
        max_value = max(
            int(getattr(game, stat_name, 0) or 0)
            for game in self.games
        )
    
        #   Return all games that match, ordered by date
        return sorted(
            [
                game for game in self.games
                if int(getattr(game, stat_name, 0) or 0) == max_value
            ],
            key=lambda game: game.date
        )


    #   Game Log Totals
    def stat_total(self, stat_name: str) -> int:
        if not isValidType(stat_name, str):
            print(f"Stat Name is not valid: {stat_name}")
            return 0
        
        return sum(
            getattr(g, stat_name, 0) or 0
            for g in self.games
        )

    def find_game_by_date(self, date):
        return next(
            (g for g in self.games if g.date == date),
            None
            )


    def get_max_entry(self, max_list, stat_name: str):
        return next(
            (entry for entry in max_list if stat_name in entry),
            None
        )
