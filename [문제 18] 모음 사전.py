word = "I"

# 1. 원하는 단어가 생성될 때까지 단어를 생성한다.
from itertools import product

def solution(word):
    answer = 0
    dic = ['A','E','I','O','U']
    candi = []
    for i in range(1,6):
        for el in product(dic,repeat=i):
            candi.append(''.join(el))
    candi.sort()
    print(candi.index(word)+1)
    return (candi.index(word)+1)




solution(word)