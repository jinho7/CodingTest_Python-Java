from collections import defaultdict

def solution(n, results):
    # 정확한 순위를 알 수 있는 선수의 수 = 나를 제외한 강한 사람 / 약한 사람 모두 알기
    # = 강 / 약 의 합이 n-1
    
    # 1이 2를 이기고, 2가 3을 이기면 → 1은 3보다 강하다 이런건 어떻게 판단?
    # 그래프 탐색으로 타고 들어가서 추가해주자.
    
    # i가 이긴 사람들
    win_graph = defaultdict(list)
    # i가 진 사람들
    lose_graph = defaultdict(list)
    
    for l, w in results:
        win_graph[l].append(w)
        lose_graph[w].append(l)
    
    # 탐색으로 이긴 사람, 진 사람 체크하기
    def dfs(start, graph, visited):
        for next_player in graph[start]:
            if next_player not in visited:
                visited.add(next_player)
                dfs(next_player, graph, visited)
    
    answer = 0
        
    for i in range(1, n+1):
        win_visited = set()
        lose_visited = set()
        
        # 그래프 전파 및 visited 추가.
        dfs(i, win_graph, win_visited)
        dfs(i, lose_graph, lose_visited)
        
        print(win_visited, lose_visited)
        if len(win_visited) + len(lose_visited) == n - 1:
            answer += 1
        
    return answer