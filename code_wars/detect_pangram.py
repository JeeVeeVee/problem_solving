import string
def is_pangram(s):
    s = s.lower()
    alfabet = "abcdefghijklmnopqrstuvwxyz"
    to_check = []
    for letter in alfabet:
        to_check.append(letter in s)

    for check in to_check:
        if check:
            continue
        else:
            return False
    return True
