#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  5 17:13:12 2026

Test main file for testing and sandbox purposes

@author: andrewgerber
"""

# Parse the player url into soup
from htmlScraper import getHtmlSoupFromUrl
from playerScraper import getPlayerDataFromSoup

player_url = input("Enter player url: ")
#"https://www.pro-football-reference.com/players/J/JeanAs00.htm"
html_soup = getHtmlSoupFromUrl(player_url)

#   Get the player info
player = getPlayerDataFromSoup(html_soup)

#   Display the info
print(player.display())