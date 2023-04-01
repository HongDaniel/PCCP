import math
n = 2

"""
1. 직접 n진법 구하기
2. 라이브러리 사용
"""


def solution(n):
    tmp = []
    answer = 0
    while n >= 3:  # 15
        tmp.append(n % 3)  # 0
        n = n//3
    tmp.append(n)
    tmp.reverse()
    for i in range(len(tmp)):
        answer += int(tmp[i]*math.pow(3, i))
    print(answer)
    return answer


solution(n)
