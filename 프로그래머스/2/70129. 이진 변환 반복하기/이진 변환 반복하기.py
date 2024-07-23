def solution(s):
    count = 0
    zero_num = 0
    while s != '1':
        # 최초 s 저장
        prev = s
        # 0 삭제
        s = s.replace('0', '')
        # 사라진 0 개수
        zero_num += len(prev) - len(s)
        # 2 진수로 변환
        s = bin(len(s))[2:]
        # loop 한 번 당 count 1 추가
        count += 1
    
    return count, zero_num
