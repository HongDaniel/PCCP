s = "try hello world"

def solution(s):
    answer = ''
    order=0
    for i in range(len(s)):
        if s[i] == " ":
            order = 0
            answer+=s[i]
            continue
        if order%2 == 0:
            answer+=s[i].upper()
        else:
            answer+=s[i].lower()
        order+=1

    # print(answer)        
    return answer

solution(s)