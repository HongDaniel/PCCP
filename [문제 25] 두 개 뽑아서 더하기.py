numbers = [5,0,2,7]		

from itertools import combinations as C

def solution(numbers):
    answer = set()
    for a,b in C(numbers,2):
        answer.add(a+b)
    answer = list(answer)
    answer.sort()
    return answer

solution(numbers)