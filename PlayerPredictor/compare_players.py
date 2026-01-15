#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 12 21:33:56 2026

Compare Player Stats and output differences

@author: andrewgerber
"""

#Define Inports
from scraper.htmlScraper import getHtmlSoupFromUrl
from scraper.playerScraper import getPlayerDataFromSoup
from classes.player import Player
#-- Imports

#Functions
def get_player_by_url(url : str) -> Player:
    try:
        html_soup = getHtmlSoupFromUrl(url)
        player = getPlayerDataFromSoup(html_soup)
        return player
    except:
        print(f"An error occured processing player 1 url: {player1_url}")
        return None

def create_compare_tables(players: list[Player]):
    
    #Display passing totals compare table
    if any(player.PlayerInfo.isQB for player in players):
        create_passing_compare_table(players, False)
    
    #Display skill totals compare
    print("\n")
    create_skill_compare_table(players, False)
    
    # Display Maxes
    print ("\n\n")
    if any(player.PlayerInfo.isQB for player in players):
        create_passing_compare_table(players, True)

    print("\n")
    create_skill_compare_table(players, True)

def create_skill_compare_table(players: list[Player], isMax: bool) -> str:
    #   Create Headers
    stat_header = "Max Stat" if isMax else "Stat"
    table_headers = [stat_header] + [str(player.PlayerInfo.name) for player in players]

    # Determine column width based on longest header
    header_col_width = max(len(h) for h in table_headers)
    
    # Collect all stat names (keys) from all players to handle missing stats
    
    all_stats = set()
    for player in players:
        if isMax:
            for d in player.GameLog.rushingMaxes:
                all_stats.update(d.keys())
            for d in player.GameLog.receivingMaxes:
                all_stats.update(d.keys())
        else:
            all_stats.update(player.GameLog.rushingTotals.keys())
            all_stats.update(player.GameLog.receivingTotals.keys())
    
    stat_col_width = max(len(s) for s in all_stats)
    col_width = max(header_col_width, stat_col_width)
    
    # Build header row
    header_row = " | ".join(h.ljust(col_width) for h in table_headers)
    
    print(header_row)
    print("-" * len(header_row))
    
    #   Create rows
    rows: list[dict[str, list[str]]] = []
    for stat in all_stats:
        
        if stat == "game_dates":
            continue
        
        values = []
        #row = {stat: values}
        #rows.append(row)
        for player in players:
            if("rush" in stat):
                if isMax:
                    values.append(str(player.GameLog.get_max_entry(player.GameLog.rushingMaxes, stat)[stat]))
                else:
                    values.append(str(player.GameLog.rushingTotals.get(stat, 0)))
            else:
                if isMax:
                    values.append(str(player.GameLog.get_max_entry(player.GameLog.receivingMaxes, stat)[stat]))
                else:
                    values.append(str(player.GameLog.receivingTotals.get(stat, 0)))
            
        row = {stat: values}
        display_row = " | ".join(h.ljust(col_width) for h in [stat, *values])
        print(display_row)
        #print(f"{stat}\t | " + "| ".join(values))
        rows.append(row)

def create_passing_compare_table(players: list[Player], isMax: bool) -> str:
    #   Create Headers
    stat_header = "Max Stat" if isMax else "Stat"
    table_headers = [stat_header] + [str(player.PlayerInfo.name) for player in players]

    # Determine column width based on longest header
    header_col_width = max(len(h) for h in table_headers)
    
    # Collect all stat names (keys) from all players to handle missing stats
    
    all_stats = set()
    for player in players:
        if isMax:
            for d in player.GameLog.passingMaxes:
                all_stats.update(d.keys())
        else:
            all_stats.update(player.GameLog.passingTotals.keys())
    
    stat_col_width = max(len(s) for s in all_stats)
    col_width = max(header_col_width, stat_col_width)

    # Build header row
    header_row = " | ".join(h.ljust(col_width) for h in table_headers)
    
    print(header_row)
    print("-" * len(header_row))


    #   Create rows
    rows: list[dict[str, list[str]]] = []
    for stat in all_stats:
        if stat == "game_dates":
            continue
        
        values = []
        #row = {stat: values}
        #rows.append(row)
        for player in players:
            if isMax:
                values.append(str(player.GameLog.get_max_entry(player.GameLog.passingMaxes, stat)[stat]))
            else:
                values.append(str(player.GameLog.passingTotals.get(stat, 0)))
            
        row = {stat: values}
        display_row = " | ".join(h.ljust(col_width) for h in [stat, *values])
        print(display_row)
        #print(f"{stat}\t | " + "| ".join(values))
        rows.append(row)
        
# https://www.pro-football-reference.com/players/A/AlleJo02.htm
# https://www.pro-football-reference.com/players/B/BurrJo01.htm
player1_url: str = "https://www.pro-football-reference.com/players/A/AlleJo02.htm" #input("Enter the first player's url: ")
player2_url: str = "https://www.pro-football-reference.com/players/B/BoweBr01.htm" #input("Enter the second player's url: ")
player3_url: str = "https://www.pro-football-reference.com/players/B/BurrJo01.htm"

#Call the scraper to set the player data
player1 = get_player_by_url(player1_url)
player2 = get_player_by_url(player2_url)
player3 = get_player_by_url(player3_url)

#   Compare by Totals
create_compare_tables([player1, player2, player3])