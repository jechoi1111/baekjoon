count = int(input())
result = [[0 for _ in range(100)] for _ in range(100)]

for _ in range(count):
    x, y = map(int, input().split())

    for i in range(x, x + 10):
        for j in range(y, y + 10):
            result[i][j] = 1

value = 0
for i in range(100):
    for j in range(100):
        if result[i][j] == 1: value += 1

print(value)