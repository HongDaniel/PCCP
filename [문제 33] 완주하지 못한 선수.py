participant = ["leo", "kiki", "eden"]	
completion = ["eden", "kiki"]	

def solution(participant, completion):
    participant.sort()
    completion.sort()

    for idx in range(len(completion)):
        if completion[idx] != participant[idx]:
            return participant[idx]
    return participant[-1]
    
solution(participant, completion)