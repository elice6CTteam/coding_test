#https://school.programmers.co.kr/learn/courses/30/lessons/12906
def solution(arr):
    answer=[arr[0]]
    cnt=0
    # for문을돌며 같은숫자가 아닌경우 answer에 append해줍니다.
    for i in arr[1:]:
        new=i
        old=answer[cnt]
        if old!=new:
            answer.append(new)
            cnt+=1
    return answer