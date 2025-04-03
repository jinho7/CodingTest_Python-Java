from itertools import permutations
import math

n = input()
num_list = list(map(int, input().split()))


# 연산자 우선 순위를 무시하고 앞에서부터 진행
# 또, 나눗셈은 정수 나눗셈으로 몫만 취한다.
# 음수를 양수로 나눌 때는 양수로 바꾼 뒤 몫을 취하고, 그 몫을 음수로 바꾼 것과 같다. 
def calculate(i, j, x):
    if x == '+':
        return i + j
    if x == '-':
        return i - j
    if x == '*':
        return i * j
    if x == '//':
        if i < 0 :
            return - ( -i // j)
        else:
            return i // j

x = list(map(int, input().split()))

z = ['+', '-', '*', '//']
stack = []
answer_list = []
for i in range(4) :
    for _ in range(x[i]):
        stack.append(z[i])

for x in set(permutations(stack, len(stack))):
    result = num_list[0]
    for i in range(len(num_list)-1):
        result = calculate(result, num_list[i+1], x[i])
    answer_list.append(result)

print(max(answer_list))
print(min(answer_list))