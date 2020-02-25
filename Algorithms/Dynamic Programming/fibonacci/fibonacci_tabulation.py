from timeit import default_timer as timer

def fib(n):
    if n == 0 or n == 1:
        return n

    state_list = [0] * (n+1)

    state_list[0] = 0
    state_list[1] = 1

    for i in range(2,n+1,1):
        state_list[i] = state_list[i-2] + state_list[i-1]

    return state_list[n]



if __name__ == "__main__":
    n = 34
    
    start = timer()
    res = fib(n)

    print(f"fibonacci of {n} is {res}")
    print(f'time taken {timer()-start:.8f}')
