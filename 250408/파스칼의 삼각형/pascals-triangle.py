n = int(input())
arr = [[1 for _ in range(i+1)] for i in range(n)]

for i in range(1, n):
    for j in range(1, i):
        arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

# 출력
for column in arr:
    for element in column:
        print(element, end= ' ')
    print()