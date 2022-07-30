import sys
import numpy as np
import matplotlib.pyplot as plt

# Make the print able to print the maximum amount of characters
np.set_printoptions(threshold=sys.maxsize)

# 1) Open the file for reading
# 2) Store all the text data in a string called text
# 3) Close the file
with open('kiwidata.txt') as file:
    text = file.read()

# 1) Declare a global variable called split
# 2) Set split to be a string array containg text, split based on the seperator ','
# 3) Remove all empty values from split array
global split
split = text.split(',')
split.remove('')

# Set split to be a numpy array of type float64
split = np.array(split).astype(np.float64)

# Create new array indexes and set it equal to i to the length of split array (0-699)
indexes = [0] * (len(split))
for i in range(len(indexes)):
    indexes[i] = i

# Copy data array into seperate arrays for each algorithm
bubbleSorted = np.copy(split)
selectionSorted = np.copy(split)
mergeSorted = np.copy(split)

#################
## BUBBLE SORT ##
#################


def BubbleSort(array):
    # While array is not sorted...
    while(np.array_equal(np.sort(array), array) == False):
        # Iterate from 0 to the length of the array - 1
        for i in range(len(array) - 1):
            # If the current item is greater than the next item, swap the items
            if(array[i] > array[i + 1]):
                temp = array[i]
                array[i] = array[i + 1]
                array[i + 1] = temp
    # Return the sorted array
    return array

####################
## SELECTION SORT ##
####################


def SelectionSort(array):
    length = len(array)
    # Iterate from 0 to the length of the array
    for i in range(length - 1):
        # Set current minimum index to i
        minIndex = i
        # Iterate from i to the length of the array
        for j in range(i + 1, length):
            minIndex = i
            # If item at index j is less than current minimum item
            # Set minimum index to position j
            if (array[j] < array[minIndex]):
                minIndex = j
            # Swap the items
            array[i], array[minIndex] = array[minIndex], array[i]
    # Return sorted array
    return array


def merge(array, left, middle, right):
    # Set n1 equal to the start index of the right subarray
    n1 = middle - left + 1
    # Set n2 equal to the start index of the right subarray
    n2 = right - middle

    # Create left and right array using n1 and n2
    leftArray = [0] * (n1)
    rightArray = [0] * (n2)

    # Populate left subarray
    for firstSubIndex in range(0, n1):
        leftArray[firstSubIndex] = array[left + firstSubIndex]

    # Populate right subarray
    for secondSubIndex in range(0, n2):
        rightArray[secondSubIndex] = array[middle + 1 + secondSubIndex]

    # firstSubIndex is the first index to compare in the left subarray
    # secondSubIndex is the first index to compare in the right subarray
    # mergedSubIndex is the first index to compare in the right subarray
    firstSubIndex = 0
    secondSubIndex = 0
    mergedSubIndex = left

    # While current index of left subarray is less
    # than the length of the subarray
    # and the current index of the right subarray is less
    # than the length of the subarray
    while firstSubIndex < n1 and secondSubIndex < n2:
        # If the current item in the left array is less than or equal to
        # the current item in the right subarray
        if leftArray[firstSubIndex] <= rightArray[secondSubIndex]:
            # Current index of merged array equals current item in left subarray
            array[mergedSubIndex] = leftArray[firstSubIndex]
            # Increment left array index by 1
            firstSubIndex += 1
        else:
            # Current index of merged array equals current item in right subarray
            array[mergedSubIndex] = rightArray[secondSubIndex]
            # Current index of right subarray increments by 1
            secondSubIndex += 1
        # Current index of merged array increases by 1
        mergedSubIndex += 1

    # While current index of left subarray is less than the length of the subarray
    while firstSubIndex < n1:
        # The item at the current merged array index is equal
        # to the current item in the left subarray
        array[mergedSubIndex] = leftArray[firstSubIndex]
        # Current left array index increments by 1
        firstSubIndex += 1
        # Merged array index increments by 1
        mergedSubIndex += 1

    # While the current right array index is less than the length of the subarray
    while secondSubIndex < n2:
        # The item at the current merged array index is equal
        # to the current item in the right subarray
        array[mergedSubIndex] = rightArray[secondSubIndex]
        # Current right array index increments by 1
        secondSubIndex += 1
        # Merged array index increments by 1
        mergedSubIndex += 1

# Merge Sort Function


def mergeSort(array, left, right):
    # If leftmost item index is less than right most item index
    # i.e. subarray length is greater than 1...
    if left < right:
        # Set index pointing to index at the end of left subarray
        # i.e. the middle of the merged array
        middle = left+(right-left)//2

        # Call mergeSort on the left subarray
        mergeSort(array, left, middle)
        # Call mergeSort on the right subarray
        mergeSort(array, middle+1, right)
        # Merge the subarrays together
        merge(array, left, middle, right)
    # Return the sorted array
    return array


# BubbleSort(bubbleSorted)
#mergeSort(mergeSorted, 0, len(mergeSorted) - 1)

bubbleSorted = BubbleSort(bubbleSorted)
#selectionSorted = SelectionSort(selectionSorted)
#mergeSorted = mergeSort(mergeSorted, 0, len(mergeSorted) - 1)

# Sorted Data Graph
plt.figure(1)
plt.title('Kiwi Weights')
plt.yticks(np.arange(min(bubbleSorted), max(bubbleSorted), 0.2))
plt.ylabel('Kiwi Weight')
plt.xlabel('Kiwi ID Number')
plt.scatter(indexes, bubbleSorted)

# Unsorted Data Graph
plt.figure(2)
plt.title('Kiwi Weights')
plt.yticks(np.arange(min(split), max(split), 0.2))
plt.ylabel('Kiwi Weight')
plt.xlabel('Kiwi ID Number')
plt.scatter(indexes, split)

plt.show()
