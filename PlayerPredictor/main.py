#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 18 12:38:10 2026

Player Predictor main operating file

@author: andrewgerber
"""

#Define Imports
import helpers.mainHelper as helper
from data.playerFirebase import PlayerFirebase


print("Beginning application.. initializing database.")

#Initialize Firebase
firebase = PlayerFirebase("/Users/andrewgerber/Development/Python/PlayerPredictor/data/player-data-cf86f-firebase-adminsdk-fbsvc-6bd1a64e27.json")
print("Database initialized.")

# Intro messaging
print("Welcome to player data with python!")

#Print Menu
print(""""
  1. Get Player from database
  2. Add Player to database
  3. Get Player breakdowns
  4. Player Trivia
  0. Quit
      """)
# Get the user selection. Stay until valid selection
valid_options: list[int] = [1,2,3,4]
error_message: str = f"Invalid input, please input integer value within {valid_options[0]}-{valid_options[-1]}"
selection = None
while not selection:    
    try:
        selection: int = int(input("What would you like to do? "))
        
        if selection == 0:
            break
        
        if selection not in valid_options:
            print(error_message)
            selection = None
            
    except:
        print(error_message)
        selection = None

# Handle the user input
print("\n\n")
if(selection == 1):
    helper.get_player(firebase)
elif(selection == 2):
    helper.add_player(firebase)
elif(selection == 3):
    helper.player_breakdowns(firebase)
elif(selection == 4):
    helper.player_trivia(firebase)