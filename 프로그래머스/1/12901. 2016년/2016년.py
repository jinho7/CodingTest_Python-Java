def solution(a, b):
    month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    return days[(sum(month_days[0:a-1])+b) % 7]
