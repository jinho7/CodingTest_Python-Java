n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def check_happy_array(arr, num):
    x = 1
    temp = 0
    
    for i in range(len(arr)):
        if arr[i] != temp:
            x = 1
            temp = arr[i]
        else:
            x += 1
        if x == num:
            return True
    return False

answer = 0
# Please write your code here.
for i in range(n):
    row = [grid[j][i] for j in range(n)]
    if check_happy_array(grid[i], m):
        answer += 1
    if check_happy_array(row, m):
        answer += 1
print(answer)