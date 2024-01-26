n, m = map(int, input().split())

tmp = []
for i in range(n):
    tmp.append(0)

for _ in range(m):
    i, j, k = map(int, input().split())

    # i ~ j 번 바구니에 넣는다
    value = j - i + 1
    for num in range(value):
        idx = i + num - 1
        tmp[idx] = k

# join 하기 전에 string으로 변환하기
print(' '.join(map(str, tmp)))