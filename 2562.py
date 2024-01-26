tmp = []
for _ in range(9):
    tmp.append(int(input()))

maxValue = max(tmp)
print(maxValue)
print(tmp.index(maxValue) + 1)