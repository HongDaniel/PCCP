arr1= [[1,2], [3,4], [5,6]]	
arr2=[[2,1], [2, 1]]

def solution(arr1, arr2):
    answer = []
    
    arr1_row = len(arr1)
    arr1_col = len(arr1[0])
    arr2_col = len(arr2[0])

    for row1 in range(arr1_row):
        tmp=[]
        for col2 in range(arr2_col):
            el=0
            for col1 in range(arr1_col):
                    el+= arr1[row1][col1] * arr2[col1][col2]
            tmp.append(el)
        answer.append(tmp)
    return answer

solution(arr1, arr2)