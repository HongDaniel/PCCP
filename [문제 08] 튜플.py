s = "{{2},{2,1,3},{2,1},{2,1,3,4}}"	
import re
def solution(s):
    answer = []
    tmp=set()
    ar = re.split('},{',s[2:-2])
    ar.sort(key=len) # 길이 정렬
    for string in ar:
        newAr = re.split(',',string)
        for s in newAr:
            if int(s) not in tmp:
                answer.append(int(s))
            tmp.add(int(s))
    print(answer)     
    return answer

solution(s)


"""
파이썬 re에 대한 정리

match(패턴,문자열,플래그) - 문자열의 처음부터 시작해서 작성한 패턴이 일치하는지 확인
re.match('a','ab') ->  <re.Match object; span=(0, 1), match='a'>
re.match('a','ba') ->  None

search(패턴,문자열,플래그) - 문자열에서 작성한 패턴이 존재하는지 확인
re.search('a','ab') ->  <re.Match object; span=(0, 1), match='a'>
re.search('a','ba') ->  <re.Match object; span=(1, 2), match='a'>

findall(패턴,문자열,플래그) - 문자열 안에 맞는 케이스를 전부 찾아서 리스트로 반환
re.findall('\d', '숫자123이 이렇게56 있다8') -> ['1','2','3','5','6','8']

fullmatch(패턴,문자열,플래그) - 문자열에 시작과 끝이 정확하게 패턴과 일치할 때 반환
re.fullmatch('a','a') -> <re.Match object; span=(0, 1), match='a'>

split(패턴,문자열,최대 split 수,플래그) - 문자열에서 패턴이 맞으면 이를 기점으로 리스트로 쪼개는 함수
re.split('a', 'abaabca') -> ['', 'b', '', 'bc', '']

sub(패턴,교체할 문자열,문자열,최대 교체 수) - 문자열에서 패턴을 발견할 경우 교체할 문자열로 교체한다
re.sub('a', 'z', 'aaaab') -> zzzzb


"""