def solution(s):
    n = len(s)
    
    # [초기 검증]: 홀수면 바로 0 반환
    if n % 2 != 0:
        return 0

    new_s = s * 2
    answer = 0
    correct_dict = {')': '(', ']': '[', '}': '{'}
    # correct_match = [['(',')'], ['[': ']'], ['{': '}']]
    
    def validate(x):
        # 삭제 처리: 보관용
        stack = []
        
        # find the (), [], {} and delete matched things
        for i in x:
            if i in correct_dict.values():
                stack.append(i)
            else:
                # 스택 끝 값 동일
                if stack and stack[-1] == correct_dict[i]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0

    for i in range(n):
        if validate(new_s[i:i+n]):
            answer += 1
    return answer