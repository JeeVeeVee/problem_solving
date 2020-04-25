def twoStacks(x, a, b):
    print(x, a ,b)
    if (a[0] > x):
        if(b[0] > x):
            return 0
        else:
            return 1 + twoStacks(x - b[0], a, b[1:])
    elif (b[0] > x):
        if(a[0] > x):
            return 0
        else:
            return 1 + twoStacks(x - a[0], a[1:], b)
    else:
        return  1 + max(twoStacks(x - a[0], a[1:], b), twoStacks(x - b[0], a, b[1:]))

print(twoStacks(10, [4,2,4,6,1], [2,1, 8, 5]))