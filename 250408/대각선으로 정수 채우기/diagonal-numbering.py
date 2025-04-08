n, m = map(int, input().split())

# Please write your code here.
arr_2d = [ [0 for _ in range(m)] for _ in range(n) ]
# 00 / 01 10 / 02 11 20 / 03 12 21 30 ... / 52 43 / 53

# 0 ~ 8
num = 1

for nm in range(n+m):
    for i in range(nm, -1, -1):
        if 0 <= nm-i < n and 0 <= i < m:
            arr_2d[nm-i][i] = num
            num += 1

for column in arr_2d:
    for element in column:
        print(element, end= ' ')
    print()