#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  6 12:07:15 2026

Main Player Class object. Inherits from PlayerInfo

@author: andrewgerber
"""
import PlayerInfo as PI
class Player(PI.PlayerInfo):
    
    def __init__(self, playerInfo = None, gameLog = None):
        #Initialize Player Info
        self.PlayerInfo = playerInfo
        self.GameLog = gameLog
    
    #Set Player Info after creation
    def setPlayerInfo(self, playerInfo):
        self.PlayerInfo = playerInfo
    
    