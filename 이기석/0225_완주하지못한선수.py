#https://school.programmers.co.kr/learn/courses/30/lessons/42576
def solution(participant, completion):
    # collections 내 counter 함수를 이용하면 더욱 쉽게 문제를 풀 수 있지만
    # 라이브러리를 이용하지 않고 풀어보겠습니다.
    # 완주하지 못한 선수는 한명 뿐이고 동명이인이 있을 수 있습니다.
    # 해당 문제의 풀이는 다음과 같을 것입니다.
    # 딕셔너리를 만들어 participant에서 선수의 이름을 순서대로 세어나간 후,
    # completion에서 이름에 따라 딕셔너리 내 값을 빼나가면 됩니다.

    # 아래 코드는 participant를 딕셔너리화 하는 과정입니다.
    # 이름에 따라 몇명의 사람이 있는지 집계합니다.
    person_dict={}
    for i in participant:
        if i not in person_dict:
            person_dict[i]=1
        else:
            person_dict[i]+=1

    # 아래 함수는 completion을 통해 만들어진 딕셔너리에서
    # 이름에 따라 그 값을 줄여나가고, 해당 값이 0이된다면 딕셔너리에서 제거합니다.
    for i in completion:
        person_dict[i]-=1
        if person_dict[i]==0:
            del person_dict[i]
    # 결국 남아있는 딕셔너리의 키는 하나이며 해당인물이 완주하지 못한 선수입니다.
    return list(person_dict)[0]