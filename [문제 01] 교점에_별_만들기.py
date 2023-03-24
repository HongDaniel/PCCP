line = [[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]] # A,B,C 

from itertools import combinations as C
def find_intersection(line1,line2):
        A,B,E = line1
        C,D,F = line2
        if A*D - B*C != 0 :
                X=(B*F-E*D)/(A*D-B*C)
                Y=(E*C-A*F)/(A*D-B*C)
                if float(X).is_integer() and float(Y).is_integer():
                        return int(X),int(Y)
                
def solution(line):
    answer = []
    tmp=[]
    x_points, y_points = set(),set()

    for line1, line2 in C(line,2):
          intersection = find_intersection(line1,line2)
          if intersection:
                x,y = intersection
                x_points.add(x)
                y_points.add(y)
                tmp.append([x,y])
    maxX, maxY = max(x_points),max(y_points)
    minX, minY = min(x_points),min(y_points)
    
    answer = [['.'] * (maxX-minX+1) for i in range (maxY-minY+1)]
    for x,y in tmp:
        answer [y-minY][x-minX] = "*"

    answer = [''.join(a) for a in answer]
    answer.reverse()
    print(answer)
    return answer

solution(line)