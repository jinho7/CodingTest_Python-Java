def solution(s):
    str_stack = []
    
    for char in s:
        str_stack.append(char)
        if len(str_stack) >= 2 and str_stack[-2] == str_stack[-1]:
            str_stack.pop()
            str_stack.pop()
            
    return 0 if str_stack else 1 