def matchingStrings(strings, queries):
    output = []
    for querie in queries:
        teller = 0
        for string in strings:
            if queries == string:
                teller += 1
        output.append(teller)
    return output