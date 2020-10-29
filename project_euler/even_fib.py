def fib():
    prev = 1
    prevprev = 0
    output = [0]
    newest = 0
    while(newest < 4000000):
        newest = prev + prevprev
        prev, prevprev = newest, prev
        output.append(newest)
    return output

print(fib())
even_sum = 0 
for i in fib():
    if i % 2 == 0:
        print(i)
        even_sum += i
print(even_sum)