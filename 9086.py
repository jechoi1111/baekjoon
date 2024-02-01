t = int(input())

for _ in range(t):
    value = input()
    length = len(value)
    print(value[0] + value[length - 1])