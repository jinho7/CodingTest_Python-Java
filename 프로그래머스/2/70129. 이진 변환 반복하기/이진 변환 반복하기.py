def solution(s):
    count = 0
    zero_num = 0
    while s != '1':
        prev = s
        s = s.replace('0', '')
        zero_num += len(prev) - len(s)
        s = bin(len(s))[2:]
        
        count += 1
    
    return count, zero_num