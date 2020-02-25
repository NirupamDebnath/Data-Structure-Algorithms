from timeit import default_timer as timer

def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-2)+fib(n-1)

if __name__ == "__main__":
    n = 34
    start = timer()
    print(f"fibonacci number of {n}: is {fib(n)}")
    print(f'\nTime taken {timer()-start}')