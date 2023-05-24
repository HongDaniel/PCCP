numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]	
hand = "right"

def solution(numbers, hand):
    answer = ''
    left = [1,4,7]
    right = [3,6,9]
    middle = {2:0,5:1,8:2,0:3}

    left_pos = -1
    right_pos = 1


    for num in numbers:
        
        if num in left: # 무조건 왼쪽 손
            answer+='L'
            left_pos = num

        elif num in right: # 무조건 오른쪽 손
            answer+='R'
            right_pos=num

        else: # 가운데 숫자
            left_distance, right_distance = 0, 0
            if left_pos not in middle.keys():   
                left_distance = abs(middle[left_pos+1]-middle[num])+1
            else:
                left_distance = abs(middle[left_pos]-middle[num])

            if right_pos not in middle.keys():
                right_distance = abs(middle[right_pos-1]-middle[num])+1
            else:
                right_distance = abs(middle[right_pos]-middle[num])
            
            if right_distance>left_distance:
                answer+='L'
                left_pos = num

            elif right_distance<left_distance:
                answer+='R'
                right_pos = num
            else:
                if hand == 'right':
                    answer+='R'
                    right_pos = num
                else:
                    answer+='L'
                    left_pos = num
    return answer



solution(numbers, hand)