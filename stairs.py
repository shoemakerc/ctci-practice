def num_permutations_to_climb_stairs(n, k):
    '''
    Uses bottom-up DP to compute the number of possible permutations to climb
    n steps when allowed to advance up to k steps at one time
    
    Time complexity: O(n * k)
    Space complexity: O(n)
    '''
    if n == 0 or n == 1:
        return 1
    permutations = [0] * (n + 1)
    permutations[0] = 1
    permutations[1] = 1
    for i in range(2, n + 1):
        j = 0
        while (j <= k):
            permutations[i] += (permutations[i - j] if i - j >= 0 else 0)
            j += 1
    print("DP/memoized table:", permutations)
    return permutations[-1]
'''
def num_permutations_to_climb_stairs_2(n, k):

    Same approach as above, but uses only O(1) space

    Time complexity: O(n * k)
    Space complexity: O(n)
    
    if n == 0 or n == 1:
        return 1
    a = 1
    b = 1
    for i in range(2, n + 1)
        j = 0
        while (j <= k):
            c = a + b
'''
def main():
    '''
    Some test examples
    '''
    print(num_permutations_to_climb_stairs(2, 2))
    print(num_permutations_to_climb_stairs(5, 3)) # i.e. how many ways to go 
                                                  # up 6 steps when allowed to
                                                  # advance up to 3 steps at a
                                                  # time?
main()