prices=[1, 2, 3, 2, 3]	

def solution(prices):
    answer = []
    
    for i in range(len(prices)):
        cnt=0
        for j in range(i+1,len(prices)):
            cnt+=1
            if prices[i]>prices[j] or j == len(prices)-1:
                answer.append(cnt)
                break
    answer.append(0)
    return answer

solution(prices)