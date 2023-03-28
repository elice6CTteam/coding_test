from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0

    # length만큼 0으로 이루어진 배열 [0, 0, ... , 0]
    on_bridge = deque([0 for _ in range(bridge_length)])
    use_weight = 0  # 다리에 올라간 트럭 총 무게

    trucks = deque(truck_weights)
    while trucks:
        # 현재 다리에 있는 트럭들과 새 트럭의 무게 총합이 한도 무게를 초과하지 않으면 트럭 올림
        # 아니면 트럭 안 올림 (= 무게가 0인 트럭 올림)
        use_weight -= on_bridge.popleft()
        if use_weight + trucks[0] <= weight:
            use_weight += trucks[0]
            on_bridge.append(trucks[0])
            trucks.popleft()
        else:
            on_bridge.append(0)
        answer += 1

    # 다리에 갓 올라온 마지막 트럭이 다리를 지나는 소요 시간 추가
    answer += bridge_length

    return answer
