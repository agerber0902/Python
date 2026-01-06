#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  6 11:12:34 2026

Class for PlayerInfo

@author: andrewgerber
"""

class PlayerInfo:
    
    def __init__(self, name, position, team, height, weight):
        print(f"Initializing PlayerInfo: {name}")
        self.name = name
        self.position = position
        self.team = team
        self.height = height
        self.weight = weight
    
    def displaySelf(self):
        print(f"{self.name}, {self.position}, {self.team}\n{self.height}, {self.weight}")
    
    #   Functions to determine position
    def isQB(self):
        return self.position.upper() == "QB"
    def isRB(self):
        return self.position.upper() == "RB"
    def isWR(self):
        return self.position.upper() == "WR"
    def isTE(self):
        return self.position.upper() == "TE"
    def isSkill(self):
        return self.isRB(self) or self.isWR(self) or self.isTE()
    def isKicker(self):
        return self.position.upper() == "K"
    def isPunter(self):
        return self.position.upper() == "P"
    # TODO: how to handle DEF?