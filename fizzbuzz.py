'''
My Python 3 implementation of the Fizzbuzz problem. Probably not the best way
to solve this, but I dislike one-liners. They're cool, but ya know..
'''
def fizzbuzz(num1, num2):
    '''
    Conditional definition of Fizzbuzz
    '''
    for i in range(num1, num2 + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("Fizzbuzz", "")
        elif i % 3 == 0:
            print("Fizz", "")
        elif i % 5 == 0:
            print("Buzz", "")
        else:
            print(i, "")

def main():
    '''
    Show an example (in this case, from 1 to 30)
    '''
    fizzbuzz(1, 30)
main()
