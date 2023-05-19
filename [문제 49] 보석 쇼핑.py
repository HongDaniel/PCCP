gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]	

'''

* 10만이 넘어가는 순간 투포인터를 이용해서 푼다.


'''

# from collections import defaultdict
# 

def solution(gems):
    gemSize = len(set(gems))
    answer = [0,len(gems)]
    gemDict = {gems[0]:1}
    leftP,rightP = 0,0
    print(gems)
    while leftP<len(gems) and rightP<len(gems):
        if len(gemDict) != gemSize: # 아직 다 안찼을 경우
            rightP+=1
            if rightP == len(gems):
                break
            if gems[rightP] in gemDict:
                gemDict[gems[rightP]]+=1
            else:
                gemDict[gems[rightP]]=1
        
        else: # 다 찼을 경우
            if rightP-leftP<answer[1]-answer[0]:
                answer[0] = leftP
                answer[1] = rightP
            
            else:
                gemDict[gems[leftP]]-=1
                if gemDict[gems[leftP]] ==0 :
                    del gemDict[gems[leftP]]
                leftP+=1

    answer=[answer[0]+1,answer[1]+1]
    return answer
            
                


solution(gems)