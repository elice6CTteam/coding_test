def solution(s):
    stack = 0
    for c in s:
        stack = stack + 1 if c == "(" else stack - 1
        if stack < 0:
            return False
    if stack != 0:
        return False
    return True
