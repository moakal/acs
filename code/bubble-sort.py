# bubble sort ascending
# 24/02/2022

import random

l = [random.randint(0, 100) for i in range(20)]
n = len(l)

print(l)

def bubbleSort(l):
    for i in range(0, n - 1):
        for j in range(0, n - i - 1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
    print(l)

bubbleSort(l)