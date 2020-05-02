def count_patterns_from(firstPoint, length):
    if (length == 1):
        return 0
    if (length > 9):
        return 0

    corners = ["A", "C", "I", "G"]
    middles = ["B", "F", "H", "D"]
    midmid = ["E"]

