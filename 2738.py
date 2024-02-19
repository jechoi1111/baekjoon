n, m = map(int, input().split())

a = [[0 for i in range(m)] for j in range(n)]
b = [[0 for i in range(m)] for j in range(n)]

for i in range(n):
    value = list(map(int, input().split()))
    for j in range(m):
        a[i][j] = value[j]


for i in range(n):
    value = list(map(int, input().split()))
    for j in range(m):
        b[i][j] = value[j]

for i in range(n):
    result = [0 for _ in range(m)]
    for j in range(m):
        result[j] += a[i][j] + b[i][j]

    print(' '.join(list(map(str, result))))