from collections import defaultdict

def solution(tickets):
    tickets.sort()  # 사전순으로 미리 정렬

    graph = defaultdict(list)
    for a, b in tickets:
        graph[a].append(b)

    path = []

    def dfs(country):
        while graph[country]:
            next_country = graph[country].pop(0)
            dfs(next_country)
        path.append(country)

    dfs("ICN")
    return path[::-1]
