def get_without_index(index, lijst):
    return lijst[:index] + lijst[(1 + index):]

def duplicate_count(text):
    text = text.upper()
    checked = []
    output = 0
    for i in range(len(text)):
        if text[i] not in checked and text[i] in get_without_index(i, text):
            output += 1
        checked.append(text[i])
    return output
        