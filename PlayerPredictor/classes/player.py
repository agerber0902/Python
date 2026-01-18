#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 18 11:41:07 2026

Player Data Class that contains the player info and the games

@author: andrewgerber
"""

#Define Imports
from dataclasses import dataclass
from .playerInfo import PlayerInfo
from .game import Game

@dataclass
class Player(PlayerInfo):
    
    games: list[Game]
    
    #Initialize the class
    def __init__(self, player_info = None):
        #Initialize Player Info
        self.PlayerInfo = player_info
    