from collections import deque

def solution(n, t, m, timetable):
    # 시간 변환 함수
    def t_to_m(x):
        h, m = map(int, x.split(":"))
        return 60 * h + m

    def m_to_t(m):
        h = (str)(m // 60).zfill(2)
        m = (str)(m % 60).zfill(2)
        return f"{h}:{m}"
    
    # timetable 정렬
    for i in range(len(timetable)):
        timetable[i] = t_to_m(timetable[i])
    timetable.sort()
    # print("직원 줄 서는 시간:", timetable)
        
    bus_stop = []
    bus_line = deque(timetable)
    
    # 버스 서는 시간
    for i in range(n):
        bus_stop.append(t_to_m("09:00") + (t * i))
    # print("버스 정류장 시간표:", bus_stop)
    
    # print("**********시작***********")
    last_boarded = -1  # 마지막에 탄 사람의 시간
    for stop_time in bus_stop:
        count = 0
        while bus_line and count < m and bus_line[0] <= stop_time:
            last_boarded = bus_line.popleft()
            count += 1
        # print("[log]", stop_time, "버스 도착 - 탑승 수:", count)

    # 마지막 버스
    last_bus_time = bus_stop[-1]
    if count < m:
        return m_to_t(last_bus_time)
    else:
        return m_to_t(last_boarded - 1)