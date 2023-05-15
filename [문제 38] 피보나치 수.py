def solution(n):
    ar = [0,1]
    for i in range(2,100001):
        new_num = (ar[i-1]%1234567 + ar[i-2]%1234567)%1234567
        ar.append(new_num)
        if i == n :
            return new_num