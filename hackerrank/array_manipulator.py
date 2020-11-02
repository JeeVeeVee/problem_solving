import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    array = [0 for i in range(n)]
    for querie in queries:
        for i in range(querie[0] - 1, querie[1]):
            array[i] += querie[2]
        print(array)
    return max(array)

print(arrayManipulation(10, [[1, 2, 100], [2, 5, 100], [3, 4, 100]]))