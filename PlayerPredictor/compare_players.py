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

def create_compare_table(players: list[Player]) -> str:
    #   Create Headers
    table_headers = ["Stat\t\t"] + [player.PlayerInfo.name for player in players]
    print(" | ".join(table_headers))
    print("--------------------------------")
    
    # Collect all stat names (keys) from all players to handle missing stats
    all_stats = set()
    for player in players:
        all_stats.update(player.GameLog.passingTotals.keys())
    
    
    #   Create rows
    rows: list[dict[str, list[str]]] = []
    for stat in all_stats:
        
        values = []
        #row = {stat: values}
        #rows.append(row)
        for player in players:
            values.append(str(player.GameLog.passingTotals.get(stat, 0)) + "\t\t")
            
        row = {stat: values}
        print(f"{stat}\t | " + "| ".join(values))
        rows.append(row)
        
    
    return ""
# https://www.pro-football-reference.com/players/A/AlleJo02.htm
# https://www.pro-football-reference.com/players/B/BurrJo01.htm
player1_url: str = "https://www.pro-football-reference.com/players/A/AlleJo02.htm" #input("Enter the first player's url: ")
player2_url: str = "https://www.pro-football-reference.com/players/B/BurrJo01.htm" #input("Enter the second player's url: ")

#Call the scraper to set the player data
player1 = get_player_by_url(player1_url)
player2 = get_player_by_url(player2_url)

#   Compare by Totals
create_compare_table([player1, player2])