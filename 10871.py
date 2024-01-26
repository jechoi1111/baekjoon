n,x = map(int, input().split())

a = input().split()

tmp = []
for idx in range(n):
    if int(a[idx]) < x:
        tmp.append(a[idx])

print(' '.join(tmp))