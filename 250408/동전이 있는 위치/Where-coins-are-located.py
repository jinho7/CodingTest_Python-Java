n, m = map(int, input().split())

coins = [tuple(map(int, input().split())) for _ in range(m)]

arr = [[0 for _ in range(n)] for _ in range(n)]

for coin in coins:
    x, y = coin
    arr[x-1][y-1] = 1

for i in range(n):
    for j in range(n):
        print(arr[i][j], end= ' ')
    print()