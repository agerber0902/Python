#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 18 12:38:10 2026

Player Predictor main operating file

@author: andrewgerber
"""

#Define Imports
from classes.player import Player
from scraper import htmlScraper
from scraper.infoScraper import info_scraper
from scraper.gameScrapper import getGameLogFromSoup
from data.playerFirebase import PlayerFirebase

#Initialize Firebase
firebase = PlayerFirebase("/Users/andrewgerber/Development/Python/PlayerPredictor/data/player-data-cf86f-firebase-adminsdk-fbsvc-6bd1a64e27.json")


# Get player data from url
#player_url = "https://www.pro-football-reference.com/players/J/JeanAs00.htm"
#player_url = "https://www.pro-football-reference.com/players/A/AlleJo02.htm"

alpha = 'A'
player_page_base_url = f"https://www.pro-football-reference.com/players/{alpha}/"

html_soup = htmlScraper.getHtmlSoupFromUrl(player_url)

# Create Player
url_to_save = player_url.split("/")[-1].split(".htm")[0]
info = info_scraper(url_to_save, html_soup)
firebase.add_playerInfo(info)
#games = getGameLogFromSoup(html_soup)
#player = Player(playerInfo = info, games = games)