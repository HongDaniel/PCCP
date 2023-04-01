s = "110010101001"


def solution(s):
    zeroCount = 0
    transform = 0
    while s != "1":
        newS = ""
        for l in s:
            if l == "1":
                newS += l
            else:
                zeroCount += 1
        binNum = bin(len(newS))
        s = binNum[2:]
        transform += 1
    # print(zeroCount, transform)
    answer = [transform, zeroCount]
    return answer


solution(s)
