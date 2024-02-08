n = int(input())

for i in range(n):
    result = ''
    space = 0 # 빈칸 개수
    star = 0 # 별 개수

    while True:
        if space == (n - i - 1):
            space = 0
            for _ in range(2 * (i + 1) - 1):
                result += '*'

            break
        else:
            result += ' '
            space += 1

    print(result)

for i in range(n - 1):
    result = ''
    space = 0
    star = 0

    while True:
        if space == (i + 1):
            space = 0
            for _ in range(2 * (n - i - 1) - 1):
                result += '*'
            break
        else:
            result += ' '
            space += 1

    print(result)
