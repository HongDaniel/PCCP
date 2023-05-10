phone_book=["12","123","1235","567","88"]


def solution(phone_book):
    phone_book.sort()
    for idx in range(len(phone_book)-1):
        if phone_book[idx+1].startswith(phone_book[idx]):
            return False
    return True

solution(phone_book)


#123
#4567
#1235858
