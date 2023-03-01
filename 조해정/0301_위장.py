def solution(clothes):
    answer = 1

    # 의상 종류별 의상 개수
    spy = {}
    for cloth, kind in clothes:
        if kind not in spy:
            spy[kind] = 1
        else:
            spy[kind] += 1

    # 얼굴 의상을 입고 있다면 상의 의상을 입고 있지 않아도 된다.
    # 따라서 안 입는 경우까지 포함해 한 종류당 (k+1) 의 경우가 존재한다. (k=종류별 의상개수)
    kinds = list(spy.values())
    for k in kinds:
        answer *= (k + 1)  # and의 관계라 곱하기
    # 스파이는 하루에 최소 한 개의 의상을 입어야 하기 때문에 아무것도 입지 않은 경우 하나는 빼줘야 한다.
    answer -= 1

    return answer
