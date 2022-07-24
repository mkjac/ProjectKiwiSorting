from select import select
import string
import time
import numpy as np

with open('kiwidata.txt') as file:
    text = file.read()
split = text.split(',')
split.remove('')

for s in split:
    s = float(s)

def BubbleSort(split):
    global bubbleSortTime
    startTime = time.time()
    n = len(split)
    swapped = False
    for i in range(n-1):
        for j in range(0, n-i-1):
            if split[j] > split[j + 1]:
                swapped = True
                split[j], split[j + 1] = split[j + 1], split[j]
         
        if not swapped:
            return
    endTime = time.time()
    bubbleSortTime = np.round_(time.time() - startTime, 3)

def SelectionSort(split):
    global selectionSortTime
    startTime = time.time()
    for i in range(len(split)):
  
        min_idx = i
        for j in range(i+1, len(split)):
            if split[min_idx] > split[j]:
                min_idx = j
    
        split[i], split[min_idx] = split[min_idx], split[i]
    selectionSortTime = np.round_(time.time() - startTime, 3)

def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
 
    L = [0] * (n1)
    R = [0] * (n2)
 
    for i in range(0, n1):
        L[i] = arr[l + i]
 
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
 
    i = 0
    j = 0
    k = l
 
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
 
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
 
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def mergeSort(arr, l, r):
    if l < r:
        m = l+(r-l)//2

        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)

def min(a, b):
    if (a <= b):
        return a
    else:
        return b

BubbleSort(split)
print('Bubble Sort Time: ' + str(bubbleSortTime) + ' seconds')
SelectionSort(split)
print('Selection Sort Time: ' + str(selectionSortTime) + ' seconds')
mergeSort()
if (min(selectionSortTime, bubbleSortTime) == selectionSortTime):
    print('Selection Sort is Fastest at ' + str(selectionSortTime) + ' seconds')
else:
    print('Bubble Sort is Fastest at ' + str(bubbleSortTime) + ' seconds')