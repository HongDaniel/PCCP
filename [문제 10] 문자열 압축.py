s = "a"

"""
1. 1~절반까지 단위로 자른다
2. 각각의 문자열을 구한다
abcabcdede 인경우
1) abcabcdede ... 10
2) abcabc2de  ... 
3) 2abcdede
"""


def solution(s):
    answer = [len(s)]
    if len(s) == 1:
        return 1
    for length in range(1, len(s)//2+1):
        # for length in range(1, 2):  # 3으로 자름
        sameLetter = 1
        newS = ""
        i = 0
        while i < len(s)-length:  # length = 1 i=0
            if s[i:i+length] == s[i+length:i+(length*2)]:
                sameLetter += 1
            else:
                if sameLetter > 1:
                    newS += str(sameLetter)+s[i:i+length]
                else:
                    newS += s[i:i+length]
                sameLetter = 1
            i += length

        if sameLetter > 1:
            newS += str(sameLetter)+s[i:]
        else:
            newS += s[i:]
        answer.append(len(newS))
    return min(answer)


solution(s)
