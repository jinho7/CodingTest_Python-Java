def my_solution(n, m, section):
    bit = list("1" * n)
    for i in range(len(section)):
        bit[section[i]-1] = "0"
    count = 0
       
    for i in range((n-m+1)):
        # 0만나면
        if bit[i] == "0":
            # m칸칸큼 1로 바꿈
            bit[i:i+m] = ["1"] * m
            count += 1

    bit.reverse()
    
    for i in range((n-m+1)):
        # 0만나면
        if bit[i] == "0":
            # m칸칸큼 1로 바꿈
            bit[i:i+m] = ["1"] * m
            count += 1
    
    return count


def solution(n, m, section):
    count = 0
    painted = 0
    
    # 안칠해진 영역 모두 돌기.
    for s in section:
        # 0 보다 크면 (처음에는 무조건 만남)
        # 여기 안걸리면 이전에 칠해버린거
        if s > painted:
            count += 1
            # 여기까진 칠해졌다! -> 섹션 + 페인트 -1
            painted = s + m - 1
    
    return count