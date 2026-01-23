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

def generate_player_team_question(player: PlayerInfo, players: list[PlayerInfo]) -> Question:
    player_team_question = f"What team does {player.name} play for?"
    
    # pick 3 random players excluding the current one
    wrong_answers = random.sample(
        [p.team if p.team != None else "Free Agent" for p in players if p.team != player.team],
        k=min(3, len(players) - 1)
    )
    correct = player.team if player.team != None else "Free Agent"
    answers = wrong_answers + [correct]
    random.shuffle(answers)
    question = Question(question = player_team_question, answers = answers, correct=correct)
    return question

def generate_player_position_question(player: PlayerInfo, players: list[PlayerInfo]) -> Question:
    player_position_question = f"What position does {player.name} play?"
    
    answers = ["QB", "RB", "WR", "TE"]
    random.shuffle(answers)
    question = Question(question = player_position_question, answers = answers, correct=player.position)
    return question

def generate_player_college_question(player: PlayerInfo, players: list[PlayerInfo]) -> Question:
    player_college_question = f"What college did {player.name} play for last?"
    
    # pick 3 random players excluding the current one
    wrong_answers = random.sample(
        [p.college for p in players if p.college != player.college],
        k=min(3, len(players) - 1)
    )

    answers = wrong_answers + [player.college]
    random.shuffle(answers)
    question = Question(question = player_college_question, answers = answers, correct=player.college)
    return question

def generate_player_drafted_team_question(player: PlayerInfo, players: list[PlayerInfo]) -> Question:
    question = f"What team drafted {player.name}?"
    
    # pick 3 random players excluding the current one
    wrong_answers = random.sample(
        [p.draftedTeam if p.draftedTeam != None else "Undrafted" for p in players if p.draftedTeam != player.draftedTeam],
        k=min(3, len(players) - 1)
    )

    correct = player.draftedTeam if player.draftedTeam != None else "Undrafted"
    answers = wrong_answers + [correct]
    random.shuffle(answers)
    return Question(question = question, answers = answers, correct=correct)

def generate_drafted_team_question(player: PlayerInfo, players: list[PlayerInfo]) -> Question:
    question = f"What player was drafted by {player.draftedTeam}" if player.draftedTeam != None else f"What player went undrafted?"
    
    # pick 3 random players excluding the current one
    wrong_answers = random.sample(
        [p.name for p in players if p != player],
        k=min(3, len(players) - 1)
    )

    answers = wrong_answers + [player.name]
    random.shuffle(answers)
    return Question(question = question, answers = answers, correct=player.name)

def generate_team_question(player: PlayerInfo, players: list[PlayerInfo]) -> Question:
    team_question = f"What player plays for {player.team}?" if player.team != None else f"What player is a free agent?"
    
    # pick 3 random players excluding the current one
    wrong_answers = random.sample(
        [p.name for p in players if p.team != player.team],
        k=min(3, len(players) - 1)
    )
    
    answers = wrong_answers + [player.name]
    random.shuffle(answers)
    return Question(question = team_question, answers = answers, correct=player.name)
    
def generate_position_question(player: PlayerInfo, players: list[PlayerInfo]) -> Question:
    position_question = f"What player plays {player.position}?"
    
    # pick 3 random players excluding the current one
    wrong_answers = random.sample(
        [p.name for p in players if p.position != player.position],
        k=min(3, len(players) - 1)
    )
    answers = wrong_answers + [player.name]
    random.shuffle(answers)
    return Question(question = position_question, answers = answers, correct=player.name)

def generate_college_question(player: PlayerInfo, players: list[PlayerInfo]) -> Question:
    college_question = f"What player finished college at {player.college}"
    
    # pick 3 random players excluding the current one
    wrong_answers = random.sample(
        [p.name for p in players if p.college != player.college],
        k=min(3, len(players) - 1)
    )
    answers = wrong_answers + [player.name]
    random.shuffle(answers)
    return Question(question = college_question, answers = answers, correct=player.name)

def generate_questions(players: list[PlayerInfo]) -> list[Question]:
    questions: list[Question] = []
    
    for player in players:
        n = random.choice([1, 2])
        if n == 1:
            questions.append(generate_team_question(player, players))
            questions.append(generate_position_question(player, players))
            questions.append(generate_college_question(player, players))
            questions.append(generate_drafted_team_question(player, players))
        else:
            questions.append(generate_player_team_question(player, players))
            questions.append(generate_player_position_question(player, players))
            questions.append(generate_player_college_question(player, players))
            questions.append(generate_player_drafted_team_question(player, players))
    
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
              

    
    
    