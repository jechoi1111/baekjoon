import copy

n,m = map(int, input().split())

arr = [i + 1 for i in range(n)]

for _ in range(m):
    i, j = map(int, input().split())

    tmp = copy.deepcopy(arr)
    for k in range(i, j + 1):
        tmp[k - 1] = arr[i + j - k - 1]

    arr = copy.deepcopy(tmp)

print(' '.join(map(str, arr)))