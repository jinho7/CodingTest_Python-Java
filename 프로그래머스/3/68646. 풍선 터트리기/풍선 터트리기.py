def solution(a):
    # 관점: 만약에 작은 걸 터뜨리는 찬스가 아예 없으면, 무조건 가장 작은 것만 하나만 살아남는다.
    # 관점: 'a[i]가 살아남을 수 있는가”를 판단하려면, 찬스 쓰는 타이밍, 어디에서 쓰냐가 중요
    # 관점: 어차피 양 쪽은 다 큰거만 사라진다. 순서가 그렇게 중요하지 않다.
    # 어차피 중앙으로 모이니까, 양쪽 다 큰것만 사라질 수 있는지!? 체크
    # = (왼쪽놈들 중 최솟값)이 a[i]보다 크거나 같아야 함
    # (오른쪽놈들 중 최솟값)이 a[i]보다 크거나 같아야 함 -> 둘 중에 하나 만족
    # 둘 다 만족시키면 => 찬스 안써도 됨.
    # 한 쪽만 만족? -> 만족 못시키는 쪽 만날 때 찬스 써버리면 됨 ㅇㅈ?
    
    # 각 최솟값 갱신 표 구하기
    
    # n이 1,000,000개 중첩 for 문 기피.
    n = len(a)
    left_min = [float('inf') for _ in range(n)]
    right_min = [float('inf') for _ in range(n)]
    left_min[0], right_min[n-1] = a[0], a[n-1]
    for i in range(1, n):
        left_min[i] = min(left_min[i-1], a[i])
    for i in range(n-2, -1, -1):
        right_min[i] = min(right_min[i+1], a[i])
    
    answer = 0
    
    for k in range(n):
        if a[k] <= left_min[k] or a[k] <= right_min[k]:
            answer += 1
              
    return answer