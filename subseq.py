arr = [1,2,-5,6,2,3,-8,-7,2,4,3,2,1,1,1,4,3,-9]
r = 2

current = []
max_length = 0

def valid(a):
	return max(a) - min(a) <= r

for i in arr:
	current.append(i)
	if valid(current) and len(current) > max_length:
		max_length = len(current)
	else:
		while not valid(current):
			current = current[1:]
print("Array is:", arr)
print("Want to find largest subsequence whose elements are equal to", r)
print("Largest subsequence has length of", max_length)