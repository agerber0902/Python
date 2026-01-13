#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  5 13:46:07 2026

Utility functions
    - Data Validation
        - Exists
        - Type
    - Safe Get

@author: andrewgerber
"""
#   Define Imports
#-- Imports

#   Validate the value exists
def doesExist(value):
    return True if value not in (None, "", " ") else False

#   Validate value based on input type
def isValidType(value, valueType):
    return True if isinstance(value, valueType) else False
