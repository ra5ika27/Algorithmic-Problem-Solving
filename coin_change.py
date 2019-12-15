#!/bin/python3

import math
import os
import random
import re
import sys
def getWays(n, c):
    # Write your code here

    S = [0] * (n + 1)
    S[0] = 1
    m = len(c)
    for i in range(m):
        for j in range(c[i], n + 1):
            S[j] += S[j - c[i]]
    return S[n+1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    c = list(map(int, input().rstrip().split()))
    ways = getWays(n, c)
    fptr.write(str(ways) + '\n')

    fptr.close()
