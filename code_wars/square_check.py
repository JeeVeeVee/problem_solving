def is_square(n):
    teller = 0
    while (teller ** 2) <= n:
        if (teller ** 2 == n):
            return True
        teller += 1
    return False