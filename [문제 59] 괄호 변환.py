p = "()))((()"			

def check_right(p):
    flag = 0
    for i in range(len(p)):
        if p[i] == '(':
            flag += 1
        else:
            flag -= 1
        if flag<0:
            return False
    return True


# 재귀함수 같은 경우에는 return문을 신경쓰자

def solution(p):
    answer = ''

    if check_right(p):
        return p
    
    # step 1 
    if p == '':
        return ''
    
    # step 2 
    flag = 0
    u,v = '', ''

    for i in range(len(p)):
        if p[i] == '(':
            flag += 1
        else:
            flag -= 1
        if flag == 0:
            u = p[:i+1]
            v = p[i+1:]
            break
    
    # step 3
    if check_right(u):
        return u + solution(v)

    # step 4
    else:
        tmp = '(' + solution(v) + ')'
        new_s = ''
        for ex in u[1:-1] : # 뒤집기
            if ex == '(':
                new_s += ')'
            else:
                new_s += '('

        tmp+= new_s
        return tmp
        

solution(p)