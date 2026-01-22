#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 21 11:24:57 2026

Main Helper that handles all the user options

@author: andrewgerber
"""

# Define Imports
from classes.playerInfo import PlayerInfo
from data.playerFirebase import PlayerFirebase
from scraper.infoScraper import info_scraper

# Validate full name input
def is_text_with_spaces(value: str) -> bool:
    return all(part.isalpha() for part in value.split())

# Get the player by url
def get_player_info_by_url(firebase: PlayerFirebase, is_add = False) -> PlayerInfo:
    player_url = input("Enter the player url you would like to add to the database: ")
    
    player_info = info_scraper(player_url, None)
    
    if player_info is not None:
        is_add = input("Would you like to add the player to the database? (y/n): ") if is_add == False else is_add
        
        if(is_add):
            # Add the player to the database
            firebase.add_playerInfo(player_info)

        print(player_info)

# -- Option 1: Get Player From Database
def get_player(firebase: PlayerFirebase):
    player_name_input: str = input("Enter the name of the player you would like to get: ")
    
    # Validate
    isValid = is_text_with_spaces(player_name_input)
    while isValid is False:
        player_name_input = input("Player Name is not valid, try again: ")
        isValid = is_text_with_spaces(player_name_input)
    
    # GET player by name
    player_info = firebase.get_player_info_by_name(player_name_input)
    print(player_info if player_info is not None else "")
    
    #If does not exist, ask for url
    if(not player_info):
        
        is_url = input("Would you like to get by url? (y/n): ")
        if is_url.lower() == 'y':
            get_player_info_by_url(firebase)
            
    return
    
# -- Option 1

# -- Option 2: Add Player to the Database
def add_player(firebase: PlayerFirebase) -> PlayerInfo:
    get_player_info_by_url(firebase, True)
    
# -- Option 2


# -- Option 3: Get Player for Breakdowns (Totals, Maxes)
def player_breakdowns(firebase: PlayerFirebase):
    print("Feature coming soon.")
    #TODO: totals
    #TODO: maxes
    
# -- Option 3


# -- Option 4: Player Trivia
def player_trivia(firebase: PlayerFirebase):
    print("Feature coming soon.")
    #TODO: create questions
    #TODO: display questions
    #TODO: create answers
    #TODO: get user input
    
# -- Option 4