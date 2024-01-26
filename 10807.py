N = int(input())

value = input().split()

v = int(input())

i = 0
for idx in range(N):
    if int(value[idx]) == v:
        i += 1

print(i)
