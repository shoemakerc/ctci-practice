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
## INSERTION SORT ##
def insertionSort(arr):
	for i in range(1, len(arr)):
		x = arr[i]
		j = i - 1
		while j >= 0 and arr[j] > x:
			arr[j + 1] = arr[j]
			j = j - 1
		arr[j + 1] = x
	return arr

def selectionSort(arr):
	for i in range(len(arr)):
		min = i
		for j in range(i + 1, len(arr)):
			if arr[j] < arr[min]:
				min = j
		swap(arr, min, i)
	return arr

def swap(arr, x, y):
	temp = arr[x]
	arr[x] = arr[y]
	arr[y] = temp

def binarySearch(arr, target):
	return binarySearchHelper(arr, target, 0, len(arr) - 1)

def main():
	unsortedArr = [2, 5, 2, 4, 12, 5, 1, 5, 8, 9, 44, 2, 1243, 6, 6, 3, 4]
	searchArr = [1, 3, 5, 7, 9]
	print("Unsorted array is:", unsortedArr)
	print("Unsorted array after insertion sort:", insertionSort(unsortedArr))
	print("Unsorted array after selection sort:", selectionSort(unsortedArr))
	# print(selectionSort(unsortedArr))
	index = binarySearch(searchArr, 8)
	if index < 0:
		print("Error: Element not found at any index")
	else:
		print("Found at index", index)
main()