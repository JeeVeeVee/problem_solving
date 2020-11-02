first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)


alfabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
text = []
for i in range(m):
    for j in range(n):
        text.append(matrix[j][i])
output = ""
teller = 0
while teller < len(text):
    nieuw_teken = text[teller]
    aanhangsel = ""
    if nieuw_teken in alfabet:
        aanhangsel = ""
        output += nieuw_teken
        teller += 1
    else:
        while (teller < len(text) and text[teller] not in alfabet):
            aanhangsel += text[teller]
            teller += 1
        if teller == len(text):
            output += aanhangsel
        else:
            output += " "
print(output)
