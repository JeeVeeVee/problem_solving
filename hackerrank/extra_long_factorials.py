def extraLongFactorials(n):
    output = 1
    times_ten_counter = 0
    for i in range(1, n + 1):
        if (i % 10 == 0):
            times_ten_counter += 1
        else:
            output *= i
    for i in range(times_ten_counter):
        output *= 10
    return output

print(extraLongFactorials(25))