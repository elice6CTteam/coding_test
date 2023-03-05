#https://school.programmers.co.kr/learn/courses/30/lessons/42586
import math
# 진행률의 올림을 구하기위해 math라이브러리를 이용했습니다.
def solution(progresses, speeds):
    answer = []
    tmp_p = []
    # 남은 진행률에 개발속도를 나눠준 올림값이 총개발일수가 될것입니다.
    for i in range(len(progresses)):
        tmp_p.append(math.ceil((100 - progresses[i]) / speeds[i]))
    # 초기값 세팅
    cnt, old = 0, tmp_p[0]

    # for문을 돌면서 필요 개발일수가 같은 값을 모아서 answer에 이어붙입니다.
    for i in tmp_p[1:]:
        cnt += 1
        if old < i:
            answer.append(cnt)
            cnt, old = 0, i
    answer.append(cnt + 1)
    return answer