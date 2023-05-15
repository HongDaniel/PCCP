
def solution(record):
    answer = []
    userInfo = {}
    # 닉네임 변경 과정
    for r in record:
        info = r.split()
        if info[0] in ('Enter', 'Change'):
            userId = info[1]
            nickname = info[2]
            userInfo[userId] = nickname

    # 출력과정
    for r in record:
        info = r.split()
        command, userId = info[0], info[1]
        if command == 'Enter':
            answer.append(userInfo[userId]+'님이 들어왔습니다.')
        elif command == 'Leave':
            answer.append(userInfo[userId]+'님이 나갔습니다.')
    return answer