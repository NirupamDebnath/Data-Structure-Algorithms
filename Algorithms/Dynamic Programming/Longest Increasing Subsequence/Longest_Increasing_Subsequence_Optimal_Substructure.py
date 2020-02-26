"""
Problem Statememnt: 
The Longest Increasing Subsequence (LIS) problem is to find
the length of the longest subsequence of a given sequence such that all elements 
of the subsequence are sorted in increasing order. For example, the length of LIS
for {10, 22, 9, 33, 21, 50, 41, 60, 80} is 6 and LIS is {10, 22, 33, 50, 60, 80}.

"""
from timeit import default_timer as timer

def calc_lis(seq):
    n = len(seq)
    lis = [1] * n

    for i in range(1,n):
        for j in range(0,i):
            if seq[i] > seq[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1

    print(lis)
    
    return max(lis)


if __name__ == "__main__":
    seq = [10, 22, 9, 33, 21, 50, 41, 60]
    start = timer()
    res = calc_lis(seq)
    print(f"Time taken {timer() - start:.8f}")

    print("LIS: ",res)
