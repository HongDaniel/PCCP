strings = ["abce", "abcd", "cdx"]
n = 1

def solution(strings, n):
    return sorted(strings,key = lambda x: (x[n],x))

solution(strings, n)