def mag_index_bf(A):
    '''
    Brute-force solution to find a "magic index" in an array

    Time complexity (worst-case): O(n)
    Space complexity: O(1)
    '''
    for i in range(len(A)):
        if A[i] == i:
            return i
    return -1

def mag_index(A):
    if len(A) == 0:
        return -1
    else:
        
def main():
    arr = [0, 2 , 3]
    print(mag_index_bf(arr))
main()