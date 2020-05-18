# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 21:47:34 2019

@author: HP
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 21:47:02 2019

@author: HP
"""

import os
import sys
import Utils.common_utilities as utils
import numpy as np

os.chdir("..")
os.chdir("data")
file = sys.argv[1]
train_input,train_output,test_input,test_output = utils.json_reader(file)

def solve(inputData):
    array = inputData
    print(array)
    result = []
    for t in range(len(array)):
        test = np.array(array[t])
        test1 = test[0]
        a1 = [test1[0], test1[1]]
        a2 = [test1[2], test1[4]]
        result.append([a1] + [a2])
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