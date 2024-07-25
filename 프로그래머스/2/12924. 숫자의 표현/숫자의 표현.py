def solution(n):
    # 연속되는 k개
    # n = (x+0) + (x+1) + (x+2) + ... + (x+(k-1)) 요론 느낌?
    # n = k * (x + x+(k-1)) / 2 = (2kx + k(k-1)) / 2
    # 2n = 2kx + k^2 - k
    # 2n - k^2 + k = 2kx
    # (2n - k^2 + k) / (2k) = x
    # x가 정수이려면, (2n - k^2 + k)가 2k로 나누어 떨어져야 됨. = k로 나누어 떨어져야 됨.
    count = 0
    # k를 1부터 증가시키면서 위 방정식을 만족하는 정수 x가 있는지 확인
    for k in range(1, n+1):
        # x가 정수이고 양수일 때마다 카운트를 증가시킵니다.
        if (n - k*(k-1)//2) % k == 0 and (n - k*(k-1)//2) // k > 0:
            count += 1
    return count

    return answer