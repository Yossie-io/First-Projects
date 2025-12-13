
fib = [0, 1]
range = int(input('How many terms in the sequence do you want to output'))
while len(fib) < range:
    index1 = len(fib) - 2
    index2 = len(fib) - 1
    next = int(fib[index1]) + int(fib[index2])
    fib.append(next)
print(fib)