def solution(sequence, k):
    n = len(sequence)
    l, r = 0, 0
    s = sequence[0]
    best = [0, n-1]

    while l < n and r < n:
        if s == k:
            # 길이 비교
            if r - l < best[1] - best[0]:
                best = [l, r]
            s -= sequence[l]
            l += 1
        elif s < k:
            r += 1
            if r < n:
                s += sequence[r]
        else:  # s > k
            s -= sequence[l]
            l += 1

    return best
