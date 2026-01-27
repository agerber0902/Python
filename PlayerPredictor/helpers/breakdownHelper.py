#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 24 15:43:11 2026

Player Breakdown Helper that uses player game data for display

@author: andrewgerber
"""

#Define Import
from classes.player import Player
from classes.game import Game, GAME_NAMING_CONVENTIONS, PASSING_NAMING_CONVENTIONS
from pandas import DataFrame
import numpy as np

PASSING_TOTAL_COLUMNS = ["cmp", "att", "td", "int", "long"]
PASSING_MAX_COLUMNS = ["cmp", "att", "td", "int", "long", "rate"]


def get_player_totals(players: list[Player]):
    return get_passing_totals(players)

def get_passing_totals(players: list[Player]):
    totals_rows = []
    maxes_rows = []

    for player in players:
        rows = []

        for game in player.games:
            if not game.passing_stats:
                continue
            rows.append(vars(game.passing_stats))

        # skip players with no passing stats
        if not rows:
            continue

        df = DataFrame(rows)

        # rename once
        df.rename(inplace=True, columns=PASSING_NAMING_CONVENTIONS)

        totals = df[PASSING_TOTAL_COLUMNS].sum()
        maxes = df[PASSING_MAX_COLUMNS].max()

        # label the row
        totals["player"] = player.playerInfo.name
        maxes["player"] = player.playerInfo.name

        totals_rows.append(totals)
        maxes_rows.append(maxes)

    totals_df = (
        DataFrame(totals_rows)
        .set_index("player")
        .sort_index()
    )

    maxes_df = (
        DataFrame(maxes_rows)
        .set_index("player")
        .sort_index()
    )

    return totals_df, maxes_df




def get_player_games(games):#player: Player) -> DataFrame:
    rows = []

    for game in games:
        if not game.passing_stats:
            continue

        row = {
            "date": game.date,
            "team": game.team_name_abbr,
            "opp": game.opp_name_abbr,
            "location": game.opp_str,  # uses your property
        }

        # unpack passing stats
        row.update(vars(game.passing_stats))

        rows.append(row)

    df = DataFrame(rows)
    df.set_index("date", inplace=True)
    df.sort_index(inplace=True)
    df.rename(inplace=True, columns=GAME_NAMING_CONVENTIONS)
    df.rename(inplace=True, columns=PASSING_NAMING_CONVENTIONS)
    df = df[["location", "cmp", "att", "td", "int", "long", "rate"]]
    return df

def display_player_totals(players: list[Player]):
    #for player in players:
        #Get the player totals table
    player_totals, maxes = get_player_totals(players)
    
        #Display the table
    print(player_totals)
    print("\n-------------------------\n")
    print(maxes)
    
    return