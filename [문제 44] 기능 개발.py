progresses = [95, 90, 99, 99, 80, 99]		
speeds = [1, 1, 1, 1, 1, 1]	

def solution(progresses, speeds):
    answer = []
    endDate = []

    # 각 과정 별 끝나는 날짜는 구하는 부분
    for progress,speed in zip(progresses,speeds):
        if (100-progress)%speed == 0:
            endDate.append([(100-progress)//speed,True])
        else:
            endDate.append([(100-progress)//speed+1,True]) 
    
    maxNum = 0 
    
    # 배포 갯수 세기
    for i in range(len(endDate)):
        cnt=1
        maxNum = max(maxNum,endDate[i][0])
        if endDate[i][1]:
            for j in range(i+1,len(endDate)):
                if endDate[j][0]>maxNum:
                    break
                endDate[j][1]=False
                cnt+=1
            answer.append(cnt)

    return answer

solution(progresses, speeds)