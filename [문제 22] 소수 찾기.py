numbers = "17"

from itertools import permutations as P

def check_prime(num):
    if num < 2 :
        return False
    
    for i in range(2,num//2+1):
        if num % i ==0:
            return False
    return True

def solution(numbers):
    answer = 0
    candi= set()
    
    for i in range(1,len(numbers)+1):
        tmp=list(P(numbers,i))
        for el in tmp:
            candi.add(int(''.join(el))) 

    for el in candi:
        if check_prime(el):
            answer+=1
    
    return answer


solution(numbers)