#https://school.programmers.co.kr/learn/courses/30/lessons/1845
def solution(nums):
    # 문제의 설명을 보면 주어지는 몬스터들의 종류는 중복이 될 가능성이 있습니다.
    # 주어진 n마리의 몬스터 중 n/2개 만큼 선택할 때를 생각해야합니다.

    # 1. 만약 모든 몬스터가 중복이 되지 않을 경우, n/2 종류만큼의 몬스터를 얻을 수 있습니다.
    # 2. 만약 모든 몬스터가 중복되어 있다면 몬스터의 수는 n/2보다 작고 최소 1종류의 몬스터를 얻을 수 있을 것입니다.

    # set()함수를 이용하게 되면 중복되는 값을 쉽게 제거할 수 있고, 중복되지 않은 값의 개수를 알 수 있습니다.
    # 이를 이용해 얻은 최소 종류수와 단순히 n/2개를 고를 경우 중 더 작은값이 결국 유저가 얻을 수 있는 종류수 일것입니다.

    # 풀이를 위해서는 min(), set(), len(), int() 함수가 필요합니다.
    # min(a,b) : a와 b중 더 작은값을 반환하는 함수입니다.
    # set(list) : list를 세트(집합)으로 변경해주는 함수입니다. list 내 중복되는 인자를 제거해줍니다.
    # len(arr) : arr의 길이를 구해주는 함수입니다. 주어진 배열의 길이를 정수형으로 반환해줍니다.
    # int(float) : 코드에서 2로 나눠줌으로서 반환되는 값의 형태가 실수 형인 것을 변환해주는 역할을 합니다.

    return min(len(set(nums)),int(len(nums)/2))