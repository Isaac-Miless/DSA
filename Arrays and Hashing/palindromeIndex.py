#!/bin/python3

import math
import os
import random
import re
import sys




# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
def palindromeIndex(s):
    # Write your code here
    length = len(s)

    if s == s[::-1]:
        return -1
    # Find the index of the character to remove
    for i in range(length//2):
        if s[i] != s[length-1-i]:
            if s[i] == s[length-2-i] and s[i+1] == s[length-3-i]:
                return length-1-i
            else:
                return i  
    return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()
