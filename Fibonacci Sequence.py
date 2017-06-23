
'''Enter a number and have the program generate the Fibonacci sequence to that number or to the Nth number.'''

def fibonacci(nth):
    
    lst = [1, 1]
    a = lst[0]
    b = lst[1]
    while len(lst) != nth:
        if len(lst) % 2 == 0:
            a += b
            lst.append(a)
        else:
            b += a
            lst.append(b)
    print lst[nth - 1]
    
def fibonacci_seq(num):
    
    lst = [1, 1]
    a = lst[0]
    b = lst[1]
    while num not in lst:
        if len(lst) % 2 == 0:
            a += b
            lst.append(a)
        else:
            b += a
            lst.append(b)
    print lst
