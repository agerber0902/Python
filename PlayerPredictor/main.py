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

# Get player data from url
player_url = "https://www.pro-football-reference.com/players/J/JeanAs00.htm"
#player_url = "https://www.pro-football-reference.com/players/A/AlleJo02.htm"
html_soup = htmlScraper.getHtmlSoupFromUrl(player_url)

# Create Player
info = info_scraper(html_soup)
games = getGameLogFromSoup(html_soup)
player = Player(playerInfo = info, games = games)