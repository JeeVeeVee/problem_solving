#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    output = 0
    for row in s:
        som = 0
        for i in row:
            som += i
        output += abs(15 - som)
        print(abs(15 - som))
    return output

formingMagicSquare([[2, 9, 8], [4, 2, 7], [5, 6, 7]])


