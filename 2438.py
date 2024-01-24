N = int(input())

i = 0
while i < N:
    i += 1

    tmp = ''
    for j in range(i):
        tmp += '*'
    print(str(tmp))
