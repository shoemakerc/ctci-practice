'''
substring_add.py
Given a (positive) integer, returns and prints the sum of all the substring integers of the 
given integer.

Problem proposed by Pritom Mazumdar on the HH Coding Interview Prep Facebook group.
Solution adapted from Ritwik Das.
'''


def get_substr_total(num):
	total = 0
	curr = 1
	for i in range(len(num) - 1, -1, -1):
		print(num[i])
		total += int(num[i]) * curr * (i + 1)
		curr = curr * 10 + 1
	return total

def main():
	inp = input("Enter a number: ")
	while (int(inp) < 0):
		print("Error: cannot find substring sum of negative numbers. Please try again.")
		inp = input("Enter a number: ")
	substr_total = get_substr_total(inp)
	print("The total of substrings of", inp, "is", substr_total)
main()