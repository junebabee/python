
'''Start with a number n > 1. Find the number of steps it takes to reach one using the following process: 
If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1.'''

n = int(raw_input('Please input an nonnegative integer: '))

while n > 1:
    
    if n % 2 == 0:
        n = n / 2
    else:
        n = 3 * n + 1
    print n
