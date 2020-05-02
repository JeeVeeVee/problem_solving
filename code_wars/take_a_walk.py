def is_valid_walk(walk):
    if len(walk) != 10:
        return False
    hor_counter = 0
    ver_counter = 0
    for dir in walk:
        if dir == "w":
            hor_counter += 1
        elif dir == "e":
            hor_counter += -1
        elif dir == "s":
            ver_counter -= 1
        elif dir == "n":
            ver_counter += 1
    return hor_counter == 0 and ver_counter == 0