fib1 = 1
fib2 = 2

n = input('Which value of element of the \
Fibonacci sequence do you want to know? n = ')
n = int(n)  # transform into an integer number


if n == 1 or n == 0:
    print (fib1)
elif n == 2:
    print (fib2)
elif n > 2:
    i = 2
    while i < n:
        fib_sum = fib2 + fib1
        fib1 = fib2
        fib2 = fib_sum
        i += 1
    print (fib_sum)
else:
    print ('The specified number should be positive')
