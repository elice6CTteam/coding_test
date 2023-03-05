# https://school.programmers.co.kr/learn/courses/30/lessons/12909
def solution(s):
    idx_dict = {"(": [], ")": []}
    for i in range(len(s)):
        idx_dict[s[i]].append(i)

    # 두 부호의 개수가 다르면 false
    if len(idx_dict["("]) != len(idx_dict[")"]):
        return False

    idx_dict["("] = list(reversed(idx_dict["("]))
    idx_dict[")"] = list(reversed(idx_dict[")"]))
    # 여는괄호가 앞에 닫는괄호보다 후순위에 있다면 false
    for i in range(len(idx_dict["("])):
        o, c = idx_dict["("][i], idx_dict[")"][i]
        if o > c:
            return False

    return True