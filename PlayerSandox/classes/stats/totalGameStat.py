#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 18 11:45:32 2026

Total Game Stats for Game Data Class

@author: andrewgerber
"""

#Define Imports
from dataclasses import dataclass

#Define Consts
TOTALS_NAMING_CONVENTIONS: dict = {
    "yds_per_touch": "YPT",
    "yards_from_scrimmage": "YFS",
    "rush_receive_td": "td"
    }

@dataclass
class TotalGameStat:
 
    touches: int = 0
    yds_per_touch: float = 0.0
    yds_from_scrimmage: int = 0
    rush_receive_td: int = 0
    fumbles: int = 0