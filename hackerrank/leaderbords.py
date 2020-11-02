#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    cur_max = len(scores)
    output = []
    for score in alice:
        scores = turn_into_set(scores)
        if decideRanking(scores, score) <= cur_max:
            scores.insert(decideRanking(scores, score) , score)
            cur_max = score
        print(scores)
        output.append(decideRanking(scores, score) + 1)
    return output

def turn_into_set(list) -> list:
    output =  []
    for i in list:
        if i in output:
            continue
        else:
            output.append(i)
    return output

def decideRanking(scores, score):
    for i in range(len(scores)):
        if scores[i] > score:
            continue
        else:
            return i
    return len(scores)

print(climbingLeaderboard([100, 100, 50, 40, 40, 20, 10], [5, 25, 50, 120]))