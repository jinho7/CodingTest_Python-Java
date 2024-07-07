def solution(s):
    a = len(s)//2
    return s[a:a+1] if len(s) % 2 else s[a-1:a+1]
    # return str[(len(str)-1)//2 : len(str)//2 + 1] 천재네