from itertools import combinations

def solution(n, times):
    l = (n//len(times) + 1)*min(times)
    r = (n//len(times) + 1)*max(times)
    
    while l <= r:
        m = (l + r) // 2
        people = sum(m // time for time in times)
        if people >= n:
            answer = m
            r = m -1
        else:
            l = m + 1
    return answer