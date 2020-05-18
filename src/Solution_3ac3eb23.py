# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 21:41:42 2019
@author: HP
"""

import numpy as np
import os
import sys
import Utils.common_utilities as utils

os.chdir("..")
os.chdir("data")
file = sys.argv[1]
train_input,train_output,test_input,test_output = utils.json_reader(file)
    
def solve(inputData):
    array = inputData
    result = []
    for t in range(len(array)):
        test = np.array(array[t])
        a1 = test[0].tolist()
        a_temp = a1
        a2 = test[0].tolist()
        i = 0
        while i < len(a2):
            if a2[i] != 0:
                temp = a2[i]
                a2[i-1] = temp
                a2[i] = 0
                a2[i+1] = temp
                i = i + 2
            else:
                i = i + 1
        y = []
        for l in range(len(array[t])):
            if(l % 2 == 0):
                y = y + [a_temp]
            else:
                y = y + [a2]
        result = result + [y]
    return result

print("\n\nTRANING")
result = solve(train_input)
print(" Output:\n",result)
if(train_output == result):
    print("Training Successful")


print("\n\nTESTING")
result = solve(test_input)
print(" Output:\n",result)
if(test_output == result):
    print("Testing Successful\n")