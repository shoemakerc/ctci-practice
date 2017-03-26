from random import shuffle

## BINARY SEARCH ##
def binarySearchHelper(arr, target, lo, hi):
	if lo > hi:
		return -1
	mid = (lo + hi) // 2
	if target == arr[mid]:
		return mid
	elif target > arr[mid]:
		return binarySearchHelper(arr, target, mid + 1, hi)
	else:
		return binarySearchHelper(arr, target, 0, mid - 1)


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
		n = arr[i]
		j = i - 1
		while j >= 0 and arr[j] > n:
			arr[j + 1] = arr[j]
			j = j - 1
		arr[j + 1] = n
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
	pass
def merge():
	pass

## RADIX SORT ##
def radixSort(arr):
	pass

'''
## BEST SORT ##
def bogoSort(arr):
	while sorted(arr) != arr:
		shuffle(arr)
		print("Bogo!", arr)
	return arr
'''

def binarySearch(arr, target):
	return binarySearchHelper(arr, target, 0, len(arr) - 1)

def main():
	searchArr = [1, 3, 5, 7, 9]
	print("Unsorted array is:", [2, 5, 2, 4, 12, 5, 1, 5, 8, 9, 44, 2, 1243, 6, 6, 3, 4])
	print("Unsorted array after insertion sort:", insertionSort([2, 5, 2, 4, 12, 5, 1, 5, 8, 9, 44, 2, 1243, 6, 6, 3, 4])) # these long inputs...damn you, side effects!
	print("Unsorted array after selection sort:", selectionSort([2, 5, 2, 4, 12, 5, 1, 5, 8, 9, 44, 2, 1243, 6, 6, 3, 4]))
	#print("Unsorted array after bogosort:", bogoSort([2, 5, 2, 4, 12, 5, 1, 5, 8, 9, 44, 2, 1243, 6, 6, 3, 4]))
	print("Unsorted array after bubble sort:", bubbleSort([2, 5, 2, 4, 12, 5, 1, 5, 8, 9, 44, 2, 1243, 6, 6, 3, 4]))
	index = binarySearch(searchArr, 8)
	if index < 0:
		print("Error: Element not found at any index")
	else:
		print("Found at index", index)
main()