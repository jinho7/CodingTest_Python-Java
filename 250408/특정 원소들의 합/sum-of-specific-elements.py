arr = [list(map(int, input().split())) for _ in range(4)]

n = len(arr)
answer = 0
for i in range(n):
    answer += sum(arr[i][0:i+1])

print(answer)