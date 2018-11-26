n = input('''What distance do you want to cover \
with 1, 2 and 3 steps.? n = ''')
n = int(n)

def recursive(n):
    if n in range(1, 4):
        initial = [1, 2, 4]
        return initial[n-1]
    elif n == 0:
        initial = [1]
        return initial[n-1]
    elif n >= 4:
        return recursive(n-1) + recursive(n-2) + recursive(n-3)
    else:
        print('The specified number should be positive')
print (recursive (n))