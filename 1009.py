testCase = int(input())

for i in range(int(testCase)):
    a, b = map(int, input().split())
    a = a % 10

    if a == 0:
        print(10)
    elif a == 1 or a == 5 or a == 6:
        print(a)
    elif a == 4 or a == 9:
        print((a ** (b % 2)) % 10)
    else:
        print((a ** (b % 4)) % 10)


# 맥북 테스트 커밋