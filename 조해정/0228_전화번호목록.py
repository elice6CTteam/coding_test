def solution(phone_book):
    answer = True

    # 문자열이기 때문에 정렬하면 전화번호 길이 상관없이 앞자릿수가 작은 숫자가 우선
    # "123", "1234", "125", "2", "297" 이런 식으로
    phone_book.sort()

    for i in range(len(phone_book) - 1):
        num1, num2 = phone_book[i], phone_book[i + 1]
        l1, l2 = len(num1), len(num2)

        # 같은 번호는 존재하지 않으니 앞에 정렬된 숫자의 길이가 더 크거나 같으면 접두사 불가
        if l1 < l2:
            # 접두사인지 확인
            if num2.startswith(num1):
                answer = False
        # 하나라도 접두사인 경우가 있으면 반복문 종료
        if not answer:
            break

    return answer
