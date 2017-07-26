import sys

class Stack:
	def __init__(self):
		self.items = []
	def isEmpty(self):
		return self.items == []
	def push(self, item):
		self.items.append(item)
	def pop(self):
		return self.items.pop()
	def peek(self):
		return self.items[len(self.items) - 1]
	def size(self):
		return len(self.items)

def tests():
	print("============================")
	print("BEGIN STACK TESTS")
	print("============================")
	x = Stack()
	x.push(3)
	x.push(62)
	print("size of stack is:", x.size())
	print("top of stack is:", x.peek())
	print("popped from stack:", x.pop())
	print("new size of stack is:", x.size())
	print("============================")
	print("END STACK TESTS")
	print("============================")

def parChecker(inp):
	s = Stack()
	balanced = True
	i = 0
	while i < len(inp) and balanced:
		if inp[i] == '(':
			s.push(inp[i])
		elif inp[i] == ')':
			if s.isEmpty():
				balanced = False
			else:
				s.pop()
		else:
			print("Invalid input. Exiting.")
			sys.exit(1)
		i = i + 1
	if balanced and s.isEmpty():
		return True
	else:
		return False

def parCheckerGen(inp):
	s = Stack()
	balanced = True
	i = 0
	while i < len(inp) and balanced:
		if inp[i] in "([{":
			s.push(inp[i])
		elif inp[i] == ')':
			if s.isEmpty():
				balanced = False
			else:
				s.pop()
		else:
			print("Invalid input. Exiting.")
			sys.exit(1)
		i = i + 1
	if balanced and s.isEmpty():
		return True
	else:
		return False

def main():
	tests()
	print(parChecker("(((()()())))(())"))
main()
