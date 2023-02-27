def solution(participant, completion):
    answer = ''
    if not completion:   # 참가자가 한 명이라면 무조건 그 사람이 완주 못 한 사람
        return participant[0]

    players = {}
    for p in participant:
        if p not in players:
            players[p] = 1
        else:
            players[p] += 1

    for c in completion:
        if players[c] > 1:
            players[c] -= 1
        else:
            del players[c]

    answer = list(players.keys())[0]
    return answer
