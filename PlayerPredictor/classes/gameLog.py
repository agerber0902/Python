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
@dataclass
class GameLog:
    games: list[Game] = field(default_factory=list)

    def total_rush_yds(self) -> int:
        return sum(g.rush_yds for g in self.games)
