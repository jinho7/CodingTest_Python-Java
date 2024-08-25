def solution(m, musicinfos):
    m = replace_sharp(m)
    candidate = []
    for music in musicinfos:
        start, end, title, code = music.split(',')
        code = replace_sharp(code)
        
        start_min = int(start.split(':')[0]) * 60 + int(start.split(':')[1])
        end_min = int(end.split(':')[0]) * 60 + int(end.split(':')[1])
        play_time = end_min - start_min
        
        # 코드 확장
        code = (code * ((play_time // len(code)) + 1))[:play_time]
        print(code)

        if m in code:
            candidate.append([title, play_time])
    candidate.sort(key=lambda x: x[1], reverse=True)
    print(candidate)
    return candidate[0][0] if candidate else "(None)"

def replace_sharp(x):
        x = x.replace('C#', 'H')
        x = x.replace('D#', 'I')
        x = x.replace('E#', 'J')
        x = x.replace('F#', 'K')
        x = x.replace('G#', 'L')
        x = x.replace('A#', 'M')
        x = x.replace("B#", "N")
        return x