# Player Sandbox
Leverages BeautifulSoup and requests libraries to scrape sports reference player pages by input url. This data is strictly use as mock data for testing.

User is prompted with a menu: 1. Get Player from database 2. Add Player to database 3. Get Player breakdowns 4. Player Trivia 0. Quit

## Option 1-2
A small amount of players exist in a firestore database for proof of concept, and the user can add get or add a player using options 1 or 2.

## Option 3
The user can enter as many player urls as they like, and the application will return a DataFrames table for stat totals and stat maxes

## Option 4
Player Trivia uses the Player Info from the database and generates 8 different types of questions. User answers the questions until answering incorrectly.

import sys
!{sys.executable} -m ensurepip --upgrade
!{sys.executable} -m pip install --upgrade pip
!{sys.executable} -m pip install firebase-admin
