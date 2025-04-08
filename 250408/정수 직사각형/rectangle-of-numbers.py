n, m = list(map(int, (input().split())))
x = 0
for i in range(n):
    for j in range(m):
        x += 1
        print(x, end = ' ')
    print()