#!/usr/bin/env python3
import os

# https://adventofcode.com/2022/day/2
# Day 2 : Rock Paper Scissors

# Scenario 1: Given a strategy for Rock Paper Scissors, input assumed to be what symbols to play
# Scenario 2: Strategy was actually suggestion when to win, lose or draw the game

# Input
# Each line is equivalent to round and what an elf might play. A,B,C for enemies and X,Y,Z are suggested strategy 
# A, X - Rock
# B, Y - Paper
# C, Z - Scissors

input_default = os.path.join(os.path.dirname(os.path.abspath(__file__)),'day_2.txt')

ROUND_WON = 6
ROUND_LOST = 0
ROUND_DRAW = 3

# Scenario 1
game_data = {
    # Assuming X = Rock, Y = Paper, Z = Scissors
    # [ equivalent_points, win_against, lose_against, draw]
    "X" : {
        "equivalent_points" : 1, 
        "win_against" : "C",
        "lose_against": "B",
        "draw": "A"
    },
    "Y" : {
        "equivalent_points" : 2, 
        "win_against" : "A",
        "lose_against": "C",
        "draw": "B"
    },
    "Z" : {
        "equivalent_points" : 3, 
        "win_against" : "B",
        "lose_against": "A",
        "draw": "C"
    }
}

# Scenario 2
additional_game_data = {
    # Correct assumptions; X = Need to lose, Y = need to draw, Z = need to win
    "A" : {
        "equivalent_points" : 1, 
        "win_against" : "Z",
        "lose_against": "Y",
        "draw": "X"
    },
    "B" : {
        "equivalent_points" : 2, 
        "win_against" : "X",
        "lose_against": "Z",
        "draw": "Y"
    },
    "C" : {
        "equivalent_points" : 3, 
        "win_against" : "Y",
        "lose_against": "X",
        "draw": "Z"
    }
}

def day2(input_path = input_default):
    # start this if running script alone
    if not os.path.exists(input_path):
        print("Error reading input!")
        exit()

    with open(input_path,"r") as input_file:
        
        total_assumed_score = 0
        total_score = 0

        for round, line in enumerate(input_file):
            round+=1
            enemy_play = ""
            suggested_play = ""
            score_to_add = 0

            if len(line.split())>1:
                enemy_play,suggested_play = line.split()
            else:
                print("Skipping round", round, "..", "Error parsing", line ,"!")
                continue

            # calculate assuming 2nd column is suggested play rock, paper, scissors
            if suggested_play in game_data.keys():
                if enemy_play == game_data[suggested_play]["win_against"]:
                    score_to_add += ROUND_WON
                elif enemy_play == game_data[suggested_play]["lose_against"]:
                    score_to_add += ROUND_LOST
                elif enemy_play == game_data[suggested_play]["draw"]:
                    score_to_add += ROUND_DRAW
                else:
                    print("Skipping round", round, "..", "Invalid enemy symbol", enemy_play)
                    continue
                
                score_to_add += game_data[suggested_play]["equivalent_points"]
                total_assumed_score += score_to_add
            else:
                print("Skipping round", round, "..", "Invalid player symbol", suggested_play)
                continue 

            # After the updated definition of the strategy, 2nd column is to either draw, lose, win
            score_to_add = 0
            if enemy_play in additional_game_data.keys():

                if suggested_play == "X":
                    # must lose
                    score_to_add += ROUND_LOST
                    symbol_to_play = additional_game_data[enemy_play]["win_against"]
                    score_to_add += game_data[symbol_to_play]["equivalent_points"]
                elif suggested_play == "Y":
                    # must draw
                    score_to_add += ROUND_DRAW
                    symbol_to_play = additional_game_data[enemy_play]["draw"]
                    score_to_add += game_data[symbol_to_play]["equivalent_points"]
                elif suggested_play == "Z":
                    # must win
                    score_to_add += ROUND_WON
                    symbol_to_play = additional_game_data[enemy_play]["lose_against"]
                    score_to_add += game_data[symbol_to_play]["equivalent_points"]
                else:
                    print("Skipping round", round, "..", "Invalid suggested play", suggested_play)
                    continue    
            else:                
                print("Skipping round", round, "..", "Invalid enemy symbol", enemy_play)
                continue               
            total_score += score_to_add

        print("---- Day 2 : Rock Paper Scissors ----")
        print("Scenario 1 assumption has a total score of:", total_assumed_score)    
        print("Scenario 2 using correct rules has a total score of:", total_score)  
        print("-------------------------------------\n")
        
if __name__ == "__main__":
    day2()