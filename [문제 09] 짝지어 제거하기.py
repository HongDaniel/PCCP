s='baabaa'

#스택을 활용한 풀이


def solution(s):
    stack=[s[0]]

    for letter in s[1:]:
        if stack and stack[-1] == letter:
            stack.pop()
            continue
        stack.append(letter)

    if len(stack)==0:
        return 1
    else:
        return 0
        
    

solution(s)