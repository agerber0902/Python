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

player1_url: str = input("Enter the first player's url: ")
player2_url: str = input("Enter the second player's url: ")

#Call the scraper to set the player data
player1 = player2 = None
player1 = get_player_by_url(player1_url)
player2 = get_player_by_url(player2_url)