import math

testCase = int(input())

for i in range(testCase):
    value = input().split()
    x1 = int(value[0])
    x2 = int(value[1])
    y1 = int(value[3])
    y2 = int(value[4])
    r1 = int(value[2])
    r2 = int(value[5])

    length = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    print(length, r1 + r2)
    if length < r1 + r2:
        print(2)
    elif length == r1 + r2:
        print(1)
    else:
        print(0)
