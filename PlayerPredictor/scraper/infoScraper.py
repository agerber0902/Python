#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 18 13:36:24 2026

@author: andrewgerber
"""

#Define Imports
import re
from classes.playerInfo import PlayerInfo

def info_scraper(url: str, html_soup):
    # Find the meta div
    meta = html_soup.find("div", id="meta")
        
    if not meta:
        print("No meta tag found for player info.")
    
    # Get Name Tag
    name_tag = meta.find("h1")
    player_name = name_tag.text.strip() if name_tag else None
    
    # Get info fields
    position = None
    team = None 
    height = None 
    weight = None 
    college = None
    drafted_team  = None
    
    #Iterate through all p elements
    for p in meta.find_all("p"):
        
        # Get p text
        text = p.get_text(" ", strip=True)
        
        # Position
        if text.startswith("Position"):
            position = text.replace("Position:", "").replace("Position :", "").split("▪")[0].strip()[0:2]
        
        # Team
        a = p.find("a")
        if text.startswith("Team") and a and a.get("href", "").startswith("/teams/"):
            team = a.text.strip()
            
        #Height and Weight
        if "lb" in text and "cm" in text:
            height_match = re.search(r"(\d+-\d+)", text)
            weight_match = re.search(r"(\d+)\s*lb", text)

            if height_match:
                height = height_match.group(1)
            if weight_match:
                weight = weight_match.group(1)
            
        # Drafted Team
        if text.startswith("Draft"):
            round_match = re.search(r"(\d+)(?:st|nd|rd|th)\s+round", text)
            pick_match = re.search(r"\((\d+)(?:st|nd|rd|th)\s+overall\)", text)
            year_match = re.search(r"(\d{4})", text)
            
            team_link = p.find("a", href=lambda h: h and h.startswith("/teams/"))
            if team_link:
                drafted_team = team_link.text.strip()
            
            if round_match:
                draft_round = int(round_match.group(1))
            if pick_match:
                draft_pick = int(pick_match.group(1))
            if year_match:
                draft_year = int(year_match.group(1))
            
        # College
        if text.startswith("College"):
            label = p.find("strong")
            
            if label and label.text.strip() == "College":
                colleges = []
            
                for elem in label.next_siblings:
                    # STOP when we hit High School
                    if getattr(elem, "name", None) == "strong" and "High School" in elem.text:
                        break
            
                    # Collect college links only
                    if getattr(elem, "name", None) == "a" and elem.get("href", "").startswith("/schools/"):
                        colleges.append(elem.text.strip())
            
                college = colleges[-1] if colleges else ""
            
            
    player_info = PlayerInfo(url = url, name = player_name, team = team, position = position, height = height, weight = weight, college = college, draftedTeam = drafted_team)
    return player_info