N = int(input())

value = N // 4

tmp = ''
for i in range(value):
    tmp += 'long '

print(tmp + 'int')