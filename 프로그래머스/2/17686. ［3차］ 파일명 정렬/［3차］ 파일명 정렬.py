def split_filename(filename):
    head = ''
    number = ''
    tail = ''
    
    # HEAD 추출
    for char in filename:
        if char.isdigit():
            break
        head += char
    
    # NUMBER 추출
    number_start = len(head)
    for i in range(number_start, len(filename)):
        if not filename[i].isdigit():
            break
        number += filename[i]
        if len(number) == 5:  # NUMBER는 최대 5자리
            break
    
    # TAIL 추출
    tail = filename[len(head) + len(number):]
    
    return head, number, tail

def solution(files):
    def sort_key(item):
        index, filename = item
        head, number, _ = split_filename(filename)
        return (head.lower(), int(number) if number else 0, index)
    
    # 원래 인덱스와 함께 파일명 정렬
    enumerated_files = list(enumerate(files))
    sorted_files = sorted(enumerated_files, key=sort_key)
    
    # 정렬된 파일명만 반환
    return [filename for _, filename in sorted_files]