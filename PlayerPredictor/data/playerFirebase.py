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

from google.cloud.firestore_v1 import FieldFilter

class PlayerFirebase(Firebase):
    
    def __init__(self, key_path = None):
        #Initialize super
        super().__init__(key_path)
        
        #Initialize own fields
        self.collection_name = "players"
        self.collection = self.db.collection(self.collection_name)
        
    # Get Player by player name
    def get_player_info_by_name(self, name: str) -> PlayerInfo:
        player = next(
            self.db.collection(self.collection_name)
            .where(filter=FieldFilter("name", "==", name.title()))
            .limit(1)
            .stream(),
            None
        )
        
        if player is None:
            print("No player found")
            return None
        else:
            return PlayerInfo(**player.to_dict())

        
    #Add Player to database
    def add_playerInfo(self, playerInfo: PlayerInfo):
        try:
            player = next(
                self.db.collection(self.collection_name)
                .where(filter=FieldFilter("url", "==", playerInfo.url))
                .limit(1)
                .stream(),
                None
            )
            
            if player:
                #update
                #self.update_playerInfo(player[1].id, playerInfo)
            else:
                self.collection.add(playerInfo.__dict__)
                print("Player Info Added")
        except:
            print("An error occured adding player info.")
        
    #Update Player in database
    def update_playerInfo(self, id: str, playerInfo: PlayerInfo):
        self.collection.document(id).update(playerInfo.__dict__)
        print(f"Player Info {id} updated.")