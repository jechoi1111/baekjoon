value = [1, 1, 2, 2, 2, 8]
inputValue = list(map(int, input().split()))

result = [0 for _ in range(len(value))]
for i in range(len(value)):
    result[i] = value[i] - inputValue[i]

result = list(map(str, result))
print(' '.join(result))