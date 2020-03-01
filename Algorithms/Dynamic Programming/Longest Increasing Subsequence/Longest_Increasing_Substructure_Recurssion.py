"""
Problem Statememnt: 
The Longest Increasing Subsequence (LIS) problem is to find
the length of the longest subsequence of a given sequence such that all elements 
of the subsequence are sorted in increasing order. For example, the length of LIS
for {10, 22, 9, 33, 21, 50, 41, 60, 80} is 6 and LIS is {10, 22, 33, 50, 60, 80}.
"""

from timeit import default_timer as timer

global maximum

def _lis(arr, n):
    global maximum
    if n == 1:
        return 1
    
    maxEndingHere = 1

    for i in range(1,n):
        res = _lis(arr, i)
        if arr[i-1] < arr[n-1] and res + 1 > maxEndingHere:
            maxEndingHere = res + 1

    maximum = max(maximum, maxEndingHere)

    return maxEndingHere

if __name__ == "__main__":
    global maximum
    maximum = 1
    seq = [10, 22, 9, 33, 21, 50, 41, 60]
    n = len(seq)
    start = timer()
    res = _lis(seq,n)
    print(f"Time taken {timer() - start:.8f}")

    print("LIS: ",maximum)