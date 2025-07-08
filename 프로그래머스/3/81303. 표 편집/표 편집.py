def solution(n, k, cmd):
    
    prev_p = [i-1 for i in range(n)]  # i번째 행의 이전 행 번호
    next_p = [i+1 for i in range(n)] # i번째 행의 이전 행 번호
    next_p[-1] = -1 # 마지막 행 처리
    deleted = [] # 삭제된 행의 정보 (복구용)
    cur = k
    
    for command in cmd:
        # 이동
        if len(command.split()) == 2:
            c, x = command.split()
            x = int(x)
            if c == 'U':
                # print(x, "만큼 위로 이동")
                for _ in range(x):
                    cur = prev_p[cur]
                # print("현재 cur:", cur)
            else:
                # print(x, "만큼 아래로 이동")
                for _ in range(x):
                    cur = next_p[cur]
                # print("현재 cur:", cur)
    # 삭제 혹은 복구    
        else:
            if command == "C":
                # print("삭제")
                deleted.append((cur, prev_p[cur], next_p[cur]))
                if prev_p[cur] != -1:
                    next_p[prev_p[cur]] = next_p[cur]
                if next_p[cur] != -1:
                    prev_p[next_p[cur]] = prev_p[cur]

                # 아래 행으로 커서 이동 (없으면 위로)
                if next_p[cur] != -1:
                    cur = next_p[cur]
                else:
                    cur = prev_p[cur]
            else:
                # print("복구")
                i, p_, n_ = deleted.pop()
                if p_ != -1:
                    next_p[p_] = i
                if n_ != -1:
                    prev_p[n_] = i
    answer = ['O' for _ in range(n)]
    for x, _, _ in deleted:
        answer[x] = 'X'
    return ''.join(answer)