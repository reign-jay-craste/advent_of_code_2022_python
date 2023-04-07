#!/usr/bin/env python3
import os

# https://adventofcode.com/2022/day/4

# Day 4 : Camp Cleanup
# Scenario 1: Find pairs whose partners fully work on all the assigned sections
# Scenario 2: Need to include overlapping work assigned sections

# Input
# Assignment areas for the pair

input_default = os.path.join(os.path.dirname(os.path.abspath(__file__)),'day_4.txt')

def day4(input_path=input_default):

    if not os.path.exists(input_path):
        print("Error reading input!")
        exit()

    with open(input_path,"r") as input_file:
        
        full_assignment_cnt = 0
        overlap_pair_cnt = 0
        
        for pair_index,line in enumerate(input_file):
            elf_pair = line.split(",")
            if len(elf_pair)!=2:
                print("Mismatch pair format. Skipping pair #", pair_index )
                continue 
            
            # Maybe a better alternative is regex, but it may be too complex for such simple exercise
            start_section_1,end_section_1 = elf_pair[0].split("-")
            start_section_2,end_section_2 = elf_pair[1].split("-")

            # Convert to numeric
            start_section_1 = int(start_section_1) 
            end_section_1 = int(end_section_1)
            start_section_2 = int(start_section_2) 
            end_section_2 = int(end_section_2)

            # Need to swap the starting and ending if they are not in order 
            if start_section_1>end_section_1: start_section_1,end_section_1 = end_section_1,start_section_1
            if start_section_2>end_section_2: start_section_2,end_section_2 = end_section_2,start_section_2

            if ( start_section_1 <= start_section_2 and end_section_1 >= end_section_2 ) or  \
            ( start_section_1 >= start_section_2 and end_section_1 <= end_section_2 ):
                full_assignment_cnt+=1
                overlap_pair_cnt+=1

            elif ( start_section_1 <= start_section_2 and end_section_1 >= start_section_2 ) or  \
            ( start_section_2 <= start_section_1 and end_section_2 >= start_section_1 ):
                # Section 2 additional requirements
                overlap_pair_cnt+=1

        print("---- Day 4 : Camp Cleanup ----")
        print("Insufficient number of pairs found:" ,full_assignment_cnt)
        print("Insufficient number of pairs found including overlaps:" ,overlap_pair_cnt)
        print("------------------------------\n")

if __name__ == "__main__":
    day4()