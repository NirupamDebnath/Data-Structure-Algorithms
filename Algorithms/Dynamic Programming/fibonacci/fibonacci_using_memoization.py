from timeit import default_timer as timer

def fib(n,lookup):
    if n == 0 or n == 1:
        lookup[n] = n
        return n

    if lookup[n] == None:
        lookup[n] = fib(n-2, lookup) + fib(n-1, lookup)
        return lookup[n]
    else:
        return lookup[n]


if __name__ == "__main__":
    n = 34
    lookup = [None] * (n+1)
    start = timer()
    res = fib(n, lookup)

    print(f"fibonacci of {n} is {res}")
    print(f'time taken {timer()-start:.8f}')
