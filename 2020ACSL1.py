#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'sumOfLastRow' function below.
#
# The function is expected to return a CHARACTER.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING d
#  3. INTEGER r
#

def sumDigit(listNum):
    listStr = ''.join([hex(i)[2:] for i in listNum])
    while len(listStr) > 1:
        summer = sum([int(i, 16) for i in listStr])
        listStr = hex(summer)[2:]
    return listStr[0].upper()


def sumOfLastRow(s, d, numRow):
    start = int(s, 16)
    delta = int(d, 16)
    for i in range(1, numRow-1):
        start += delta*(i+1)
    lastRow = [start+(i+1)*delta for i in range(numRow)]
    return sumDigit(lastRow)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input().strip()

    d = input().strip()

    r = int(input().strip())

    result = sumOfLastRow(s, d, r)

    # fptr.write(str(result) + '\n')

    # fptr.close()
    print(str(result))
