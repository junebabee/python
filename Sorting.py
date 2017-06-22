
'''Implement two types of sorting algorithms: Merge sort and bubble sort.'''

# bubble sort

def bubble_sort(lst):
    
    n = len(lst)
    while n > 2: 
        for indx in range(n - 2):
            if lst[indx] > lst[indx + 1]:
                lst[indx], lst[indx + 1] = lst[indx + 1], lst[indx]
        n -= 1    
    return lst

# merge sort

from random import randint

def merge(lst1, lst2):
    
    new = []
    while lst1 and lst2:
        if lst1[0] < lst2[0]:
            new.append(lst1.pop(0))
        else:
            new.append(lst2.pop(0))
    new.extend(lst1)
    new.extend(lst2)
    return new

def merge_sort(lst):
    
    if len(lst) <= 1:
        return lst
    if len(lst) > 1:
        r = lst[randint(0, len(lst) -1)]
        left, mid, right = [], [], []
        for i in lst:
            if i < r:
                left.append(i)
            elif i == r:
                mid.append(i)
            else:
                right.append(i)
        
        left = merge_sort(left)
        left.extend(mid)
        right = merge_sort(right)
        
        return merge(left, right)
