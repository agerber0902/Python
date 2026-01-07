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
        
    def display(self):
        
        rush_att_max = self.GameLog.get_max_entry(self.GameLog.rushingMaxes, "rush_att")
        rush_yds_max = self.GameLog.get_max_entry(self.GameLog.rushingMaxes, "rush_yds")
        rush_td_max = self.GameLog.get_max_entry(
            self.GameLog.rushingMaxes, "rush_td"
        )
        
        rec_yds_max = self.GameLog.get_max_entry(
            self.GameLog.receivingMaxes, "rec_yds"
        )
        rec_td_max = self.GameLog.get_max_entry(
            self.GameLog.receivingMaxes, "rec_td"
        )
        rec_max = self.GameLog.get_max_entry(
            self.GameLog.receivingMaxes, "rec"    
        )
        target_max = self.GameLog.get_max_entry(
            self.GameLog.receivingMaxes, "targets"    
        )
        
        return f"""
{self.PlayerInfo.name} | {self.PlayerInfo.position}, {self.PlayerInfo.team}
{self.PlayerInfo.height} {self.PlayerInfo.weight}lbs

Season Stats:
    Rushing
        Attempts: {self.GameLog.rushingTotals.get("rush_att", 0)}
        Yards: {self.GameLog.rushingTotals.get("rush_yds", 0)}
        TD: {self.GameLog.rushingTotals.get("rush_td", 0)}

    Receiving
        Catches/Targets: {self.GameLog.receivingTotals.get("rec", 0)}/{self.GameLog.receivingTotals.get("targets", 0)}
        Yards: {self.GameLog.receivingTotals.get("rec_yds", 0)}
        TD: {self.GameLog.receivingTotals.get("rec_td", 0)}

Best Performances:
    Rushing
        Attempts: {rush_att_max["rush_att"] if rush_att_max else 0}
            Games: {self.format_dates(rush_att_max["game_dates"]) if rush_att_max else "-"}

        Yards: {rush_yds_max["rush_yds"] if rush_yds_max else 0}
            Games: {self.format_dates(rush_yds_max["game_dates"]) if rush_yds_max else "-"}

        TDs: {rush_td_max["rush_td"] if rush_td_max else 0}
            Games: {self.format_dates(rush_td_max["game_dates"]) if rush_td_max else "-"}

    Receiving
        Receptions: {rec_max["rec"] if rec_max else 0}
            Games: {self.format_dates(rec_max["game_dates"]) if rec_max else "-"}
    
        Targets: {target_max["targets"] if target_max else 0}
            Games: {self.format_dates(target_max["game_dates"]) if target_max else "-"}
    
        Yards: {rec_yds_max["rec_yds"] if rec_yds_max else 0}
            Games: {self.format_dates(rec_yds_max["game_dates"]) if rec_yds_max else "-"}

        TDs: {rec_td_max["rec_td"] if rec_td_max else 0}
            Games: {self.format_dates(rec_td_max["game_dates"]) if rec_td_max else "-"}
"""

    def format_dates(self, dates):
        formatted = []
    
        for d in dates:
            game = self.GameLog.find_game_by_date(d)
    
            date_str = (
                d.strftime("%m/%d/%Y")
                if hasattr(d, "strftime")
                else str(d)
            )
    
            if game:
                formatted.append(
                    f"{date_str} {'@' if game.game_location.upper() == 'AWAY' else 'vs.'} {game.opp_name_abbr}"
                )
            else:
                formatted.append(date_str)
    
        return ", ".join(formatted)

