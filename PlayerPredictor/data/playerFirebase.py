#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 19 14:39:35 2026

Player Firebase Class
Contains CRUD operations for the Player database
Inherits from Firebase Base Class

@author: andrewgerber
"""

#Define Imports
from .firebase import Firebase
from classes.playerInfo import PlayerInfo

class PlayerFirebase(Firebase):
    
    def __init__(self, key_path = None):
        #Initialize super
        super().__init__(key_path)
        
        #Initialize own fields
        self.collection_name = "players"
        self.collection = self.db.collection(self.collection_name)
        
    #Add Player to database
    def add_playerInfo(self, playerInfo: PlayerInfo):
        player = self.collection.where("url", "==", playerInfo.url).get()
        print(player)
        if player:
            #update
            self.update_playerInfo(player[1].id, playerInfo)
        else:
            self.collection.add(playerInfo.__dict__)
            print("Player Info Added")
        
    #Update Player in database
    def update_playerInfo(self, id: str, playerInfo: PlayerInfo):
        self.collection.document(id).update(playerInfo.__dict__)
        print(f"Player Info {id} updated.")