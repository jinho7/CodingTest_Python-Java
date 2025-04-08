n = int(input())

arr = [[0 for _ in range(n)] for _ in range(n)]

# [n][n]에서 시작 -> 올라가면서 시작
# code
num = 1
for i in range(n-1, -1, -1):
    # (n-i)
    if (n-i) % 2 == 0:
        for j in range(n):
            arr[j][i] += num
            num += 1
    # 홀수
    else:
        for j in range(n-1, -1, -1):
            arr[j][i] += num
            num += 1
    

# 출력
for column in arr:
    for element in column:
        print(element, end= ' ')
    print()