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

PASSING_TOTAL_COLUMNS = ["cmp", "att", "td", "int"]
PASSING_MAX_COLUMNS = ["cmp", "att", "td", "int", "long", "rate"]

RUSHING_TOTAL_COLUMNS = ["rush_att", "rush_yds", "rush_td"]
RUSHING_MAX_COLUMNS = ["rush_att", "rush_td", "rush_long"]

RECEIVING_TOTAL_COLUMNS = ["rec", "targets", "rec_yds", "rec_td"]
RECEIVING_MAX_COLUMNS = ["rec", "targets", "rec_yds", "rec_td", "rec_long"]

def get_player_totals(players: list[Player]):
    passing_totals, passing_maxes = get_passing_totals(players)
    rushing_totals, rushing_maxes = get_rushing_totals(players)
    receiving_totals, receiving_maxes = get_receiving_totals(players)
    return passing_totals, passing_maxes, rushing_totals, rushing_maxes, receiving_totals, receiving_maxes
    

def get_receiving_totals(players: list[Player]):
    totals_rows = []
    maxes_rows = []

    for player in players:
        rows = []

        for game in player.games:
            if not game.passing_stats:
                continue
            rows.append(vars(game.receiving_stats))

        # skip players with no passing stats
        if not rows:
            continue

        df = DataFrame(rows)

        totals = df[RECEIVING_TOTAL_COLUMNS].sum()
        maxes = df[RECEIVING_MAX_COLUMNS].max()

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

def get_rushing_totals(players: list[Player]):
    totals_rows = []
    maxes_rows = []

    for player in players:
        rows = []

        for game in player.games:
            if not game.passing_stats:
                continue
            rows.append(vars(game.rushing_stats))

        # skip players with no passing stats
        if not rows:
            continue

        df = DataFrame(rows)

        totals = df[RUSHING_TOTAL_COLUMNS].sum()
        maxes = df[RUSHING_MAX_COLUMNS].max()

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




def get_player_games(games, is_passing: bool):#player: Player) -> DataFrame:
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
        if is_passing:
            row.update(vars(game.passing_stats))
        else:
            row.update(vars(game.total_stats))

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
    passing_totals, passing_maxes, rushing_totals, rushing_maxes, receiving_totals, receiving_maxes = get_player_totals(players)
    
        #Display the table
    print("PASSING:")
    print(passing_totals)
    print("\n-------------------------\n")
    print(passing_maxes)
    
    print("\nRUSHING")
    print(rushing_totals)
    print("\n-------------------------\n")
    print(rushing_maxes)
    
    print("\nRECEIVING")
    print(receiving_totals)
    print("\n-------------------------\n")
    print(receiving_maxes)
    
    
    return