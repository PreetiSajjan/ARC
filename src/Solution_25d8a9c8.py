# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 21:43:42 2019

@author: Preeti Sajjan
"""

import os
import sys
import Utils.common_utilities as utils

os.chdir("..")
os.chdir("data")
file = sys.argv[1]
train_input,train_output,test_input,test_output = utils.json_reader(file)

def solve(inputData):
    array = inputData
    solution = inputData
    for i in range(len(array)):
        for j in range(len(array[i])):
            if(len(set(array[i][j]))==1):
                solution[i][j] = [5, 5, 5]
            else:
                solution[i][j] = [0, 0, 0]   
    return solution

##training
print("\n\nTraining")
output = solve(train_input)
print(" Output: \n", output)
if(train_output == output):
    print("Training Data Verified!!!")

##training
print("\n\nTesting")
output = solve(test_input)
print(" Output: \n", output)
if(test_output == output):
    print("Testing Data Verified!!!")