def solution(priorities, location):
    stack = []
    answer = 0

    job = priorities[location]

    # 중요도 숫자 별 개수
    number_dict = {i: 0 for i in range(1, 10)}
    for n in priorities:
        number_dict[n] += 1

    priorities = list(map(str, priorities))
    priorities_str = ''.join(priorities)
    for i in range(9, 0, -1):
        if number_dict[i] == 0:
            continue

        if job != i:
            # 중요도가 높은 건 무조건 job보다 앞에 있으니까
            answer += number_dict[i]

            # 문자열 split, 나눠진 리스트들 중 제일 뒷값은 항상 제일 앞
            priorities = priorities_str.split(str(i))

            # job 위치 값 최신화 (남은 문자열에서의 새 위치)
            total = len(priorities_str)  # 남은 중요도 총 개수
            if location >= total - len(priorities[-1]):
                location -= (total - len(priorities[-1]))
            else:
                cnt, cnt_i = 0, 0
                for p in priorities:
                    cnt += len(p)
                    if location < cnt + cnt_i:
                        location = location - cnt_i + len(priorities[-1])
                        break
                    cnt_i += 1
            priorities_str = priorities[-1] + ''.join(priorities[:-1])
        else:
            # 같은 중요도 중에서 몇 번째 job인지에 따라 추가
            answer += priorities_str[:(location + 1)].count(str(i))
            break

    return answer
