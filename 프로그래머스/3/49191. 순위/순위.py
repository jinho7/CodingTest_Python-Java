from collections import defaultdict

# Floyd-Warshall 방법으로도 풀어보자.
def solution(n, results):
    # 1. 초기 그래프 세팅 (문자열: 'Win', 'Lose', 'Unknown')
    graph = [['Unknown' for _ in range(n+1)] for _ in range(n+1)]
    
    for i in range(1, n+1):
        graph[i][i] = 'Self'  # 자기 자신은 'Self'

    for a, b in results:
        graph[a][b] = 'Win'
        graph[b][a] = 'Lose'
    
    # 초기 탐색용 그래프
    for x in range(1, len(graph)):
        print(graph[x][1:len(graph)])

    # 플로이드-워셜 알고리즘
    for k in range(1, n+1):  # 경유 노드
        for i in range(1, n+1):  # 출발 노드
            for j in range(1, n+1):  # 도착 노드
                # i > k > j -> i 와 j 관계도 Update
                if graph[i][k] == 'Win' and graph[k][j] == 'Win':
                    graph[i][j] = 'Win'
                    graph[j][i] = 'Lose'
                elif graph[i][k] == 'Lose' and graph[k][j] == 'Lose':
                    graph[i][j] = 'Lose'
                    graph[j][i] = 'Win'

    # 3. 순위 계산
    answer = 0
    for i in range(1, n+1):
        known = 0
        for j in range(1, n+1):
            if graph[i][j] != 'Unknown' and graph[i][j] != 'Self':
                known += 1
        if known == n - 1:
            answer += 1

    return answer