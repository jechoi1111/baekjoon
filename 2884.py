value = input().split()
h = int(value[0])
m = int(value[1])

if m - 45 > 0:
    print(str(h) + ' ' + str(m - 45))
elif m - 45 < 0:
    if h - 1 == -1:
        print(str(23) + ' ' + str(m + 15))
    else:
        print(str(h - 1) + ' ' + str(m + 15))
else:
    if h == 0:
        print(str(0) + ' ' + str(0))
    else:
        print(str(h) + ' ' + str(0))