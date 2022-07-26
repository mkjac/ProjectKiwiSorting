import numpy as np
import sys
import time
import matplotlib.pyplot as plt

np.set_printoptions(threshold=sys.maxsize)

with open('kiwidata.txt') as file:
    text = file.read()
    file.close()
global split
split = text.split(',')
split.remove('')

split = np.array(split).astype(np.float64)

indexes = [0] * (len(split))

for i in range(len(indexes)):
    indexes[i] = i


def BubbleSort(array):
    sorting = np.copy(array)
    while(np.array_equal(np.sort(sorting), sorting) == False):
        for i in range(len(array) - 1):
            if(sorting[i] > sorting[i + 1]):
                temp = sorting[i]
                sorting[i] = sorting[i + 1]
                sorting[i + 1] = temp

    return sorting


def SelectionSort(array):
    for i in range(0, len(array)):
        minIndex = i
        for j in range(i + 1, len(array)):
            if (array[j] < array[minIndex]):
                minIndex = j
            temp = array[i]
            array[i] = array[minIndex]
            array[minIndex] = temp
    return array


def merge(array, left, middle, right):
    n1 = middle - left + 1
    n2 = right - middle

    leftArray = [0] * (n1)
    rightArray = [0] * (n2)

    for firstSubIndex in range(0, n1):
        leftArray[firstSubIndex] = array[left + firstSubIndex]

    for secondSubIndex in range(0, n2):
        rightArray[secondSubIndex] = array[middle + 1 + secondSubIndex]

    firstSubIndex = 0
    secondSubIndex = 0
    mergedSubIndex = left

    while firstSubIndex < n1 and secondSubIndex < n2:
        if leftArray[firstSubIndex] <= rightArray[secondSubIndex]:
            array[mergedSubIndex] = leftArray[firstSubIndex]
            firstSubIndex += 1
        else:
            array[mergedSubIndex] = rightArray[secondSubIndex]
            secondSubIndex += 1
        mergedSubIndex += 1

    while firstSubIndex < n1:
        array[mergedSubIndex] = leftArray[firstSubIndex]
        firstSubIndex += 1
        mergedSubIndex += 1

    while secondSubIndex < n2:
        array[mergedSubIndex] = rightArray[secondSubIndex]
        secondSubIndex += 1
        mergedSubIndex += 1


def mergeSort(array, left, right):
    if left < right:
        middle = left+(right-left)//2

        mergeSort(array, left, middle)
        mergeSort(array, middle+1, right)
        merge(array, left, middle, right)
    return array


def MySort(array):
    one = [0] * (len(array))
    myList = list(array)

    for i in range(len(myList)):
        number = min(myList)
        one[i] = number
        myList.remove(number)

    return one


begin = time.time()
# bubbleSorted = np.copy(split)
# selectionSorted = np.copy(split)
# mergeSorted = np.copy(split)
optimizedSorted = np.copy(split)

# bubbleSorted = BubbleSort(bubbleSorted)
# selectionSorted = SelectionSort(selectionSorted)
# mergeSorted = mergeSort(mergeSorted, 0, len(mergeSorted) - 1)
optimizedSorted = MySort(optimizedSorted)

end = time.time()
timeTaken = end - begin
# print(*bubbleSorted)
# print(*selectionSorted)
# print(*mergeSorted)
print(*optimizedSorted)
print(str(np.round(timeTaken, 3)) + ' seconds')

plt.yticks(np.arange(min(optimizedSorted), max(optimizedSorted), 0.5))
plt.scatter(indexes, optimizedSorted)
plt.show()
