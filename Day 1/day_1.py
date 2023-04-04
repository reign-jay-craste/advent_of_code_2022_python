#!/usr/bin/env python3

# https://adventofcode.com/2022/day/1
# Day 1 : Calorie counting

# Scenario 1: Calculate maximum calorie brought by 1 elf
# Scenario 2: Calculate maximum calorie of top 3 elves

# Input
# Each line consists of calories for all the foods brought by each elves. Empty lines separates each elves.

if __name__ == "__main__":
    # start this if running script alone
    # input file should be day_1.txt
    with open('day_1.txt',"r") as input_file:
        elf = []
        total_calories = 0
        for line in input_file:
            if line.strip()=="":
                elf.append(total_calories)
                total_calories = 0
            else:
                if line.strip().isnumeric():
                    total_calories += int(line.strip())
                else:
                    #error
                    print("ERROR, non numeric data found. Skipping..")
        
        if total_calories!=0: 
            elf.append(total_calories)
            total_calories = 0

        if len(elf)>1:
            # One must also consider what if, there were multiple elves having the same total?
            max_calories = max(elf)

            print("The maximum calories the an elf has is: ",max_calories)

            # Scenario 1
            index = [i+1 for i in range(len(elf)) if elf[i] == max_calories]
            if len(index)>1:
                print("The elves that has the highest number of calories are elves:", index)
            else:
                print("The elf that has the highest number of calories is", index)

            # Scenario 2
            n = 3
            sorted_calories = sorted(elf,reverse=True) #if you need unique calorie values, use set(elf) instead
            top_n_total = sum(sorted_calories[:3])
            
            print("The total for the top", n, "calories an elf carry is",top_n_total)