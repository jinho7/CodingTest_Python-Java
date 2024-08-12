def solution(arr):
    result = [0, 0]  # [0의 개수, 1의 개수]

    def compress(x, y, n):
        if n == 1:
            result[arr[y][x]] += 1
            return arr[y][x]
        
        half = n // 2
        top_left = compress(x, y, half)
        top_right = compress(x + half, y, half)
        bottom_left = compress(x, y + half, half)
        bottom_right = compress(x + half, y + half, half)
        
        if top_left == top_right == bottom_left == bottom_right and top_left is not None:
            result[top_left] -= 3  # 중복 카운트 제거
            return top_left
        return None

    compress(0, 0, len(arr))
    return result