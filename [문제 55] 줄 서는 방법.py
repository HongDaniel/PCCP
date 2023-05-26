n=20
k=555

import math

def solution(n, k):
    Nums = list(range(1, n+1))
    Answer = []

    while n != 0:
        temp = math.factorial(n-1)
        Index = (k-1)//temp
        k = k % temp
        Answer.append(Nums.pop(Index))
        n -= 1
    
    return Answer
