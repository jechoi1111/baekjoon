t = int(input())

for _ in range(t):
    value = input().split()
    r = int(value[0])
    s = value[1]

    result = ''
    for i in range(len(s)):
        for _ in range(r):
            result += s[i]

    print(result)