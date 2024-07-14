def solution(n, m, section):
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