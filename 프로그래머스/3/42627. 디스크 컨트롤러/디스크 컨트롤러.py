import heapq

def solution(jobs):
    # 한 번 시작하면 일단 그 작업 끝날 때 까지 그 작업만 수행

    # [동시 사건 처리]
    # A 작업을 마친 시점 = B 작업 요청 시작 시점
    # 그래도 B 작업을 대기 큐에 저장하는 것이 우선, 동시에 우선 순위 높은 작업이 꺼내짐
    
    # 반환 시간 = 요청 ~ 종료
    
    # 요청 시각 순서대로 큐 다시 만듬 => 이제 time_heap이 jobs 대체
    time_heap = []
    for i, (request_time, turnaround_time) in enumerate(jobs):
        # 요청 시각 빠른 순 (작업 요청 시각,  작업 소요 시간, 작업 번호)
        heapq.heappush(time_heap, (request_time, turnaround_time, i))
    # print(time_heap[0][0])
    # 대기 큐
    # 우선 순위 정렬 순: [소요 시간 짧은, 요청 시각 빠른, 작업 번호 빠른] 순
    # (turnaround_time, request_time, i)
    priority_p = []

    terminated_time = 0
    answer = 0
    
    while time_heap or priority_p:
        # print("----현재 시각:", terminated_time)
        # 매번 작업 종료시점에서 그 전에 우선순위 큐에 들어온 것이 있는지 갱신.
        while time_heap and time_heap[0][0] <= terminated_time:
            request_time, turnaround_time, i = heapq.heappop(time_heap)
            # print("종료 시간 전에 큐 정리:", i, request_time, turnaround_time)
            heapq.heappush(priority_p, ((turnaround_time, request_time, i)))
        if not priority_p and time_heap and time_heap[0][0] > terminated_time:
            request_time, turnaround_time, i = heapq.heappop(time_heap)
            # print("가장 빠른 것이 종료 시간 이후:", i, request_time, turnaround_time)
            heapq.heappush(priority_p, ((turnaround_time, request_time, i)))
            terminated_time = (request_time)
            # print("현재 시각! ", terminated_time)

        # # 대기 큐가 비어 있지 않다면, 가장 우선 순위가 높은 작업을 꺼내어, 작업
        if priority_p:
            turnaround_time, request_time, i = heapq.heappop(priority_p)

            terminated_time += turnaround_time
            answer += (terminated_time - request_time)
            # print("  ")
            # print(i,"번 째 작업", request_time, turnaround_time)
            # print(terminated_time, "-", request_time, "추가")
            # print("현재", answer)
    return answer // len(jobs)