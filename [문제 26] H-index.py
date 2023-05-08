citations = [1, 4, 5]

def solution(citations):
    ref, answer = 0, 0
    citations.sort()

    for ref in range(0,citations[-1]+1):
        cnt = 0 
        for el in citations:
            if el>= ref:
                cnt+=1
        if cnt>=ref:
            answer = ref

    return answer

solution(citations)