def get_without_index(index, lijst):
    return lijst[:index] + lijst[(1 + index):]

x = range(10)
print(get_without_index(4, x))