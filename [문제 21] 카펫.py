brown = 8
yellow = 1

# 가로*2 + 세로 *2  = brown +4 
# 가로 = (brown+4 - 2*세로)/2
# (가로-2)*(세로-2) = yellow 
# (brown-2*세로)*(세로-2) = 2*yellow

def solution(brown, yellow):
    answer = []
    for vertical in range(3,brown):
        if ((brown-2*vertical)*(vertical-2)) == 2*yellow:
            answer.append(int((brown+4-2*vertical)/2))
            answer.append(vertical)
            break
    return answer


solution(brown, yellow)