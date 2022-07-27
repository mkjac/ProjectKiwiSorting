import numpy as np
import sys
import time
import matplotlib.pyplot as plt

# Make the print able to print the maximum amount of characters
np.set_printoptions(threshold=sys.maxsize)

# 1) Open the file for reading
# 2) Store all the text data in a string called text
# 3) Close the file
with open('kiwidata.txt') as file:
    text = file.read()
    file.close()

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

# Bubble Sort Function


def BubbleSort(array):
    # Copy the array passed into the function to sorting array
    sorting = np.copy(array)
    # While sorting array is not sorted...
    while(np.array_equal(np.sort(sorting), sorting) == False):
        # Iterate from 0 to the length of the array - 1
        for i in range(len(array) - 1):
            # If the current item is greater than the next item, swap the items
            if(sorting[i] > sorting[i + 1]):
                temp = sorting[i]
                sorting[i] = sorting[i + 1]
                sorting[i + 1] = temp
    # Return the sorted array
    return sorting

# Selection Sort Function


def SelectionSort(array):
    # Iterate from 0 to the length of the array
    for i in range(0, len(array)):
        # Set current minimum index to i
        minIndex = i
        # Iterate from i to the length of the array
        for j in range(i + 1, len(array)):
            # If item at index j is less than current minimum item
            # Set minimum index to position j
            if (array[j] < array[minIndex]):
                minIndex = j
            # Swap the items
            temp = array[i]
            array[i] = array[minIndex]
            array[minIndex] = temp
    # Return sorted array
    return array

# Merge Function


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

# My Optimized Sort


def MySort(array):
    # Create array with length of the original array to store final sorted values
    one = [0] * (len(array))
    # Create list copy of original array
    myList = list(array)

    # For loop that iterates through the length of the list times
    for i in range(len(myList)):
        # Set current number equal to the minimum value in the list
        number = min(myList)
        # Set the current index of one array equal to the minimum number
        one[i] = number
        # Remove the minimum number from the list
        myList.remove(number)
    # Return sorted array
    return one

# Print Time Function


def PrintTime(text, time):
    # Print the text, which is which algorithm it is,
    # plus 'took' and then the time, converted into a string,
    # to 3 decimal places, plus ' seconds'
    print(text + ' took ' + str(np.round(time, 3)) + ' seconds')


# Copy the original array into seperate arrays for sorting
bubbleSorted = np.copy(split)
selectionSorted = np.copy(split)
mergeSorted = np.copy(split)
optimizedSorted = np.copy(split)

#################
## BUBBLE SORT ##
#################

# Store the time before function started
begin = time.time()
# Set the bubbleSorted array equal to the bubble sorted array
bubbleSorted = BubbleSort(bubbleSorted)
# Store the time after the function has ended
end = time.time()
# Set bubbleTime to the time the function took to execute
bubbleTime = end - begin

####################
## SELECTION SORT ##
####################

# Store the time before function started
begin = time.time()
# Set the selectionSorted array equal to the selection sorted array
selectionSorted = SelectionSort(selectionSorted)
# Store the time after the function has ended
end = time.time()
# Set selectionTime to the time the function took to execute
selectionTime = end - begin

################
## MERGE SORT ##
################

# Store the time before function started
begin = time.time()
# Set the mergeSorted array equal to the merge sorted array
mergeSorted = mergeSort(mergeSorted, 0, len(mergeSorted) - 1)
# Store the time after the function has ended
end = time.time()
# Set mergeTime to the time the function took to execute
mergeTime = end - begin

####################
## OPTIMIZED SORT ##
####################

# Store the time before function started
begin = time.time()
# Set the optimizedSorted array equal to the optimized sorted array
optimizedSorted = MySort(optimizedSorted)
# Store the time after the function has ended
end = time.time()
# Set optimizedTime to the time the function took to execute
optimizedTime = end - begin

# Prints each of the sorted arrays
# print(*bubbleSorted)
# print(*selectionSorted)
# print(*mergeSorted)
# print(*optimizedSorted)

# Prints the time each function took to complete
PrintTime('Bubble Sort', bubbleTime)
PrintTime('Selection Sort', selectionTime)
PrintTime('Merge Sort', mergeTime)
PrintTime('Optimized Sort', optimizedTime)

# Sets the time of the fastest algorithm
fastest = min([bubbleTime, selectionTime, mergeTime, optimizedTime])

# Sets fastestFunc to be the text specifying the name of the fastest function
if (fastest == bubbleTime):
    fastestFunc = 'Bubble Sort'
elif (fastest == selectionTime):
    fastestFunc = 'Selection Sort'
elif (fastest == mergeTime):
    fastestFunc = 'Merge Sort'
else:
    fastestFunc = 'Optimized Sort'

# Print which function time was the fastest
print('The fastest was ' + fastestFunc + ' which took ' +
      str(np.round(fastest, 3)) + ' seconds')

# Plot the data as a scatter graph
plt.yticks(np.arange(min(optimizedSorted), max(optimizedSorted), 0.5))
plt.scatter(indexes, optimizedSorted)
plt.show()
