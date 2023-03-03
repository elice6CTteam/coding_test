def solution(arr):
    answer = []
    for a in arr:
        if answer[-1:] != [a]:  # 연속 같은 숫자인지 확인
            answer.append(a)
    return answer
