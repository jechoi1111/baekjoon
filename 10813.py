n, m = map(int, input().split())

tmp = []
for i in range(n):
    tmp.append(i + 1)

for _ in range(m):
    i, j = map(int, input().split())

    if i == j: continue

    old_i = tmp[i - 1]
    old_j = tmp[j - 1]

    tmp[i - 1] = old_j
    tmp[j - 1] = old_i

print(' '.join(map(str, tmp)))