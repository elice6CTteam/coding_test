def solution(phone_book):
    phone_book.sort()
    # 해당문제의 핵심은 코드의 효율성을 높이는 데 있습니다.
    # 문자열형태의 숫자가 나열되어있는 전화번호를 정렬하게되면 첫 문자의 크기부터 비교해 정렬하게됩니다.
    # 예를들어 12, 1213, 121 을 정렬하게되면 12 121 1213순으로 정렬되는것입니다.
    # 이렇게 정렬된 문자열이 있다면 양옆의 문자열만 비교해도 전체문자열에 각 문자열이 접두사에 포함되는지 검사할 수 있습니다.
    # 한번의 for문으로 모든 문자열을 탐색하기에 매우 효율적인 코드를 작성할 수 있습니다.
    # 또한 접두사의 존재유무는 startswith함수를 이용하면 쉽게 탐색할 수 있습니다.
    for i in range(1, len(phone_book)):
        if phone_book[i].startswith(phone_book[i - 1]):
            return False
    return True