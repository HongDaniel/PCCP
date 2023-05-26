skill = "CBD"	
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]	


def solution(skill, skill_trees):
    answer = 0
    
    for candi in skill_trees:
        tmp=''
        for step in candi: 
            if step in skill:
                tmp += step
        
        if skill[0:len(tmp)] == tmp:
            answer+=1
    return answer

solution(skill, skill_trees)