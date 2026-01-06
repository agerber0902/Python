#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  5 13:42:43 2026

Sports Reference Player page web scraper.
Take an input of player_url which maps to player's page on sports reference
Get the 2025 Game Log Table and parse data

@author: andrewgerber
"""

#   Define Imports
from utils import doesExist
from classes.gameLog import GameLog
#-- Imports

#   Use beautiful soup to get the the player game log
def getGameLogFromSoup(html_soup):
    print("Gathering Game Log from soup")
    
    game_log = []
    
    #   If html soup does not exist, return empty list
    if not doesExist(html_soup):
        print("No HTML was returned by the response.")
        return game_log
    
    player_name = html_soup.select_one(".breadcrumbs strong").get_text(strip=True)
    
    print(f"Html found. Parsing for Game Log Table for {player_name}..")
    
    # Iterate through all tables to find game log    
    game_log_table = None

    for table in html_soup.find_all("table"):
        caption = table.find("caption")
        if not caption:
            print('no caption')
            continue

        caption_text = caption.get_text(strip=True).lower()
        print(f"Caption Found: '{caption_text}'")
        if "game log" in caption_text:
            game_log_table = table
            break

    # Get all the table rows
    game_log_rows = game_log_table.find_all('tr')

    # Trim heading row
    game_log_rows = game_log_rows[2:]

    
    return games_from_log(game_log_rows, player_name)
    
    return game_log
    print("Gathering finished");

#   Return all the games from the game log table
def games_from_log(game_log_rows, player_name):
    #Find all table headers with data-stat tag      
    games = []

    for game_row in game_log_rows:  # your list of <tr> tags
        row_data = {}

        for cell in game_row.find_all(["th", "td"]):
            stat = cell.get("data-stat")
            if not stat:
                print("No Stat")
                continue

            value = cell.get_text(strip=True)

            # Normalize game location
            if stat == "game_location":
                if value == "@":
                    value = "AWAY"
                elif value == "":
                    value = "HOME"
                elif value == "N":
                    value = "NEUTRAL"

            row_data[stat] = value

        games.append(row_data)
    
    print(f"Found {len(games)} games for {player_name}")
    game_log = GameLog(games = games)
    return game_log