#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 18 11:45:32 2026

Player Info Data Class containing the basic player info
Name, Team, Position, height, weight, college

@author: andrewgerber
"""

#Define imports
from dataclasses import dataclass

#Define Consts
RB_NAMES = ["RB", "HB", "FB"]

@dataclass
class PlayerInfo:
    # Basic player info
    name: str 
    team: str
    position: str
    height: str
    weight: str
    
    # Bonus player info
    college: str
    draftedTeam: str
    
    # Define Properties
    @property
    def isQb(self) -> bool:
        return self.position.upper() == "QB"
    @property
    def isRb(self) -> bool:
        return self.position.upper() in RB_NAMES
    @property
    def isWr(self) -> bool:
        return self.position.upper() == "WR"
    @property
    def isTE(self) -> bool:
        return self.position.upper() == "TE"
    @property
    def isSkill(self) -> bool:
        return self.isRb or self.isWr or self.isTE
    # End of Properties