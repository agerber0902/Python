#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  6 12:07:15 2026

Main Player Class object. Inherits from PlayerInfo
Displays all the player info and game log highlights

@author: andrewgerber
"""
from .playerInfo import PlayerInfo
from pandas import DataFrame

std_game_col_names = {"team_name_abbr": "team",
         "game_location": "loc",
         "yds_from_scrimmage": "total_yds",
         "rush_receive_td": "total_tds"
         }

class Player(PlayerInfo):
    
    def __init__(self, player_info = None, game_log = None):
        #Initialize Player Info
        self.PlayerInfo = player_info
        self.GameLog = game_log
        

    def display_games(self):
        games = DataFrame(self.GameLog.games)
        games.rename(
            columns=std_game_col_names, inplace=True)
        return games