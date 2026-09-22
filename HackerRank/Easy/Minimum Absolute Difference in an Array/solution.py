# HackerRank Problem: Minimum Absolute Difference in an Array
# Link: https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem
# Difficulty: Easy
# Language: python3

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumAbsoluteDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def minimumAbsoluteDifference(arr):
    # Write your code here
    arr.sort()
    n = len(arr)
    mini = float('inf')
    for i in range(1,n):
        mini = min(mini, abs(arr[i-1]-arr[i]))
    return mini
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
