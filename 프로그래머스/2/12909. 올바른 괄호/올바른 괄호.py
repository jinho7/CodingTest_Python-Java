def solution(s):
    
    # 남아 있는 '(' 개수 저장
    count = 0
    for char in s:
        if char == '(':
            count += 1
        else:  # char == ')'
            # 스택이 비어있는데 오른쪽 괄호가 나온 경우
            if count == 0:  
                return False
            count -= 1
    # 모든 괄호가 올바르게 짝지어졌으면 0
    return count == 0