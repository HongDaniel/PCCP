n =2 

# 하노이의 탑을 재귀로 풀어보기
# 1. n-1개의 블록을 2번으로 옮긴다. -> n-2개의 블록을 3번으로 옮긴다.
# 2. 가장 큰 블록을 3번으로 옮긴다.
# 3. n-1개의 블록을 3번으로 옮긴다.

def hanoi(n,a,b,history):
    if n == 0 :
        return 0
    
    hanoi(n-1,a,6-(a+b),history) # n-1개를 2번으로 옮김
    history.append([a,b])
    hanoi(n-1,6-(a+b),b,history)
    return history

def solution(n):
    print(hanoi(n,1,3,[]))
    return hanoi(n,1,3,[])

solution(n)