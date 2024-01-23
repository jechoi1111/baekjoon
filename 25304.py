X = int(input())
N = int(input())

result = 0
for i in range(N):
    value = input().split()
    a = int(value[0])
    b = int(value[1])
    result += a * b

if X == result: print('Yes')
else: print('No')