# HackerRank Problem: Palindrome Index
# Link: https://www.hackerrank.com/challenges/palindrome-index/problem
# Difficulty: Easy
# Language: python3

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
# aaab

def palindromeIndex(s):
    if s == s[::-1]:
        return -1
    n = len(s) 
    l = 0
    r = n-1
    while l < r:
        if s[l] == s[r]:
            l+=1
            r-=1
        else:
            str1 = s[:l]+s[l+1:] 
            str2 = s[:r]+s[r+1:] 
            if str1 == str1[::-1]:
                return l
            elif str2 == str2[::-1]:
                return r
    return -1
    
    ''' while l < r:
        str1 = s[:l]+s[l+1:]
        str2 = s[:r]+s[r+1:]
        if str1 == str1[::-1]:
            return l
        elif str2 == str2[::-1]:
            return r
        l+=1
        r-=1
    return -1 '''
    ''' for i in range(n):
        str = s[:i]+s[i+1:]
        if str == str[::-1]:
            return i
    return -1 '''
    
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()
