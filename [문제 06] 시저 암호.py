s="a B z"
n=4
import string


def solution(s, n):
    small_letters   = list(string.ascii_lowercase)
    big_letters     = list(string.ascii_uppercase)
    answer = ''
    
    for letter in s:
        tmp = ' '
        if letter == ' ':
            answer+=tmp
            continue

        if letter in small_letters:
            idx = small_letters.index(letter)
            tmp = small_letters[(idx+n)%len(small_letters)]            

        if letter in big_letters:
            idx = big_letters.index(letter)
            tmp = big_letters[(idx+n)%len(small_letters)]            
        answer+=tmp
    return answer


solution(s, n)