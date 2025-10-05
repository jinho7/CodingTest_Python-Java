from collections import defaultdict, deque

def solution(storage, requests):
    
    n, m = len(storage), len(storage[0])
    is_box = [[1] * m for _ in range(n)]
    
    def use_forklift(alpha):
        # 외부와 닿아있는 부분 갱신 -> 실제 뺄 알파벳의 위치 탐색
        outside_targets = get_outside_contact(alpha)
        
        # 한 번에 제거
        for i, j in outside_targets:
            is_box[i][j] = 0
        
        return 0
    
    def use_crane(alpha):
        # 1. 모든 알파벳 검색 후, 빼주기
        for i in range(n):
            for j in range(m):
                if storage[i][j] == alpha:
                    is_box[i][j] = 0
        return 0
    
    def get_outside_contact(alpha):
        # 효율 생각 안하고, BFS
        
        # (n+2)x(m+2) 확장격자에서 (0,0) 바깥공기부터 BFS
        visited = [[False] * (m + 2) for _ in range(n + 2)]
        
        q = deque([(0, 0)])
        visited[0][0] = True

        outside_targets = set()

        # 외부 라운드 에서부터 색칠해 나간다고 생각하면 편함.
        while q:
            x, y = q.popleft()
            
            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                nx, ny = x + dx, y + dy
                
                # 격자 범위 외부 이거나, 방문 했으면 건너 뛰기
                if (not (0 <= nx <= n + 1 and 0 <= ny <= m + 1)) or visited[nx][ny]:
                    continue
                    
                # 방문 처리
                visited[nx][ny] = True
                
                # 1. 내부라면?
                if 1 <= nx <= n and 1 <= ny <= m:
                    # 실제 창고 내부 좌표로 치환
                    i, j = nx - 1, ny - 1
                    
                    # Box가 빠진 영역이라면, 색칠 & 계속 이동
                    if is_box[i][j] == 0:
                        q.append((nx, ny))
                    # is_box[i][j] == 1: 막혀 있다면, 색칠 X
                    else:
                        # 단, 알파벳이 alpha면 '외부 접촉이며, 뺄 알파벳' 후보에 추가
                        if storage[i][j] == alpha:
                            outside_targets.add((i, j))
                # 2. 확장격자 바깥(진짜 외부 공기)면, 색칠 & 계속 이동
                else:
                    q.append((nx, ny))
                
        return outside_targets

    for request in requests:
        # 지게차 [외부 연결만]
        if len(request) == 1:
            use_forklift(request)
        # 크레인 [모두]
        else:
            use_crane(request[0])
    
    return sum(map(sum, is_box))