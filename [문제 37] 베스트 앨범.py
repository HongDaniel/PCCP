from collections import defaultdict

genres=["classic", "pop", "classic", "classic", "pop"]
plays=[800, 600, 150, 800, 2500]
	

def solution(genres, plays):
    answer = []
    
    info = defaultdict(list)
    genre_total = defaultdict(int)

    # 장르별 통합 재생횟수
    for idx in range(len(genres)):
        info[genres[idx]].append((idx, plays[idx]))
        genre_total[genres[idx]] += plays[idx]

    genre_total = sorted(genre_total.items(), key=lambda x:x[1], reverse=True)
    new_info = []

    # 장르별로 고유번호, 플레이 횟수로 소팅
    for key, value in info.items():
        new_el = []
        new_el.append(key)
        new_value = sorted(value, key=lambda x: x[0])
        new_value = sorted(value, key=lambda x: x[1], reverse=True)
        new_el.append(new_value)
        new_info.append(new_el)
    
    for genre,plays in genre_total:
        for info in new_info:
            if info[0] == genre:
                answer.append(info[1][0][0])

                if len(info[1]) >= 2:
                    answer.append(info[1][1][0])

    return answer

solution(genres, plays)