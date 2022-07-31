from kiwi import BubbleSort, SelectionSort, mergeSort, split
import numpy as np
from random import randint
import time

# Function to shuffle a given array


def ShuffleArray(arr):
    # Make copy of original array
    oldArray = np.copy(arr)
    # Create empty list to store shuffled array
    newArray = []
    # Set current right index of old array to length of original array
    currentLen = len(arr) - 1

    # While right index of old array is greater than one less than the left index of old array
    while(currentLen > -1):
        # Generate random int between 0 and current right index of old array
        randIndex = randint(0, currentLen)
        # Append the item at the random index in the old array to the shuffle array list
        newArray.append(oldArray[randIndex])
        # Remove random item in old array from the old array
        oldArray = np.delete(oldArray, randIndex)
        # Minus one from currentLen to get the new right index of the old array
        currentLen -= 1
    # Return the shuffled array
    return newArray


# Best Case
sortedData = np.sort(np.copy(split))
# Average Case
randomData = ShuffleArray(np.copy(split))
# Worst Case
reversedData = np.array(np.copy(sortedData))[::-1]

#################
## BUBBLE SORT ##
#################


def test_WorstBubbleSort():
    begin = time.time()
    # BubbleSort(reversedData) == sortedData
    assert np.array_equal(BubbleSort(np.copy(reversedData)), sortedData)
    print('\nTime taken: ' +
          str(np.round(time.time() - begin, 3)) + ' seconds')


def test_AverageBubbleSort():
    begin = time.time()
    assert np.array_equal(BubbleSort(np.copy(randomData)), sortedData)
    print('\nTime taken: ' +
          str(np.round(time.time() - begin, 3)) + ' seconds')


def test_BestBubbleSort():
    begin = time.time()
    assert np.array_equal(BubbleSort(np.copy(sortedData)), sortedData)
    print('\nTime taken: ' +
          str(np.round(time.time() - begin, 3)) + ' seconds')

####################
## SELECTION SORT ##
####################


def test_WorstSelectionSort():
    begin = time.time()
    assert np.array_equal(SelectionSort(np.copy(reversedData)), sortedData)
    print('\nTime taken: ' +
          str(np.round(time.time() - begin, 3)) + ' seconds')


def test_AverageSelectionSort():
    begin = time.time()
    assert np.array_equal(SelectionSort(np.copy(randomData)), sortedData)
    print('\nTime taken: ' +
          str(np.round(time.time() - begin, 3)) + ' seconds')


def test_BestSelectionSort():
    begin = time.time()
    assert np.array_equal(SelectionSort(np.copy(sortedData)), sortedData)
    print('\nTime taken: ' +
          str(np.round(time.time() - begin, 3)) + ' seconds')

################
## MERGE SORT ##
################


def test_WorstMergeSort():
    begin = time.time()
    # Worst Case
    assert np.array_equal(
        mergeSort(np.copy(reversedData), 0, len(reversedData) - 1), sortedData)
    print('\nTime taken: ' +
          str(np.round(time.time() - begin, 3)) + ' seconds')


def test_AverageMergeSort():
    begin = time.time()
    # Average Case
    assert np.array_equal(
        mergeSort(np.copy(randomData), 0, len(randomData) - 1), sortedData)
    print('\nTime taken: ' +
          str(np.round(time.time() - begin, 3)) + ' seconds')


def test_BestMergeSort():
    begin = time.time()
    # Best Case
    assert np.array_equal(
        mergeSort(np.copy(sortedData), 0, len(sortedData) - 1), sortedData)
    print('\nTime taken: ' +
          str(np.round(time.time() - begin, 3)) + ' seconds')
