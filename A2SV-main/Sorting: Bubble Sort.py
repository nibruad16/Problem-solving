#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    co =0
    for i in range(0 , len(a)-1):
        for j in range(len(a)-1):
            if a[j] > a[j+1]:
                a[j] , a[j+1] = a[j+1],a[j]
                co += 1
    return co

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    k = countSwaps(a)
    print("Array is sorted in" , k , "swaps.")
    print("First Element:",min(a))
    print("Last Element:",max(a))
