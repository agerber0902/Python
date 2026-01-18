#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 16 17:42:18 2026

Leveraging pandas, compare players based on player game logs

@author: andrewgerber
"""

#Define Imports
import pandas as pd

from classes.player import Player

from scraper.htmlScraper import getHtmlSoupFromUrl
from scraper.playerScraper import getPlayerDataFromSoup
#--Imports

#Functions
def compare_players(players: list[Player]) -> pd.DataFrame:
    #   Validate players
    if not players or len(players) <= 0:
        print("Player list is empty")
        
    #   Convert to Data Frame
    data_frame = pd.DataFrame(players)
    print(data_frame)

#--Functions

#TESTING
def get_player_by_url(url : str) -> Player:
    try:
        html_soup = getHtmlSoupFromUrl(url)
        player = getPlayerDataFromSoup(html_soup)
        return player
    except:
        print(f"An error occured processing player 1 url: {player1_url}")
        return None
    
player1_url: str = "https://www.pro-football-reference.com/players/A/AlleJo02.htm" #input("Enter the first player's url: ")
player2_url: str = "https://www.pro-football-reference.com/players/B/BoweBr01.htm" #input("Enter the second player's url: ")
player3_url: str = "https://www.pro-football-reference.com/players/B/BurrJo01.htm"

#Call the scraper to set the player data
player1 = get_player_by_url(player1_url)
player2 = get_player_by_url(player2_url)
player3 = get_player_by_url(player3_url)

data_frame = pd.DataFrame([
    player1.PlayerInfo.to_dataframe_row(),
    player2.PlayerInfo.to_dataframe_row(),
    player3.PlayerInfo.to_dataframe_row(),
])

passing_totals_data_frame = pd.DataFrame([
    player1.game_log_to_dataframe("passing_totals"),
    player2.game_log_to_dataframe("passing_totals"),
    player3.game_log_to_dataframe("passing_totals"),
    ])

rushing_totals_data_frame = pd.DataFrame([
    player1.game_log_to_dataframe("rushing_totals"),
    player2.game_log_to_dataframe("rushing_totals"),
    player3.game_log_to_dataframe("rushing_totals"),
    ])

receiving_totals_data_frame = pd.DataFrame([
    player1.game_log_to_dataframe("receiving_totals"),
    player2.game_log_to_dataframe("receiving_totals"),
    player3.game_log_to_dataframe("receiving_totals"),
    ])

passing_maxes_data_frame = pd.DataFrame([
    player1.game_log_to_dataframe("passing_maxes"),
    player2.game_log_to_dataframe("passing_maxes"),
    player3.game_log_to_dataframe("passing_maxes"),
    ])

rushing_maxes_data_frame = pd.DataFrame([
    player1.game_log_to_dataframe("rushing_maxes"),
    player2.game_log_to_dataframe("rushing_maxes"),
    player3.game_log_to_dataframe("rushing_maxes"),
    ])

receiving_maxes_data_frame = pd.DataFrame([
    player1.game_log_to_dataframe("receiving_maxes"),
    player2.game_log_to_dataframe("receiving_maxes"),
    player3.game_log_to_dataframe("receiving_maxes"),
    ])

print(f"{passing_totals_data_frame}\n")
print(f"{rushing_totals_data_frame}\n")
print(f"{receiving_totals_data_frame}\n")
print(f"{passing_maxes_data_frame}\n")
print(f"{rushing_maxes_data_frame}\n")
print(f"{receiving_maxes_data_frame}")

#compare_players([player1, player2, player3])

#END TESTING