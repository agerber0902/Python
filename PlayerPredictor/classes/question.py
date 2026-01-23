#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 22 17:43:49 2026

Trivia Question Class that contains the answers, correct answer, and question

@author: andrewgerber
"""
from dataclasses import dataclass

@dataclass
class Question:
    
    question: str
    answers: list[str]
    correct: str