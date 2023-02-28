participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

def solution(participant, completion):
    participant.sort()
    completion.sort()

    print(participant)
    print(completion)

    for a,b in zip(participant,completion):
        if a != b:
            return a
    
    return participant[-1]

print(solution(participant, completion))