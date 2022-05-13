# insertion sort
# 24/02/2022

import random

l = [random.randint(0, 100) for i in range(20)]
n = len(l)

print(l)

def insertionSort(l):
    for i in range(1, n):
        k = l[i]
        j = i - 1
        while j >= 0 and k < l[j] :
                l[j + 1] = l[j]
                j -= 1
        l[j + 1] = k
    print(l)

insertionSort(l)