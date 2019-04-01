
'''
    -*- coding: utf-8 -*-
    Python Version: 3.6
    Course: GEOG5790M Programming-for-Spatial-Analysts-Advanced-Skills
    Author: Annabel Whipp
    File name: ca.py
   
'''

# import random
import random

# variables

number_of_iterations = 10
width = 10
height = 10
fire_start_x = 4
fire_start_y = 4
fuel_amount = 5

# building the environment
environment = []
results = []
for h in range(height):
    row = []
    results_row = []
    for w in range(width):
        row.append(fuel_amount)
        results_row.append(fuel_amount)
    environment.append(row)
    results.append(results_row)

# iterations
for step in range(number_of_iterations):
    for h in range(1, height - 1):
        for w in range(1, width - 1):
            fire = False
            if (environment[h-1][w-1] < fuel_amount): fire = True 
            if (environment[h-1][w] < fuel_amount): fire = True 
            if (environment[h-1][w+1] < fuel_amount): fire = True 
            if (environment[h][w-1] < fuel_amount): fire = True 
            if (environment[h][w] < fuel_amount): fire = True 
            if (environment[h][w+1] < fuel_amount): fire = True
            if (environment[h+1][w-1] < fuel_amount): fire = True 
            if (environment[h+1][w] < fuel_amount): fire = True 
            if (environment[h+1][w+1] < fuel_amount): fire = True 
            if (fire == True) & (environment[h][w] > 0): 
                results[h][w] -= 1

# adding a stopping conditions 
# we can add a stopping condition and print out the number of iterations
# that it takes to end

environment = results
print (environment)
total = 0
for h in range(1, height - 1): 
    for w in range(1, width - 1): 
        total += environment[h][w]
if (total == 0):
    print("ends at iteration ", step)
    pass

