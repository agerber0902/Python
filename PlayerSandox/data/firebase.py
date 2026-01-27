#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 19 14:13:52 2026

Firebase Base Class with CRUD operations for database

@author: andrewgerber
"""

#Define Imports
import firebase_admin
from firebase_admin import credentials, firestore, auth

class Firebase:
    def __init__(self, key_path: str = None):
        # Only initialize if no apps exist
        if not firebase_admin._apps:
            if key_path:
                cred = credentials.Certificate(key_path)
                firebase_admin.initialize_app(cred)
            else:
                firebase_admin.initialize_app()
            print("Firebase app initialized.")
        else:
            print("Firebase app already initialized, using existing app.")

        # Initialize Firestore and Auth clients
        self.db = firestore.client()
        self.auth = auth