clothes= [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]	

from collections import defaultdict

def solution(clothes):
    answer = 1

    dict = defaultdict(list)
    for cloth,kind in clothes:
        dict[kind].append(cloth)

    for key in dict:
        answer*=len(dict[key])+1
    
    answer-=1
    return answer

solution(clothes)