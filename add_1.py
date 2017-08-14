'''
add_1.py
Solution to 5.2: Increment an arbitrary-precision integer, from Elements of
Programming Interviews in Python by Aziz, Lee, and Prakash
'''
def add_1(arr):
    '''
    Given an array representation of a positive decimal integer, returns the
    array representation of that integer + 1
    '''
    arr[-1] += 1
    for i in range(len(arr) - 1, 0, -1):
        if arr[i] != 10:
            break
        arr[i] = 0
        arr[i - 1] += 1
    if arr[0] == 10:
        arr[0] = 0
        arr.insert(0, 1)
def main():
    '''
    Tester code
    '''
    lst = [1, 2, 3]
    add_1(lst)
    print(lst)
    lst2 = [0]
    add_1(lst2)
    print(lst2)
    lst3 = [9, 9, 9]
    add_1(lst3)
    print(lst3)
main()
