phone_book1 = ["119","97674223","1195524421"]
phone_book2 = ["123","456","789"]
phone_book3 = ["12","123","1235","567","88"]

def solution(phone_book):
    phone_book.sort()
    len1 = len(phone_book)-1

    for i in range(len1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False

    return True

    
print(solution(phone_book1))
print(solution(phone_book2))
print(solution(phone_book3))
