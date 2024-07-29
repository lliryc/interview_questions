#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the candies function below.
def candies(n, arr):
    cands = [0] * n
    if n == 0:
        return 0
    if n == 1:
        return 1
    if arr[0] <= arr[1]:
        cands[0] = 1
    if arr[n-1] <= arr[n-2]:
        cands[n-1] = 1
    for i in range(1,n-1):
        if arr[i-1] >= arr[i] <= arr[i+1]:
            cands[i] = 1
        if arr[i] > arr[i-1] and cands[i-1]>0:
            cands[i] = cands[i-1] + 1
    if arr[n-1] > arr[n-2] and cands[n-2] > 0:
        cands[n-1] = cands[n-2] + 1
    for i in range(n-2, -1, -1):
        if arr[i+1] < arr[i]:
             cands[i] = max(cands[i+1] + 1, cands[i])
    return sum(cands)

def minCandiesDistr(arr):
    n =  len(arr)
    if n == 0:
          return 0
    if n == 1:
         return 1
    cand = [0] * n
    if arr[0] <=arr[1]:
         cand[0] = 1
    if arr[n - 1] <= arr[n-2]:
         cand[n-1] =1
    # find mins and fill from left to right
    for i in range(1, n-1):
        if arr[i-1] >= arr[i] <= arr[i+1]:
            cand[i] = 1
        if arr[i] > arr[i-1] and cand[i-1] != 0:
            cand[i] = cand[i-1] + 1
    if arr[n - 1] > arr[n-2] and cand[n-2] != 0:
        cand[n-1] = cand[n-2] + 1
    # find max and fill from right to left
    # cand[i] == 0 or cand[i] > 0 cand[i] = (cand[i], cand[i+1] + 1)
    for i in range(n-2, -1, -1):
         if arr[i] > arr[i+1] and cand[i+1] != 0:
                 cand[i] = max( cand[i+1] +1, cand[i])
    return sum(cand)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # n = int(input())
    #
    # arr = []
    #
    # for _ in range(n):
    #     arr_item = int(input())
    #     arr.append(arr_item)

    # result = candies(n, arr)
    #
    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
    print(minCandiesDistr([2, 4, 2, 6, 1, 7, 8, 9, 2, 1]))
