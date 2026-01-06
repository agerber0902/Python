#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  6 11:12:34 2026

Data Class for PlayerInfo

@author: andrewgerber
"""


from dataclasses import dataclass
@dataclass
class PlayerInfo:
    name: str
    position: str
    team: str
    height: str
    weight: str

    #   Functions to determine position
    @property
    def isQB(self):
        return self.position.upper() == "QB"
    @property
    def isRB(self):
        return self.position.upper() == "RB"
    @property
    def isWR(self):
        return self.position.upper() == "WR"
    @property
    def isTE(self):
        return self.position.upper() == "TE"
    @property
    def isSkill(self):
        return self.isRB(self) or self.isWR(self) or self.isTE()
    @property
    def isKicker(self):
        return self.position.upper() == "K"
    @property
    def isPunter(self):
        return self.position.upper() == "P"
    # TODO: how to handle DEF?