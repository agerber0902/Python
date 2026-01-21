#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 21 11:24:57 2026

Main Helper that handles all the user options

@author: andrewgerber
"""

# Define Imports
from classes.player import Player

# -- Option 1: Get Player From Database
def get_player() -> Player:
    player_name_input: str = input("Enter the name of the player you would like to get: ")
    
    #TODO: Validate
    #TODO: GET player by name
    #TODO: If does not exist, ask for url
    #TODO: validate url
    #TODO: get player from url
    #TODO: ask to save
    #TODO: view
    
# -- Option 1

# -- Option 2: Add Player to the Database
def add_player() -> Player:
    player_url_input: str = input("Enter the player url you would like to add to the database: ")
    #TODO: validate
    #TODO: save
    #TODO: view
    
# -- Option 2


# -- Option 3: Get Player for Breakdowns (Totals, Maxes)
def player_breakdowns():
    print("Feature coming soon.")
    #TODO: totals
    #TODO: maxes
    
# -- Option 3


# -- Option 4: Player Trivia
def player_trivia():
    print("Feature coming soon.")
    #TODO: create questions
    #TODO: display questions
    #TODO: create answers
    #TODO: get user input
    
# -- Option 4