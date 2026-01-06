#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  6 12:07:15 2026

Main Player Class object. Inherits from PlayerInfo

@author: andrewgerber
"""
from .playerInfo import PlayerInfo
class Player(PlayerInfo):
    
    def __init__(self, player_info = None, game_log = None):
        #Initialize Player Info
        self.PlayerInfo = player_info
        self.GameLog = game_log