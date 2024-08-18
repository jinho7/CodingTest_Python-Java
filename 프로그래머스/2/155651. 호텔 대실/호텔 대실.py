def solution(book_time):
    events = []
    
    # HH:MM을 분 단위로 변환하는 함수
    def time_to_minutes(time):
        hours, minutes = map(int, time.split(':'))
        return hours * 60 + minutes
    
    # 각 예약에 대해 입실, 퇴실 이벤트를 추가
    for start, end in book_time:
        start_time = time_to_minutes(start)
        end_time = time_to_minutes(end)
        
        events.append((start_time, 1))  # 입실 시각에 방 하나 필요
        events.append((end_time + 10, -1))  # 퇴실+청소 후 시각에 방 하나 반환

    # 이벤트를 시간 순으로 정렬, 같은 시간일 경우 퇴실이 입실보다 우선
    events.sort(key=lambda x: (x[0], x[1]))

    max_rooms = 0
    current_rooms = 0
    
    # 이벤트를 순차적으로 처리
    for event in events:
        current_rooms += event[1]
        max_rooms = max(max_rooms, current_rooms)
    
    return max_rooms