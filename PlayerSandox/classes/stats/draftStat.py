#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 18 17:42:33 2026

Player Draft data class

@author: andrewgerber
"""

#Define Imports
from dataclasses import dataclass

@dataclass
class DraftStat:
    draft_team: str
    draft_round: str
    draft_pick: str
    draft_year: str