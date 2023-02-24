def solution(nums):
    # 선택할 수 있는 폰켓몬 수
    n = len(nums) // 2
    # 주어진 입력의 폰켓몬 종류 수
    m = len(set(nums))

    # 선택할 수 있는 최대 폰켓몬 종류
    answer = m if m < n else n

    return answer
