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
from scraper.utils import doesExist
import datetime
from scraper.classes.gameLog import GameLog
from scraper.classes.game import Game
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

        games.append(game_from_dict(row_data))
    
    print(f"Found {len(games)} games for {player_name}")
    game_log = GameLog(games = games)
    return game_log

#   Convert dict to Game object
def game_from_dict(data: dict) -> Game:
    
    return Game(
        date=datetime.datetime.strptime(data["date"], "%Y-%m-%d").date(),
        team_name_abbr=data.get("team_name_abbr", ""),
        game_location=data.get("game_location", ""),
        opp_name_abbr=data.get("opp_name_abbr", ""),
        game_result=data.get("game_result", ""),

        pass_cmp = int(data.get("pass_cmp", 0) or 0),
        pass_att = int(data.get("pass_att", 0) or 0),
        pass_yds = int(data.get("pass_yds", 0) or 0),
        pass_td  = int(data.get("pass_td", 0) or 0),
        pass_int = int(data.get("pass_int", 0) or 0),
        pass_long = int(data.get("pass_long", 0) or 0),
        pass_rating = float(data.get("pass_rating", 0) or 0),
        pass_sacked = int(data.get("pass_sacked", 0) or 0),

        rush_att=int(data.get("rush_att", 0) or 0),
        rush_yds=int(data.get("rush_yds", 0) or 0),
        rush_td=int(data.get("rush_td", 0) or 0),
        rush_long=int(data.get("rush_long", 0) or 0),
        rush_yds_per_att=float(data.get("rush_yds_per_att", 0) or 0),

        targets=int(data.get("targets", 0) or 0),
        rec=int(data.get("rec", 0) or 0),
        rec_yds=int(data.get("rec_yds", 0) or 0),
        rec_yds_per_rec=float(data.get("rec_yds_per_rec", 0) or 0),
        rec_td=int(data.get("rec_td", 0) or 0),
        rec_long=int(data.get("rec_long", 0) or 0),
        catch_pct=float(str(data.get("catch_pct", "0") or "0").replace("%", "")),
        rec_yds_per_tgt=float(data.get("rec_yds_per_tgt", 0) or 0),

        touches=int(data.get("touches", 0) or 0),
        yds_per_touch=float(data.get("yds_per_touch", 0) or 0),
        yds_from_scrimmage=int(data.get("yds_from_scrimmage", 0) or 0),
        rush_receive_td=int(data.get("rush_receive_td", 0) or 0),
        fumbles=int(data.get("fumbles", 0) or 0),
    )