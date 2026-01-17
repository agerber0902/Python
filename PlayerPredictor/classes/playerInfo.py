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

    def to_dataframe_row(self) -> dict:
        return {
            "name": self.name,
            "position": self.position,
            "team": self.team,
            "height": self.height,
            "weight": self.weight
            }
        

    #   Functions to determine position
    @property
    def isQB(self) -> bool:
        return "QB" in self.position.upper()
    @property
    def isRB(self) -> bool:
        return self.position.upper() == "RB"
    @property
    def isWR(self) -> bool:
        return self.position.upper() == "WR"
    @property
    def isTE(self) -> bool:
        return self.position.upper() == "TE"
    @property
    def isSkill(self) -> bool:
        return self.isRB(self) or self.isWR(self) or self.isTE()
    @property
    def isKicker(self) -> bool:
        return self.position.upper() == "K"
    @property
    def isPunter(self) -> bool:
        return self.position.upper() == "P"
    # TODO: how to handle DEF?
