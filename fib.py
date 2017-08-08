def fib(n):
    arr = [0] * (n + 1)
    return fib_helper(n, arr)

def fib_helper(n, memo):
    if n == 0 or n == 1:
        return n
    if memo[n] == 0:
        memo[n] = fib_helper(n - 1, memo) + fib_helper(n - 2, memo)
    return memo[n]

def main():
    print(fib(20))
main()