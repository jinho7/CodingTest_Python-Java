def solution(n):
    answer = []

    graph = []
    num = 0
    for i in range(n):
        graph.append([])
        num += (i+1)

    mode = 0
    D = 0
    R = 0
    U = 0

    cnt = n
    cnt2 = 0
    row = 0
    for i in range(num):
        if mode == 0:
            graph[row].insert(D, i+1)
            cnt2 += 1
            if cnt2 < cnt:
                row += 1
            elif cnt2 == cnt:
                cnt2 = 0
                cnt -= 1
                mode = 1
                D += 1

        elif mode == 1:
            graph[row].insert(D+cnt2, i+1)    
            cnt2 += 1
            if cnt2 == cnt:
                cnt2 = 0
                cnt -= 1
                mode = 2
                R += 1
                row -= 1

        elif mode == 2:
            graph[row].insert(len(graph[row])-U, i+1)
            cnt2 += 1
            if cnt2 < cnt:
                row -= 1
            elif cnt2 == cnt:
                cnt2 = 0
                cnt -= 1
                mode = 0
                U += 1
                row += 1

    for i in range(len(graph)):
        for j in range(len(graph[i])):
            answer.append(graph[i][j])

    return answer