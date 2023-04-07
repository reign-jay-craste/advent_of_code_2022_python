#!/usr/bin/env python3
import os

# https://adventofcode.com/2022/day/3

# Day 3 : Rucksack Reorganization
# Scenario 1: Find the sum of all the priorities for the misplaced/wrong items
# Scenario 2: Find the sum of priorities for group badges. Group badge is common for each 3 consecutive rucksacks

# Input
# Each character is the same item, and each rucksack (line) contains twewo compartment that are always
# the same size
# Each compartment should not have the same item on its pair compartment
# Each item has a priority value:
# a - z = 1 - 26
# A - Z = 27 - 52


def getPriority(item):
    value = -1
    if not item.isalpha():
        print("Unidentified item", item, "found!")
        return value
    
    if item.islower():
        value = ord(item) - 96 # ascii a = 97
    else:
        value = ord(item) - 64 + 26 # ascii A = 65

    return value

input_default = os.path.join(os.path.dirname(os.path.abspath(__file__)),'day_3.txt')

def day3(input_path = input_default):
    if not os.path.exists(input_path):
        print("Error reading input!")
        exit()

    with open(input_path,"r") as input_file:

        elf_group = []
        sum_wrong_item_priorities = 0
        sum_badge_priorities = 0

        for rucksack, line in enumerate(input_file):
            line = line.strip()
            if line=="":
                continue

            rucksack+=1

            compartments = line[:len(line)//2], line[len(line)//2:] # // to round for odd lengths 
            common_items = set.intersection(*map(set,compartments))

            for chr in common_items:
                sum_wrong_item_priorities += getPriority(chr)

            elf_group.append(line)
            if rucksack % 3 == 0:
                # if the list ends with a group less than 3, no badge will be calculated
                badge = set.intersection(*map(set,elf_group))
                for chr in badge:
                    sum_badge_priorities += getPriority(chr)
                elf_group = []

        print("---- Day 3 : Rucksack Reorganization ----")
        print("The sum of the priorities for the wrong items found were:" ,sum_wrong_item_priorities)
        print("The sum of the priorities for the group badges are:" ,sum_badge_priorities)
        print("-----------------------------------------\n")
if __name__ == "__main__":
    day3()