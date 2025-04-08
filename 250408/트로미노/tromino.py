n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
answer = 0

# 기억자 3개, 일자 3개 (세로 가로 한 번에 할 수 있나?)
# 1. 기억자 3개는 2x2에서 하나씩 빼는 테스트로
for i in range(n-1):
    for j in range(m-1):
        temp_arr = [grid[i][j], grid[i+1][j], grid[i][j+1], grid[i+1][j+1]]
        temp_arr_sum = sum(temp_arr)
        for k in range(4):
            answer = max(answer, temp_arr_sum - temp_arr[k])
# 2. 세로3
for i in range(n-2):
    for j in range(m):
        temp_arr_sum = grid[i][j]+grid[i+1][j]+grid[i+2][j]
        answer = max(answer, temp_arr_sum)

# 3. 가로3
for i in range(n):
    for j in range(m-2):
        temp_arr_sum = sum(grid[i][j:j+3])
        answer = max(answer, temp_arr_sum)

print(answer)