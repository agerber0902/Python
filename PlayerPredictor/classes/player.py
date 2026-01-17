#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  6 12:07:15 2026

Main Player Class object. Inherits from PlayerInfo
Displays all the player info and game log highlights

@author: andrewgerber
"""
from .playerInfo import PlayerInfo

class Player(PlayerInfo):
    
    def __init__(self, player_info = None, game_log = None):
        #Initialize Player Info
        self.PlayerInfo = player_info
        self.GameLog = game_log

    def game_log_to_dataframe(self, logType: str) -> dict:
        if(logType == "" or logType == " "):
            return None
        
        if(logType.upper() == "PASSING_TOTALS"):
            return {
                "player_name" : self.PlayerInfo.name,
                **self.GameLog.passingTotals
                }
        elif(logType.upper() == "RUSHING_TOTALS"):
            return {
                "player_name" : self.PlayerInfo.name,
                **self.GameLog.rushingTotals
                }
        elif(logType.upper() == "RECEIVING_TOTALS"):
            return {
                "player_name" : self.PlayerInfo.name,
                **self.GameLog.receivingTotals
                }
        elif(logType.upper() == "PASSING_MAXES"):
            return {
                "player_name" : self.PlayerInfo.name,
                **self.GameLog.flatten_maxes(self.GameLog.passingMaxes)
                }
        elif(logType.upper() == "RUSHING_MAXES"):
            return {
                "player_name" : self.PlayerInfo.name,
                **self.GameLog.flatten_maxes(self.GameLog.rushingMaxes)
                }
        elif(logType.upper() == "RECEIVING_MAXES"):
            return {
                "player_name" : self.PlayerInfo.name,
                **self.GameLog.flatten_maxes(self.GameLog.receivingMaxes)
                }
        else:
            return None

    def display(self):        
        return f"""
{self.PlayerInfo.name} | {self.PlayerInfo.position}, {self.PlayerInfo.team}
{self.PlayerInfo.height} {self.PlayerInfo.weight}lbs
{self.display_stats(self.PlayerInfo.isQB)}
"""

    
    def display_stats(self, isQb: bool) -> str:
        
        stats: str = """"""
        totals: str = """
Season Stats:"""
        
        maxes: str = """Best Preformaces:"""
        
        if (isQb):
            # -- Totals
            totals += self.display_passing_stats(True)
            totals += "\n"
            totals += self.display_skill_stats(True)
            stats += totals
            # -- Maxes
            maxes += self.display_passing_stats(False)
            maxes += "\n"
            maxes += self.display_skill_stats(False)
            stats += maxes
        else:
            totals += self.display_skill_stats(True)
            stats += totals
            stats += "\n"
            maxes += self.display_skill_stats(False)
            stats += maxes
        return stats
    
    def display_passing_stats(self, isTotal: bool) -> str:
        if isTotal:
            return f"""
        Passing
            Attempts: {self.GameLog.passingTotals.get("pass_att", 0)}
            Completions: {self.GameLog.passingTotals.get("pass_cmp", 0)}
            Yards: {self.GameLog.passingTotals.get("pass_yds", 0)}
            TD: {self.GameLog.passingTotals.get("pass_td", 0)}
            INT: {self.GameLog.passingTotals.get("pass_int", 0)}
        """
        else:
            # return max
            pass_att_max = self.GameLog.get_max_entry(self.GameLog.passingMaxes, "pass_att")
            pass_cmp_max = self.GameLog.get_max_entry(self.GameLog.passingMaxes, "pass_cmp")
            pass_yds_max = self.GameLog.get_max_entry(self.GameLog.passingMaxes, "pass_yds")
            pass_td_max = self.GameLog.get_max_entry(self.GameLog.passingMaxes, "pass_td")
            pass_int_max = self.GameLog.get_max_entry(self.GameLog.passingMaxes, "pass_int")
            return f"""
        Passing
            Attempts: {pass_att_max["pass_att"] if pass_att_max else 0}
                Games: {self.format_dates(pass_att_max["game_dates"]) if pass_att_max else "-"}
            Completions: {pass_cmp_max["pass_cmp"] if pass_cmp_max else 0}
                Games: {self.format_dates(pass_cmp_max["game_dates"]) if pass_cmp_max else "-"}
            Yards: {pass_yds_max["pass_yds"] if pass_yds_max else 0}
                Games: {self.format_dates(pass_yds_max["game_dates"]) if pass_yds_max else "-"}
            TD: {pass_td_max["pass_td"] if pass_td_max else 0}
                Games: {self.format_dates(pass_td_max["game_dates"]) if pass_td_max else "-"}
            INT: {pass_int_max["pass_int"] if pass_int_max else 0}
                Games: {self.format_dates(pass_int_max["game_dates"]) if pass_int_max else "-"}
        """
        
    def display_skill_stats(self, isTotal: bool) -> str:
        if isTotal:
            return f"""
    Rushing
        Attempts: {self.GameLog.rushingTotals.get("rush_att", 0)}
        Yards: {self.GameLog.rushingTotals.get("rush_yds", 0)}
        TD: {self.GameLog.rushingTotals.get("rush_td", 0)}
    
    Receiving
        Catches/Targets: {self.GameLog.receivingTotals.get("rec", 0)}/{self.GameLog.receivingTotals.get("targets", 0)}
        Yards: {self.GameLog.receivingTotals.get("rec_yds", 0)}
        TD: {self.GameLog.receivingTotals.get("rec_td", 0)}
        """
        else:
            
            rush_att_max = self.GameLog.get_max_entry(self.GameLog.rushingMaxes, "rush_att")
            rush_yds_max = self.GameLog.get_max_entry(self.GameLog.rushingMaxes, "rush_yds")
            rush_td_max = self.GameLog.get_max_entry(self.GameLog.rushingMaxes, "rush_td")
            rec_yds_max = self.GameLog.get_max_entry(self.GameLog.receivingMaxes, "rec_yds")
            rec_td_max = self.GameLog.get_max_entry(self.GameLog.receivingMaxes, "rec_td")
            rec_max = self.GameLog.get_max_entry(self.GameLog.receivingMaxes, "rec")
            target_max = self.GameLog.get_max_entry(self.GameLog.receivingMaxes, "targets")
            
            return f"""
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

