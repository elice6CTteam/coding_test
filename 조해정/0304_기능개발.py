def solution(progresses, speeds):
    answer = []

    date = 0    # 배포 가능 날짜
    for p, s in zip(progresses, speeds):
        need_days = -((p - 100) // s)       # 필요한 작업 일수
        # 앞의 기능이 완성되지 않으면 뒤에 기능들이 완성되어도 배포가 불가능
        if date < need_days:
            answer.append(1)
            date = need_days
        else:
            answer[-1] += 1

    return answer
