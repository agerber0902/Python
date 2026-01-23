#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 22 17:25:17 2026

Trivia Helper that contains all functionality for player trivia

@author: andrewgerber
"""

# Define Imports
import random
import os
import time

from data.playerFirebase import PlayerFirebase
from classes.playerInfo import PlayerInfo
from classes.question import Question

def generate_question(player: PlayerInfo, players: list[PlayerInfo], category: str, isPlayerQuestion: bool) -> Question:
    if category == "team":
        question = (f"What player plays for {player.team}?" if player.team != None else "What player is a free agent?") if isPlayerQuestion else f"What team does {player.name} play for?"
        correct = player.name if isPlayerQuestion else player.team if player.team != None else "Free Agent"
        
        if isPlayerQuestion:
            wrong_answers = random.sample(
                [p.name for p in players if p.team != player.team],
                k=min(3, len(players) - 1)
            )
        else:
            wrong_answers = random.sample(
                [p.team if p.team != None else "Free Agent" for p in players if p.team != player.team],
                k=min(3, len(players) - 1)
            )
            
        answers = [correct] + wrong_answers
        random.shuffle(answers)
        return Question(question = question, answers = answers, correct = correct)
    elif category == "position":
        question = f"What player plays {player.position}?" if isPlayerQuestion else f"What position does {player.name} play?"
        correct = player.name if isPlayerQuestion else player.position
        
        if isPlayerQuestion:
            wrong_answers = random.sample(
                [p.name for p in players if p.position != player.position],
                k=min(3, len(players) - 1)
            )
        else:
            wrong_answers = ["QB", "RB", "WR", "TE"]
            
        answers = [correct] + wrong_answers
        random.shuffle(answers)
        return Question(question = question, answers = answers, correct = correct)
        
    elif category == "college":
        question = f"What player finished college at {player.college}" if isPlayerQuestion else f"What college did {player.name} play for last?"
        correct = player.name if isPlayerQuestion else player.college
        
        if isPlayerQuestion:
            wrong_answers = random.sample(
                [p.name for p in players if p.college != player.college],
                k=min(3, len(players) - 1)
            )
        else:
            wrong_answers = random.sample(
                [p.college for p in players if p.college != player.college],
                k=min(3, len(players) - 1)
            )
            
        answers = [correct] + wrong_answers
        random.shuffle(answers)
        return Question(question = question, answers = answers, correct = correct)
    elif category == "draftedTeam":
        question = (f"What player was drafted by {player.draftedTeam}" if player.draftedTeam != None else "What player went undrafted?") if isPlayerQuestion else f"What team drafted {player.name}?"
        correct = player.name if isPlayerQuestion else player.draftedTeam if player.draftedTeam != None else "Undrafted Free Agent"
        
        if isPlayerQuestion:
            wrong_answers = random.sample(
                [p.name for p in players if p.draftedTeam != player.draftedTeam],
                k=min(3, len(players) - 1)
            )
        else:
            wrong_answers = random.sample(
                [p.draftedTeam if p.draftedTeam != None else "Undrafted Free Agent" for p in players if p.draftedTeam != player.draftedTeam],
                k=min(3, len(players) - 1)
            )
            
        answers = [correct] + wrong_answers
        random.shuffle(answers)
        return Question(question = question, answers = answers, correct = correct)
    else:
        print(f"No category for: {category}")
        return None
    
def generate_questions(players: list[PlayerInfo]) -> list[Question]:
    questions: list[Question] = []
    
    for player in players:
        n = random.choice([1, 2])
        questions.append(generate_question(player, players, 'team', n == 1))
        questions.append(generate_question(player, players, 'position', n == 1))
        questions.append(generate_question(player, players, 'college', n == 1))
        questions.append(generate_question(player, players, 'draftedTeam', n == 1))
    
    random.shuffle(questions)
    return questions

def start_trivia(firebase: PlayerFirebase):
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("Player Trivia starting.. getting players..")
    
    #Get players
    players = firebase.get_players()
    
    #Generate questions
    questions = generate_questions(players)
    num_questions = len(questions)
    print(f"{num_questions} questions generated. Loading trivia..")
    
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    score = 0
    game_over = False
    while game_over == False:
        for question in questions:
            print(f"""\n\n
\t\t\t\t\tPlayer Trivia
--------------------------------------------------------
Score: {score}\t\t\t\t\t\t\t\t Question: {score}/{num_questions}

    {question.question}
        1. {question.answers[0]}
        2. {question.answers[1]}
        3. {question.answers[2]}
        4. {question.answers[3]}
    """)
        
            while True:
                user_answer = input("Answer (1–4): ")
            
                if user_answer.isdigit() and user_answer in ["1", "2", "3", "4"]:
                    answer_value = int(user_answer) - 1
                    break
            
                print("Invalid input, try again.")
        
            if(question.answers[answer_value] == question.correct):
                print("Correct! Incoming question..")
                score += 1
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')
            else:
                print(f"Incorrect, it's {question.correct}")
                game_over = True
                break;
    
    if(score == num_questions):
        print("Congratulations! Trivia Complete!")
              

    
    
    