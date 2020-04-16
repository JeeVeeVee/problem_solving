#!/bin/python3


#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    output = []
    for i in s:
        output.append([i])
    vorige_output = []
    teller = 0
    while(output != vorige_output):
        teller += 1
        vorige_output = output
        for list in output:
            for i in s:
                if not (i in list):
                    add = True
                    for j in list:
                        if ((i + j) % k == 0):
                            add = False
                    if add:
                        list.append(i)
        for list in output:
            if len(list) <= teller:
                output.remove(list)
        print(output)
    return len(output[0])

print(nonDivisibleSubset(10, [770528134, 663501748, 384261537, 800309024, 103668401, 538539662, 385488901, 101262949, 557792122, 46058493]))



