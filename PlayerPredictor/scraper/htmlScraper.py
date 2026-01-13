#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  5 15:11:49 2026

Web Scraper that uses requests to and the input url to get html and return it

@author: andrewgerber
"""

#   Define Imports
import requests
from scraper.utils import doesExist, isValidType
from bs4 import BeautifulSoup
#-- Imports

#   Get the html soup from the url
def getHtmlSoupFromUrl(url):
    html = getPlayerHtmlFromUrl(url);
    
    #   If html does not exist, return None
    if not doesExist(html):
        print("No HTML was returned by the response.")
        return None
    
    #   Get the html soup
    print("Soup was created")
    return BeautifulSoup(html, features="html.parser")

#   Get the html page from the url
def getPlayerHtmlFromUrl(player_url):
    
    #   Validate url, if invalid return None
    if not isValidUrl(player_url):
        print(f"Player URL input is invalid: {player_url}")
        return None
    
    #   If URL is valid, return html
    try:
        html = getHtmlFromUrl(player_url)
        return html
    except:
        return None

#   Validate the url input
def isValidUrl(url):
    return doesExist(url) and isValidType(url, str)

#   Using requests, call the url and get the response data
def getHtmlFromUrl(url):
    response = requests.get(url)
    if not response:
        raise Exception("Response was not found.")
        return
    
    return response.text