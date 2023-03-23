line = [[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]] # A,B,C 

from itertools import combinations as C
def find_intersection(line1,line2):
        A,B,E = line1
        C,D,F = line2
        if A*D - B*C != 0 :
                X=(B*F-E*D)/(A*D-B*C)
                Y=(E*C-A*F)/(A*D-B*C)
                if float(X).is_integer() and float(Y).is_integer():
                        return X,Y
def solution(line):
    answer = []
    tmp=[]
    maxX,maxY = -1001,-1001
    minX,minY = 1001,1001

    for i in range(len(line)) :
        for j in range(i+1,len(line)):
           
                        maxX,maxY = max(int(X),maxX),max(int(Y),maxY)
                        minX,minY = min(int(X),minX),min(int(Y),minY)

    answer = [['.'] * (maxX-minX+1) for i in range (maxY-minY+1)]
    for x,y in tmp:
        answer [y-minY][x-minX] = "*"

    answer = [''.join(a) for a in answer]
    answer.reverse()
    return answer

solution(line)