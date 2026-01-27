#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 18 11:57:52 2026

Game Data Class with Naming Conventions

@author: andrewgerber
"""
#Define Imports
from dataclasses import dataclass
from datetime import date, datetime
from typing import Optional
from .stats.passingGameStat import PassingGameStat
from .stats.rushingGameStat import RushingGameStat
from .stats.receivingGameStat import ReceivingGameStat
from .stats.totalGameStat import TotalGameStat

#Define Consts
GAME_NAMING_CONVENTIONS = {
    "team_name_abbr" : "team",
    "game_location": "location",
    "opp_name_abbr": "opp",
    "game_result": "result",
    }
PASSING_NAMING_CONVENTIONS = {
    "pass_cmp": "cmp",
    "pass_att": "att",
    "pass_yds": "yds",
    "pass_td": "td",
    "pass_int": "int",
    "pass_long": "long",
    "pass_rating": "rate",
    "pass_sacked": "sacked"
    }
 #   Convert dict to Game object
def game_from_dict(data: dict):
    
    passing_stats = PassingGameStat(
        pass_cmp = int(data.get("pass_cmp", 0) or 0),
        pass_att = int(data.get("pass_att", 0) or 0),
        pass_yds = int(data.get("pass_yds", 0) or 0),
        pass_td  = int(data.get("pass_td", 0) or 0),
        pass_int = int(data.get("pass_int", 0) or 0),
        pass_long = int(data.get("pass_long", 0) or 0),
        pass_rating = float(data.get("pass_rating", 0) or 0),
        pass_sacked = int(data.get("pass_sacked", 0) or 0)
    )
    
    rushing_stats = RushingGameStat(
        rush_att=int(data.get("rush_att", 0) or 0),
        rush_yds=int(data.get("rush_yds", 0) or 0),
        rush_td=int(data.get("rush_td", 0) or 0),
        rush_long=int(data.get("rush_long", 0) or 0),
        rush_yds_per_att=float(data.get("rush_yds_per_att", 0) or 0)
    )
    
    receiving_stats = ReceivingGameStat(
        targets=int(data.get("targets", 0) or 0),
        rec=int(data.get("rec", 0) or 0),
        rec_yds=int(data.get("rec_yds", 0) or 0),
        rec_yds_per_rec=float(data.get("rec_yds_per_rec", 0) or 0),
        rec_td=int(data.get("rec_td", 0) or 0),
        rec_long=int(data.get("rec_long", 0) or 0),
        catch_pct=float(str(data.get("catch_pct", "0") or "0").replace("%", "")),
        rec_yds_per_tgt=float(data.get("rec_yds_per_tgt", 0) or 0)
    )
    
    total_stats = TotalGameStat(
        touches=int(data.get("touches", 0) or 0),
        yds_per_touch=float(data.get("yds_per_touch", 0) or 0),
        yds_from_scrimmage=int(data.get("yds_from_scrimmage", 0) or 0),
        rush_receive_td=int(data.get("rush_receive_td", 0) or 0),
        fumbles=int(data.get("fumbles", 0) or 0)
    )
    
    return Game(
        date=datetime.strptime(data["date"], "%Y-%m-%d").date(),
        team_name_abbr=data.get("team_name_abbr", ""),
        game_location=data.get("game_location", ""),
        opp_name_abbr=data.get("opp_name_abbr", ""),
        game_result=data.get("game_result", ""),
    
        passing_stats = passing_stats,
    
        rushing_stats = rushing_stats,
    
        receiving_stats = receiving_stats,
    
        total_stats = total_stats,
    )    

@dataclass
class Game(PassingGameStat, RushingGameStat, ReceivingGameStat, TotalGameStat):
    
    # Game meta data
    date: Optional[date] = None
    team_name_abbr: str = ""
    game_location: str  = "" # HOME / AWAY
    opp_name_abbr: str  = ""
    game_result: str    = ""   #"W, 20-13"

    # Stats (composition)
    passing_stats: Optional[PassingGameStat] = None
    rushing_stats: Optional[RushingGameStat] = None
    receiving_stats: Optional[ReceivingGameStat] = None
    total_stats: Optional[TotalGameStat] = None
    
    @property
    def opp_str(self):
        if self.game_location.upper() == "AWAY":
            return f"@ {self.opp_name_abbr}"
        else:
            return f"vs {self.opp_name_abbr}"
    
    @property
    def game_string(self):
        opp_string: str = f"@ {self.opp_name_abbr}" if self.game_location.upper() == "AWAY" else f"vs {self.opp_name_abbr}" 
        return f"{self.date} {opp_string}"