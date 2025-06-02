def solution(sequence):
    answer = 0
    x_1 = sequence[:]
    x_2 = sequence[:]
    for i in range(0, len(x_1) ,2):
        x_1[i] *= -1
    for i in range(1, len(x_2) ,2):
        x_2[i] *= -1
    
    def max_arr(arr):
        current = max_sum = arr[0]
        for i in range(1, len(arr)):
            current = max(arr[i], current + arr[i])
            max_sum = max(max_sum, current)
        return max_sum
    
    return max(max_arr(x_1), max_arr(x_2))

# (그 부분 수열을 퍼스 수열로 곱하고 나머지) 전체 합 가장 큰 경우 구함... [부분 수열이 아닌]
# def solution(sequence):
    
#     # 부분 수열이 공 집합인 수열
#     answer = sum(sequence)
    
#     # 홀수
#     odd_seq = [ sequence[i] for i in range(0, len(sequence), 2)]
#     odd_seq_sum = sum(odd_seq)
#     # 짝수
#     even_seq = [ sequence[i] for i in range(1, len(sequence), 2)]
#     even_seq_sum = sum(even_seq)
    
#     # 1로 시작하는 경우
#     # 홀수 idx에 -1을 곱함 / 짝수 idx는 무조건 그대로
#     minus_odd_arrays = []
#     # 홀수 subarrays & -1 처리   
#     for s in range(len(odd_seq)):
#         for e in range(s + 1, len(odd_seq) + 1):
#             minus_odd_sub_arrays = [ -i for i in odd_seq[s:e]]
#             minus_odd_arrays.append(odd_seq[:s] + minus_odd_sub_arrays + odd_seq[e:])

#     # 홀수 합 & max 갱신
#     for minus_odd_array in minus_odd_arrays:
#         print(minus_odd_array)
#         print(even_seq_sum + sum(minus_odd_array))
#         answer = max(answer, even_seq_sum + sum(minus_odd_array))
    
#     # -1로 시작하는 경우
#     # 짝수 idx에 -1을 곱함 / 홀수 idx는 무조건 그대로
#     minus_even_arrays = []
#     # 짝수 subarrays & -1 처리
#     for s in range(len(even_seq)):
#         for e in range(s + 1, len(even_seq) + 1):
#             minus_even_sub_arrays = [ -i for i in even_seq[s:e]]
#             minus_even_arrays.append(even_seq[:s] + minus_even_sub_arrays + even_seq[e:])
    
#     print("---")
#     # 짝수 합 & max 갱신
#     for minus_odd_array in minus_odd_arrays:
#         print(minus_odd_array)
#         print(odd_seq_sum + sum(minus_odd_array))
#         answer = max(answer, odd_seq_sum + sum(minus_odd_array))
        
#     return answer