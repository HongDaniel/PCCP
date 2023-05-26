numbers = [1,1,1,1,1]
target = 3

# DFS를 활용한 풀이 (재귀)

def dfs (idx,numbers,target,value):
    cnt =0 

    if idx == len(numbers):
        if value == target:
            return 1
        else:
            return 0
    cnt += dfs(idx+1,numbers,target,value+numbers[idx])
    cnt += dfs(idx+1,numbers,target,value-numbers[idx])
    
    return cnt

def solution(numbers, target):
    answer = dfs(0,numbers,target,0)
    return answer

solution(numbers, target)