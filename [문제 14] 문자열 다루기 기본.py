s= "a234"	
def solution(s):
    return True if len(s) in (4,6) and s.isdigit() else False

solution(s)