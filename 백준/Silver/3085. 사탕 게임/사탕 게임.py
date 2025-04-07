N = int(input())

arr = [list(input()) for _ in range(N)]

def check_max(arr):
    max_len = 1
    for i in range(N):
        cnt = 1
        for j in range(1, N):
            if arr[i][j] == arr[i][j-1]:
                cnt += 1
            else:
                cnt = 1
            max_len = max(max_len, cnt)

    for j in range(N):
        cnt = 1
        for i in range(1, N):
            if arr[i][j] == arr[i-1][j]:
                cnt += 1
            else:
                cnt = 1
            max_len = max(max_len, cnt)
    return max_len

def swap_check(arr):
    max_len = 1
    for i in range(N):
        for j in range(N):
            # 같지 않을 때만 스왑
            # 오른쪽과 교환
            if j + 1 < N and arr[i][j] != arr[i][j+1]:
                #print('arr', i, j, '&', 'arr', i, j+1,'인덱스 교환')
                #print(arr[i][j], '&', arr[i][j+1], '스왑')
                arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
                # 체크하고 복원
                max_len = max(max_len, check_max(arr))
                #print('max_len: ', max_len)
                arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
            # 아래와 교환
            if i + 1 < N and arr[i][j] != arr[i+1][j]:
                #print('arr', i, j, '&', 'arr', i+1, j,'인덱스 교환')
                #print(arr[i][j], '&', arr[i+1][j], '스왑')
                arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
                #print(arr)
                # 체크하고 복원
                max_len = max(max_len, check_max(arr))
                #print('max_len: ', max_len)
                arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]

    return max_len
    
x = check_max(arr)

if x == N:
    #print('스왑 없이 바로 N')
    print(x)

else:
    print(swap_check(arr))