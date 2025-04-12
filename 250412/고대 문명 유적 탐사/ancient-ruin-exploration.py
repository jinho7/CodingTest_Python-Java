from collections import deque

k, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(5)]
m_list = list(map(int, input().split()))


# 5x5 고정
# 유물 조각 = 7가지 종류 [1 ~ 7]

# 1) 탐사 진행
 # 탐사 진행 방법 [3x3]
 # => 3x3 격자 선택 & 잡고 회전 가능. [시계 90, 180, 270 도 중 하나]
 #  => 선택할 시 "무조건" 회전 해야 한다.
 #  = 회전 목표
 #   1. 유물 1차 획득 가치 최대화
 #   2. 여러가지인 경우, 회전 각도 제일 적은
 #   3. 여러가지인 경우, 회전 중심 좌표의 열이 가장 작은 구간. -> 행이 가장 작은 구간 [주의]

# 중심 기준, 시계방향 90도 회전
def rotate_90(arr, x, y):
    new = [[0] * 3 for _ in range(3)]
    # 시작부분 부터, 3x3 회전
    for i in range(3):
        for j in range(3):
            new[j][2-i] = arr[x+i-1][y+j-1]
     # 원본 배열에 반영
    for i in range(3):
        for j in range(3):
            arr[x+i-1][y+j-1] = new[i][j]
    return arr

def check_max(arr):
    # max_num, (x, y), 반시계로 몇번 돌렸는가
    answer = [[], (0, 0), 0]
    for i in range(3, 0, -1):
        for j in range(3, 0, -1):
            for rotate_90_count in range(1, 5):
                if rotate_90_count < 4:
                    arr = rotate_90(arr, i, j)
                    #print(f'{i, j}에서 {rotate_90_count}번 회전')
                    cood_groups = find_groups(arr)
                    #print(f'터뜨릴 좌표 : {cood_groups}')
                    # 갱신
                    if len(answer[0]) < len(cood_groups):
                        coords = cood_groups
                        answer = [coords, (i, j), rotate_90_count]
                        #print("갱신")
                else:
                    arr = rotate_90(arr, i, j)
    return answer

# 2) 유물 1차 획득
# 상하좌우 탐색 & 같은 숫자인 것들끼리 묶음이 된다. + 3개 이상 묶이면 사라짐 -> 숫자 상관 X, 개수 = 가치

def dfs(x, y, value, group):
    visited[x][y] = True
    group.append((x, y))

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 5 and 0 <= ny < 5:
            if not visited[nx][ny] and arr[nx][ny] == value:
                dfs(nx, ny, value, group)


def find_groups(arr):
    global visited
    visited = [[False for _ in range(5)] for _ in range(5)]
    all_groups = []

    for i in range(5):
        for j in range(5):
            if not visited[i][j]:
                group = []
                dfs(i, j, arr[i][j], group)
                if len(group) >= 3:
                    all_groups.extend(group)

    return all_groups

# 유적 조각 정보
# 1 ~ 7 M개 적혀있음. -> 조각이 사라졌을 때 새로 생겨나는 조각에 대한 정보
# 앞에서부터 생성됨 (충분히 많음 )
# 이후 쓸 때는 다음 꺼 부터
# 열 번호가 가장 작은 순. -> 행 번호가 가장 작은 순
def pop_it(arr, coords, m_list):
    coords.sort(reverse = True, key = lambda x: (x[0]))
    coords.sort(key = lambda x: (x[1]))
    for i in range(len(coords)):
        x, y = coords[i]
        new = m_list.popleft()
        #print(f'{x,y}에 {new} 들어감')
        arr[x][y] = new
    return arr


m_list = deque(m_list)
answer = []

# 실제 회전, 터뜨리기, 유적 조각 갱신, 연쇄 획득
# ---
# 1~2 반복 = 1턴
# K번 턴 진행
# 각 턴마다 획득한 유물의 가치의 총합을 작성
# K번 진행 못했지만, 중간에 어떤 방식으로도 유물을 획득할 수 없다면 즉시 종료된다. -> 이 턴에는 아무것도 출력하지 않는다. [주의]
for _ in range(k):
    turn_answer = 0
    coords, (x, y), rotate_90_count = check_max(arr)
    if coords:
        turn_answer += len(coords)
        for _ in range(rotate_90_count):
            arr = rotate_90(arr, x, y)
        arr = pop_it(arr, coords, m_list)

        # 3) 유물 연쇄 획득
        # 새로운 유물이 생성된 후에도 또 체크했을 때 3개 이상 연결될 수 있다.
        # 그럼 연쇄적으로 또 1~2가 반복된다.
        while True:
            cood_groups = find_groups(arr)
            turn_answer += len(cood_groups)
            if not cood_groups:
                break
            arr = pop_it(arr, cood_groups, m_list)
        answer.append(turn_answer)
for i in range(len(answer)):
    print(answer[i], end = ' ')