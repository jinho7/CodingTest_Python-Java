def solution(files):
    def split_file(file):
        head = ""
        number = ""
        tail = ""
        i = 0
        while i < len(file) and not file[i].isdigit():
            head += file[i]
            i += 1
        while i < len(file) and file[i].isdigit() and len(number) < 5:
            number += file[i]
            i += 1
        return (head, number)

    files.sort(key=lambda file: (split_file(file)[0].lower(), int(split_file(file)[1])))

    return files