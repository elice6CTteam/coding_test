cloth1 = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]

cloth2 = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]



def solution(clothes):
    answer = 1
    n = {}

    for (cloth, key) in clothes:
        if key in n:
            n[key] += 1
        else:
            n[key] = 1

    for i in n.values():
        answer *= (i+1)

    return answer-1


print(solution(cloth1))
print(solution(cloth2))