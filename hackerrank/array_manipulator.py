def arrayManipulation(n, queries):
    line = []
    for i in range(n):
        line.append(0)
    for querie in queries:
        begin = querie[0] - 1
        end = querie[1]
        value = querie[2]
        for i in range(begin, end):
            line[i] += value
        print(line)

    return max(line)