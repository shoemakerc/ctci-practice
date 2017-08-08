def num_permutations_to_climb_stairs(n):
    '''
    Uses memoization to compute the number of possible permutations to climb n
    steps when allowed to advance up to 3 steps at one time

    Time complexity: O(n)
    Space complexity: O(n)
    '''

    permutations = [-1] * (n + 1)
    return count_ways(n, permutations)
def count_ways(n, memo):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif memo[n] > -1:
        return memo[n]
    else:
        memo[n] = count_ways(n - 1, memo) + count_ways(n - 2, memo) + count_ways(n - 3, memo)
    return memo[n]
def main():
    '''
    Examples
    '''
    print(num_permutations_to_climb_stairs(3))
main()