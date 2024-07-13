def solution(s, n):
    # 'A' : 65, 'Z' : 90, 'a' : 97, 'z' : 122
    x = ''
    for i in s:
        if 'A' <= i <= 'Z':
            x += chr((ord(i) - ord('A') + n) % 26 + ord('A'))
        elif 'a' <= i <= 'z':
            x += chr((ord(i) - ord('a') + n ) % 26 + ord('a'))
        else:
            x += i
    return x