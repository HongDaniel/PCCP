answers = [1,2,3,4,5]


def check_answer(pattern,answer):
    print(pattern)
    print(answer)


def solution(answers):
    answer = []
    patterns = [[1,2,3,4,5],[2,1,2,3,2,4,2,5],[ 3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]

    for pattern in patterns[:1]:
        answer.append(check_answer(pattern,answers))

    return answer

solution(answers)