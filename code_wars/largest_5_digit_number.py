
def solution(digits):
    max = 0
    for i in range(len(digits) - 4):
        to_test = int(digits[i:i + 5])
        print(to_test)
        if to_test > max:
            max = to_test
    return max


number = "1234567898765"
print(solution(number))