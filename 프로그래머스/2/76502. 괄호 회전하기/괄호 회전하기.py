def solution(s):
    s2 = s+s
    answer = 0
    for i in range(len(s)):
        if is_right(s2[i:len(s)+i]):
            answer += 1
    return answer

# 참고함
def is_right(s):
    stack = []
    matching = {')': '(', ']': '[', '}': '{'}
    
    for char in s:
        if char in matching.values():
            stack.append(char)
        elif char in matching:
            if stack and stack[-1] == matching[char]:
                stack.pop()
            else:
                return False
    return len(stack) == 0

# "{(})" 케이스 해결 못하겠음