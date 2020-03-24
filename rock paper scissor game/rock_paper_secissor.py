# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 18:51:26 2020

@author: Saif
"""

#%% Importing necessary modules
import numpy as np
import random
from calc_result import calc_result

#%% initiating variables
play_mode = int(input("Select Mode :\n 1)Play VS Computer\n 2)Play VS friend\n==> "))
turn = int(input("Enter total number of turns ==>"))

#%% defining function
def calc_result(move1,move2):
    possible_moves = ['rock' , 'paper' , 'scissor']
    if move1 == possible_moves[0]:
        if move2 == possible_moves[1]:
            result = move2 + ' wins'
        else:
            result = move1 + ' wins'
    elif move1 == possible_moves[1]:
        if move2 == possible_moves[2]:
            result = move2 + ' wins'
        else:
            result = move1 + ' wins'
    elif move1 == possible_moves[2]:
        if move2 == possible_moves[0]:
            result = move2 + ' wins'
        else:
            result = move1 + ' wins'
    return result

#%% Starting pvp game
if play_mode == 2:
    current_turn = 0
    while current_turn < turn:
        player_1 = input("Player 1 type your turn ==> ")
        player_1 = player_1.lower()
        print("hiding player 1 move, waiting for player 2\n\n"*30)
        player_2 = input("Player 2 type your turn ==> ")
        player_2 = player_2.lower()
        if player_1 == player_2:
            result = "Tie"
        else:
            result = calc_result(player_1,player_2)
        current_turn += 1
        print(result)

#%% Starting vs computer        
if play_mode == 1:
    current_turn = 0
    while current_turn < turn:
        player = input("Player type your turn ==> ")
        player = player.lower()
        print("waiting for Computer\n\n"*5)
        computer = random.choice(['rock' , 'paper' , 'scissor'])
        if computer == player:
            result = "Tie"
        else:
            result = calc_result(player,computer)
        current_turn += 1
        print(result , '. [INFO] ..computer used ' + computer)

input()