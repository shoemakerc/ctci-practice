'''
sorts-and-searches.py

Just a bunch of different sorting and searching algorithms. To be
added onto and reviewed for practice purposes

'''
from random import shuffle # For the best sorting algorithm ever

## BINARY SEARCH ##
def binary_search(arr, target):
    if len(arr) == 0:
        return -1
    else:
        mid = len(arr) // 2
        if target == arr[mid]:
            return mid
        elif target > arr[mid]:
            return binary_search(arr[mid + 1:], target)
        else:
            return binary_search(arr[:mid], target)

## BUBBLE SORT ##
def bubbleSort(arr):
    n = len(arr)
    while n > 0:
        new = 0
        for i in range(1, n):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                new = i
        n = new
    return arr

## INSERTION SORT ##
def insertionSort(arr):
    for i in range(1, len(arr)):
        curr = arr[i]
        j = i
        while j > 0 and arr[j - 1] > curr:
            arr[j] = arr[j - 1]
            j = j - 1
        arr[j] = curr
    return arr

## SELECTION SORT ##
def selectionSort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[min], arr[i] = arr[i], arr[min]
    return arr

## MERGE SORT ##
def mergeSort(arr):
    if len(arr) == 1:
        return arr
    left = []
    right = []
    for i in range(len(arr)):
        if i < (len(arr))/2:
            left.append(arr[i])
        else:
            right.append(arr[i])
    left = mergeSort(left)
    right = mergeSort(right)
    return merge(left, right)
def merge(left, right):
    result = []
    while len(left) != 0 and len(right) != 0:
        if left[0] <= right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]
    while len(left) != 0:
        result.append(left[0])
        left = left[1:]
    while len(right) != 0:
        result.append(right[0])
        right = right[1:]
    return result

## QUICK SORT ##
def quickSort(arr, lo, hi):
    if lo < hi:
        split = partition(arr, lo, hi)
        quickSort(A, lo, split - 1)
        quickSort(A, split + 1, hi)
    return arr
def partition(arr, lo, hi):
    '''Assume first value is pivot'''
    pivot = arr[lo]
    left = lo + 1
    right = hi
    for j in range(lo, hi - 1):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[hi] = arr[hi], arr[i + 1]
    return i + 1

'''
## BEST SORT ##
def bogoSort(arr):
    while sorted(arr) != arr:
        shuffle(arr)
        print("Bogo!", arr)
    return arr
'''

def main():
    searchArr = [1, 3, 5, 7, 9]
    print("Unsorted array is:", [2, 5, 2, 4, 12, 5, 1, 5, 8, 9, 44, 2, 1243, 6, 6, 3, 4])
    print("Unsorted array after insertion sort:", insertionSort([2, 5, 2, 4, 12, 5, 1, 5, 8, 9, 44, 2, 1243, 6, 6, 3, 4])) # these long inputs...damn you, side effects!
    print("Unsorted array after selection sort:", selectionSort([2, 5, 2, 4, 12, 5, 1, 5, 8, 9, 44, 2, 1243, 6, 6, 3, 4]))
    #print("Unsorted array after bogosort:", bogoSort([2, 5, 2, 4, 12, 5, 1, 5, 8, 9, 44, 2, 1243, 6, 6, 3, 4]))
    print("Unsorted array after bubble sort:", bubbleSort([2, 5, 2, 4, 12, 5, 1, 5, 8, 9, 44, 2, 1243, 6, 6, 3, 4]))
    print("Unsorted array after merge sort:", mergeSort([2, 5, 2, 4, 12, 5, 1, 5, 8, 9, 44, 2, 1243, 6, 6, 3, 4]))
    #print("Unsorted array after quick sort:", quickSort([2, 5, 2, 4, 12, 5, 1, 5, 8, 9, 44, 2, 1243, 6, 6, 3, 4], 0, len([2, 5, 2, 4, 12, 5, 1, 5, 8, 9, 44, 2, 1243, 6, 6, 3, 4])))
    print(binary_search(searchArr, 8))
    print(binary_search(searchArr, 4))
main()