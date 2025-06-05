from collections import defaultdict

def solution(tickets):
    tickets.sort(key=lambda x: x[1])
    
    graph = defaultdict(list)
    for a, b in tickets:
        graph[a].append(b)
    
    print(graph)
    def dfs(country):
        while graph[country]:
            print(graph[country])
            next_country = graph[country].pop(0)
            dfs(next_country)
        path.append(country)
        print(path)
    path = []
    dfs('ICN') 
    return path[::-1]