N = int(input())

for i in range(N):

    tmp = ''
    j = i + 1
    for k in range(N):
        if N - k <= j:
            tmp += '*'
        else: tmp += ' '
    print(tmp)