def get_index_smallest(i):
    output = 0
    cur_min = int(str(i)[0])
    teller = 0
    for j in str(i):
        if int(j) < cur_min:
            cur_min = int(j)
            output = teller
        teller += 1
    return output

def decide_smallest():
    pass

def smallest(n):
    index_smallest = get_index_smallest(n)
    if index_smallest == 0:
        smollest = int(str(n)[0] + str(smallest(str(n[1:])))[0])
    else:
        if str(n)[index_smallest] == "0":
            return