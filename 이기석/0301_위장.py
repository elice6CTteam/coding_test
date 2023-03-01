#https://school.programmers.co.kr/learn/courses/30/lessons/42578
def solution(clothes):
    # 의상의 종류에 따른 의류 개수를 딕셔너리로 만들어줍니다.
    # collections모듈의 defaultdict를 활용하면 아래 코드를 단순화할 수 있습니다!
    cloth_dict = {}
    for i in clothes:
        if i[1] not in cloth_dict:
            cloth_dict[i[1]]=1
        else:
            cloth_dict[i[1]]+=1

    # 다음으로 의상의 조합을 고려해야합니다.
    # 각 의상의 종류마다 스파이는 하나 이하의 옷을 선택할 수 있고, 무조건 하나 이상의 옷은 입어야합니다.
    # 그렇다면 각 의상의 종류마다 의류의 개수+1(안입는 선택지) 만큼의 경우의 수가 있고,
    # 경우의 수를 모두 곱한 값에서 - 1(아무것도 입지않은 경우는 없음으로 빼줌)의 값이 정답이 됩니다.
    # 이제 코드를 작성해봅시다.

    # math라이브러리의 prod함수를 이용하면 아래 for문을 생략할 수 있습니다.
    answer=1
    for i in cloth_dict.values():
        answer*=i+1
    return answer-1
