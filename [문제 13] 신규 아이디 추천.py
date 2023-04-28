import re 

new_id="z-+.^."

def solution(new_id):
    answer = ''
    
    # step1
    answer = new_id.lower()

    # step2
    answer = re.sub('[^a-z0-9\-_.]','',answer)

    # step3
    answer = re.sub('\.+','.',answer)

    # step4
    answer = re.sub('^[.]|[.]$','',answer)

    # step5
    if answer == '':
        answer = 'a'

    #step6
    if len(answer) > 15:
        answer = answer[:15]
    if answer[-1] == '.':
        answer = answer[:-1]

    #step7
    if len(answer)<3:
        addLetter = answer[-1]
        while(len(answer)<3):
            answer += addLetter
    # print(answer)
    return answer

solution(new_id)