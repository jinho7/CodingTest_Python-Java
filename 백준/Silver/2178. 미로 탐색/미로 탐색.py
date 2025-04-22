import heapq

n, m = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(n)]


def dijkstra(arr):
    # (0,0) 에서 (n-1, m-1)까지
    heap = [(1, (0, 0))]
    distances = [[float('inf') for _ in range(m)] for _ in range(n)]
    distances[0][0] = 1
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    while heap:
        cur_dist, cur_xy = heapq.heappop(heap)
        x, y = cur_xy

        for dx, dy in directions:
            dist, nx, ny = cur_dist + 1, x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] != 0:
                if dist < distances[nx][ny]:
                    distances[nx][ny] = dist
                    heapq.heappush(heap, (dist, (nx, ny)))
    
    return distances[n-1][m-1]

print(dijkstra(arr))