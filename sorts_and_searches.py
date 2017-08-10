'''
sorts-and-searches.py

Just a bunch of different sorting and searching algorithms. To be added onto
and reviewed for practice purposes

'''
from random import shuffle # For the best sorting algorithm ever

## BINARY SEARCH ##
def binary_search(arr, target):
    if len(arr) == 0:
        return -1
    else:
        return binary_search_helper(arr, target, 0, len(arr) - 1)
def binary_search_helper(arr, target, lo, hi):
    if lo > hi:
        return -1 
    mid = (lo + hi) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search_helper(arr, target, 0, mid - 1)
    else:
        return binary_search_helper(arr, target, mid + 1, hi)

## BUBBLE SORT ##
def bubble_sort(arr):
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
def insertion_sort(arr):
    for i in range(1, len(arr)):
        curr = arr[i]
        j = i
        while j > 0 and arr[j - 1] > curr:
            arr[j] = arr[j - 1]
            j = j - 1
        arr[j] = curr
    return arr

## SELECTION SORT ##
def selection_sort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[min], arr[i] = arr[i], arr[min]
    return arr

## MERGE SORT ##
def merge_sort(arr):
    helper = [0] * len(arr)
    return merge_sort_helper(arr, helper, 0, len(arr) - 1)
def merge_sort_helper(arr, helper, lo, hi):
    if lo < hi:
        mid = (lo + hi) // 2
        merge_sort_helper(arr, helper, lo, mid)
        merge_sort_helper(arr, helper, mid + 1, hi)
        arr = merge(arr, helper, lo, mid, hi)
    return arr
def merge(arr, helper, lo, mid, hi):
    for i in range(lo, hi + 1):
        helper[i] = arr[i]

    helperLeft = lo
    helperRight = mid + 1
    curr = lo

    while helperLeft <= mid and helperRight <= hi:
        if helper[helperLeft] <= helper[helperRight]:
            arr[curr] = helper[helperLeft]
            helperLeft += 1
        else:
            arr[curr] = helper[helperRight]
            helperRight += 1
        curr += 1
    remaining = mid - helperLeft
    for i in range(remaining + 1):
        arr[curr + i] = helper[helperLeft + i]
    return arr

## QUICK SORT ##
def quicksort(arr):
    return quicksort_helper(arr, 0, len(arr) - 1)
def quicksort_helper(arr, lo, hi):
    if lo < hi:
        split = partition(arr, lo, hi)
        quicksort_helper(arr, lo, split - 1)
        quicksort_helper(arr, split + 1, hi)
    return arr
def partition(arr, lo, hi):
    '''
    Assume first value is pivot
    '''
    pivot = arr[lo]
    left = lo + 1
    right = hi
    done = False
    while not done:
        while left <= right and arr[left] <= pivot:
            left += 1
        while arr[right] >= pivot and right >= left:
            right -= 1
        if right < left:
            done = True
        else:
            arr[left], arr[right] = arr[right], arr[left]
    arr[lo], arr[right] = arr[right], arr[lo]
    return right

## SHELL SORT ##
'''
TODO
def shell_sort(arr):
'''

## BEST SORT ##
def bogosort(arr):
    while sorted(arr) != arr:
        shuffle(arr)
        print("Bogo!", arr)
    return arr


def main():
    searchArr = [1, 3, 5, 7, 9]
    print("Unsorted array is:", [2, 5, 2, 4, 12, 5, 1, 5, 8, 9, 44, 2, 1243, 6, 6, 3, 4])
    print("Unsorted array after insertion sort:", insertion_sort([2, 5, 2, 4, 12, 5, 1, 5, 8, 9, 44, 2, 1243, 6, 6, 3, 4])) # these long inputs...damn you, side effects!
    print("Unsorted array after selection sort:", selection_sort([2, 5, 2, 4, 12, 5, 1, 5, 8, 9, 44, 2, 1243, 6, 6, 3, 4]))
    print("Unsorted array after bubble sort:", bubble_sort([2, 5, 2, 4, 12, 5, 1, 5, 8, 9, 44, 2, 1243, 6, 6, 3, 4]))
    print("Unsorted array after merge sort:", merge_sort([2, 5, 2, 4, 12, 5, 1, 5, 8, 9, 44, 2, 1243, 6, 6, 3, 4]))
    print("Unsorted array after quicksort:", quicksort([2, 5, 2, 4, 12, 5, 1, 5, 8, 9, 44, 2, 1243, 6, 6, 3, 4]))
    print(binary_search(searchArr, 8))
    print(binary_search(searchArr, 4))
main()