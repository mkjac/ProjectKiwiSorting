from operator import index
import string
import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as tck
import time
import sys

np.set_printoptions(threshold=sys.maxsize)

with open('kiwidata.txt') as file:
    text = file.read()
    file.close()
split = text.split(',')
split.remove('')

split = np.array(split).astype(np.double)

indexes = [0] * (len(split))

for i in range(len(indexes)):
    indexes[i] = i

selectionSorted = split
bubbleSorted = split
mergeSorted = split
optimizedSorted = split

def BubbleSort(split):
    n = len(split)
    swapped = False
    for i in range(n-1):
        for j in range(0, n-i-1):
            if split[j] > split[j + 1]:
                swapped = True
                split[j], split[j + 1] = split[j + 1], split[j]
         
        if not swapped:
            return split

def SelectionSort(split):
    for i in range(len(split)):
  
        min_idx = i
        for j in range(i+1, len(split)):
            if split[min_idx] > split[j]:
                min_idx = j
    
        split[i], split[min_idx] = split[min_idx], split[i]
    return split

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
    return arr

def MySort(arr):
    one = [0] * (len(arr))
    myList = list(arr)

    for i in range(len(myList)):
        number = min(myList)
        one[i] = number
        myList.remove(number)

    return one

def MyMin(a, b, c, d):
    if (a <= b and a <= c and a <= d):
        return a
    elif (b <= a and b <= c and b <= d):
        return b
    elif (c <= a and c <= b and c <= d):
        return c
    else:
        return d

global begin
global end
begin = time.time()
BubbleSort(bubbleSorted)
end = time.time()
bubbleSortTime = end - begin
#print(*bubbleSorted)
print('Bubble Sort Time: ' + str(round(bubbleSortTime, 3)) + ' seconds')

begin = time.time()
selectionSorted = SelectionSort(selectionSorted)
end = time.time()
selectionSortTime = end - begin
#print(*selectionSorted)
print('Selection Sort Time: ' + str(round(selectionSortTime, 3)) + ' seconds')

begin = time.time()
mergeSorted = mergeSort(mergeSorted, 0, len(mergeSorted) - 1)
end = time.time()
mergeSortTime = end - begin
#print(*mergeSorted)
print('Merge Sort Time: ' + str(round(mergeSortTime, 3)) + ' seconds')

begin = time.time()
optimizedSorted = MySort(optimizedSorted)
end = time.time()
optimizedSortTime = end - begin
print(*optimizedSorted)
print('Optimized Sort Time: ' + str(round(optimizedSortTime, 3)) + ' seconds')

if (min(selectionSortTime, bubbleSortTime, mergeSortTime, optimizedSortTime) == selectionSortTime):
    print('Selection Sort is Fastest at ' + str(round(selectionSortTime, 3)) + ' seconds')
elif (min(selectionSortTime, bubbleSortTime, mergeSortTime, optimizedSortTime) == bubbleSortTime):
    print('Bubble Sort is Fastest at ' + str(round(bubbleSortTime, 3)) + ' seconds')
elif(min(selectionSortTime, bubbleSortTime, mergeSortTime, optimizedSortTime) == optimizedSortTime):
    print('Optimized Sort is Fastest at ' + str(round(optimizedSortTime, 3)) + ' seconds')
else:
    print('Merge Sort is Fastest at ' + str(round(mergeSortTime, 3)) + ' seconds')

plt.yticks(np.arange(min(optimizedSorted), max(optimizedSorted), 0.5))
plt.scatter(indexes, optimizedSorted)
plt.show()