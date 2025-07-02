def rotate_90(matrix):
    return [list(reversed(col)) for col in zip(*matrix)]

def is_unlock(key, lock, dx, dy):
    N, M = len(lock), len(key)
    temp = [row[:] for row in lock]  # lock 복사

    for i in range(M):
        for j in range(M):
            x, y = i + dx, j + dy
            if 0 <= x < N and 0 <= y < N:
                temp[x][y] += key[i][j]

    # 자물쇠 모든 값이 1인지 확인
    for i in range(N):
        for j in range(N):
            if temp[i][j] != 1:
                return False
    return True

def solution(key, lock):
    N, M = len(lock), len(key)

    for _ in range(4):  # 4방향 회전
        key = rotate_90(key)
        for dx in range(-M+1, N):
            for dy in range(-M+1, N):
                if is_unlock(key, lock, dx, dy):
                    return True
    return False
