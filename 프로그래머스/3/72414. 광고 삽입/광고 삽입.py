def solution(play_time, adv_time, logs):
    # 문자열 → 초 단위 변환
    def time_to_seconds(time):
        hh, mm, ss = map(int, time.split(":"))
        return hh * 3600 + mm * 60 + ss

    # 초 → "HH:MM:SS" 변환
    def seconds_to_time(seconds):
        hh = seconds // 3600
        mm = (seconds % 3600) // 60
        ss = seconds % 60
        return f"{hh:02}:{mm:02}:{ss:02}"

    play_time = time_to_seconds(play_time)
    adv_time = time_to_seconds(adv_time)
    total_time = [0] * (play_time + 2)  # +2는 index overflow 방지용

    # 1️⃣ 각 로그별 입장/퇴장 표시 (+1 / -1)
    for log in logs:
        start, end = log.split("-")
        start, end = time_to_seconds(start), time_to_seconds(end)
        total_time[start] += 1
        total_time[end] -= 1

    # 2️⃣ 현재 시점 시청자 수 계산 (prefix sum 1)
    for i in range(1, play_time + 1):
        total_time[i] += total_time[i - 1]

    # 3️⃣ 누적 시청 시간 계산 (prefix sum 2)
    for i in range(1, play_time + 1):
        total_time[i] += total_time[i - 1]

    # 4️⃣ 광고 구간별 누적 시청 시간 계산 (슬라이딩 윈도우)
    max_view = total_time[adv_time - 1]
    best_start = 0
    for end in range(adv_time, play_time):
        # [end - adv_time + 1, end] 구간의 총 시청 시간
        view = total_time[end] - total_time[end - adv_time]
        if view > max_view:
            max_view = view
            best_start = end - adv_time + 1

    return seconds_to_time(best_start)
