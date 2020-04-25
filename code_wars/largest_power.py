import math

def largest_power(n):
    n = n - 1
    if n == 1:
        return (1, -1)
    output = 0
    for i in range(2, int(math.sqrt(n) + 1)):
        teller = 1
        while (i ** teller <= n):
            if i ** teller == n:
                output += 1
            teller += 1
    if output == 0:
        return largest_power(n - 1)
    elif (i ** teller == n):
        return largest_power(n - 1)

    else:
        return (n, output)

print(largest_power(6))

