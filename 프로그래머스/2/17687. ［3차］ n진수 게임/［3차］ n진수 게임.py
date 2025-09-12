def solution(n, t, m, p):
    # n 진법, t result 갯수, m 참가인원, 튜브 순서 p
    answer = ''
    answer_len = 0
    digits = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    
    all_num = 0
    full_str = '0'
    full_str_len = 1
    if p == 1:
        answer += full_str
        answer_len += 1
    while True:
        s = ''
        num = all_num
        while num != 0:
            x = num % n
            if x >= 10 : x = digits[x]
            s += str(x)
            num = num // n
        s = s[::-1]
        for i in range(len(s)):
            if ((full_str_len + i + 1) - p) % m == 0:
                answer += s[i]
                answer_len += 1
                if answer_len == t:
                    break
        if answer_len == t:
            break
        full_str_len += len(s)
        full_str += s
        all_num += 1
    
    return answer