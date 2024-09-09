def collatz_sequence(k):
        sequence = [k]
        while k > 1:
            if k % 2 == 0:
                k //= 2
            else:
                k = k * 3 + 1
            sequence.append(k)
        return sequence
    
def calculate_areas(sequence):
    areas = []
    for i in range(len(sequence) - 1):
        
        area = (sequence[i] + sequence[i + 1]) / 2
        areas.append(area)
    return areas

def solution(k, ranges):
    sequence = collatz_sequence(k)
    areas = calculate_areas(sequence)
    
    n = len(areas)
    results = []
    
    for a, b in ranges:
        end = n + b  
        if a > end:
            results.append(-1.0)
        else:
            result = sum(areas[a:end])
            results.append(result)
    
    return results
    
    return 