#!/usr/bin/env python3
import os
import re
from copy import deepcopy

# https://adventofcode.com/2022/day/5

# Day 5 : Supply Stacks
# Scenario 1: Like a tower of Hanoi but with instructions what moves to play, need to identify top most crates
# Scenario 2: Orders will be moved as-is their initial positioning

# Input
# Assignment areas for the pair
# [x] = crates (with number below them)
# move {n_crates} from {source_column} to {destination_column}

input_default = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'day_5.txt')
row_pattern = re.compile(r'(.{4}|.{3})')
crate_dict_1 = {}
crate_dict_2 = {}

def day5(input_path = input_default):
    if not os.path.exists(input_path):
        print("Error reading input!")
        exit()

    with open(input_path,"r") as input_file:
        move_list_found = False
        crate_stack = []

        for index,line in enumerate(input_file):
            
            if line.strip()=="":
                continue

            if "move" not in line:
                
                if move_list_found == True:
                    # ends except for whitespaces
                    break 
                else:
                    crate_stack.append([])
                    last_row = len(crate_stack)-1
                    
                    for match in row_pattern.finditer(line):
                        crate_stack[last_row].append(match.group(1).strip().strip("[").strip("]"))

                continue

            elif "move" in line and not move_list_found:
                # create a dictionary to use as reference 
                move_list_found = True
                for col, key in enumerate(crate_stack[last_row]):
                    crate_dict_1[key] = []

                    for row in reversed(crate_stack[:-1]):
                        crate = row[col]        
                        if crate=="":
                            break               
                        crate_dict_1[key].append(crate)

                crate_dict_2 = deepcopy(crate_dict_1) # because array objects are copied as pointers using other methods

            if move_list_found:
                # move crates in the array as per instructions
                move_pattern = "move (\d+) from (\d+) to (\d+)"
                match = re.match(move_pattern,line)

                if match:
                    n_crates, source, destination = match.groups()
                    n_crates = int(n_crates)

                    try:
                        crate_dict_1[destination].extend(reversed(crate_dict_1[source][-n_crates:]))
                        crate_dict_1[source] = crate_dict_1[source][:-n_crates]

                        crate_dict_2[destination].extend(crate_dict_2[source][-n_crates:])
                        crate_dict_2[source] = crate_dict_2[source][:-n_crates]

                    except KeyError as e:
                        print("Error:", e )
                    
        top_crates = ""
        top_crates_2 = ""

        # list top most crates
        for col, key in enumerate(crate_stack[last_row]):
                
                col_size =  len(crate_dict_1[key]) - 1
                if col_size < 0:
                    top_crates+=" "
                else:
                    top_crates+=crate_dict_1[key][col_size]

                # Scenario 2
                col_size =  len(crate_dict_2[key]) - 1
                if col_size < 0:
                    top_crates_2+=" "
                else:
                    top_crates_2+=crate_dict_2[key][col_size]

        print("---- Day 5 : Supply Stacks ----")
        print("The top crates after the activity are:", top_crates)
        print("The top crates after the activity for CrateMover 9001 are:", top_crates_2)
        print("-------------------------------\n")
        
if __name__ == "__main__":
    day5()