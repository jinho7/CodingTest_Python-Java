n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

answer = 0
# Please write your code here.
for i in range(n-3+1):
    for j in range(n-3+1):
        temp_sum = 0
        for k in range(3):
            temp_sum += sum(grid[k][j:j+3])
        answer = max(answer, temp_sum)
print(answer)