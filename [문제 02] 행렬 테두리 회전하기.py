rows = 6
columns = 6
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]


def rotate(board,query): 
    x1,y1 = query[0]-1, query[1]-1
    x2,y2 = query[2]-1, query[3]-1

    stack=[]
    for y in range(y1,y2+1):
        stack.append(board[x1][y])
        if len(stack) == 1:
            continue
        board[x1][y] = stack[-2]
    
    for x in range(x1+1,x2+1):
        stack.append(board[x][y2])
        board[x][y2]=stack[-2]

    for y in range(y2-1,y1-1,-1):
        stack.append(board[x2][y])
        board[x2][y] = stack[-2]
    
    for x in range(x2-1,x1-1,-1):
        stack.append(board[x][y1])
        board[x][y1]=stack[-2]

    return board,min(stack)

def solution(rows, columns, queries):
    answer = []

    # Board 초기세팅
    board = [[0]*columns for _ in range(rows)]
    for i in range(rows):
        for j in range(1,columns+1):
            board[i][j-1] = i*columns +j
    
    for query in queries:
        board,smallest = rotate(board,query)
        answer.append(smallest)
    
    print(answer)
    return answer

solution(rows, columns, queries)