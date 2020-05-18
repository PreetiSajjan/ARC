# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 21:49:11 2019

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
    solution = []
    for i in range(len(array)):
        temp_y = []
        for j in range(len(array[i])):
            ratio = (int)(len(array[i][j])/3)
            temp_y = temp_y + [array[i][j][:ratio]]
        solution = solution + [temp_y]   
    return solution

##training
print("\n\nTraining")
output = solve(train_input)
print("Output:\n", output)
if(train_output == output):
    print("Training Data Verified!!!")

##training
print("\n\nTesting")
output = solve(test_input)
print("Output:\n", output)
if(test_output == output):
    print("Testing Data Verified!!!\n")