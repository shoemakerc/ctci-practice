def num_permutations_to_climb_stairs(n, k):
    if n == 0 or n == 1:
        return 1
    combinations = [0] * (n + 1)
    combinations[0] = 1
    combinations[1] = 1
    for i in range(2, n + 1):
        j = 0
        while (j <= k):
            combinations[i] += (combinations[i - j] if i - j >= 0 else 0)
            j += 1
    print(combinations)
    return combinations[-1]
def main():
    '''Some test examples'''
    print(num_permutations_to_climb_stairs(4, 2))
    print(num_permutations_to_climb_stairs(6, 3)) # i.e. how many ways to go up 6 steps when allowed to advance up to 3 steps at a time?
    print(num_permutations_to_climb_stairs(0, 0))
    print(num_permutations_to_climb_stairs(2, 10))
    print(num_permutations_to_climb_stairs(1, 3))
    print(num_permutations_to_climb_stairs(3, 1))
    print(num_permutations_to_climb_stairs(5, 4))
main()