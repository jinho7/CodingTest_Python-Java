from collections import deque

def solution(x, y, n):
    answer = 0
    # Greedy bfs 로 탐색 / 백트레킹
    q = deque([(x, 0)])
    visited = set([x])
    
    if x == y:
        return 0
    
    while q:
        cur, count = q.popleft()
        for nxt in (cur + n, cur * 2, cur * 3):
            if nxt == y:
                return count + 1
            elif nxt < y and nxt not in visited:
                q.append((nxt, count + 1))
                visited.add(nxt)
            
    return -1