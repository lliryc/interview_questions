#!/bin/python3

import math
import os
import random
import re
import sys
import itertools

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    fulllst = sorted([sorted(s[i:j]) for i in range(0, len(s)) for j in range(i+1,len(s)+1)])
    print(fulllst)
    stat = list(filter(lambda i : i > 1,[len(list(v)) for (k,v) in itertools.groupby(fulllst)]))
    sm = sum([(i*(i-1))//2 for i in stat])
    return sm


def sherlockAnagrams2(s):
    l = len(s)
    substr_lst = sorted([sorted(s[i:j] ) for i in range(l) for j in range(i+1, l+1)])
    grouped_lst = [len(list(group)) for (k,group) in itertools.groupby(substr_lst)]
    grouped_list = filter(lambda k: k > 1, grouped_lst)
    return sum([i*(i-1)//2 for i in grouped_list])



if __name__ == '__main__':
    print(sherlockAnagrams2("ifailuhkqq"))
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # q = int(input())
    #
    # for q_itr in range(q):
    #     s = input()
    #
    #     result = sherlockAndAnagrams(s)
    #
    #     fptr.write(str(result) + '\n')
    #
    # fptr.close()
