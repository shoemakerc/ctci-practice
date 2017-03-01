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

def insertionSort(arr):
	for i in range(1, len(arr)):
		

def selectionSort(arr):
	for i in range(len(arr)):
		min = i
		for j in range(i + 1, len(arr)):
			if arr[j] < arr[min]:
				min = j
		swap(arr, min, i)

def swap(arr, x, y):
	temp = arr[x]
	arr[x] = arr[y]
	arr[y] = temp

def binarySearch(arr, target):
	return binarySearchHelper(arr, target, 0, len(arr) - 1)

def main():
	arr = [1, 3, 5, 7, 9]
	index = binarySearch(arr, 8)
	if index < 0:
		print("Error: Element not found at any index")
	else:
		print("Found at index", index)
main()