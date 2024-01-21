value = input().split()

a = int(value[0])
b = int(value[1])

if a < b:
    print('<')
elif a > b:
    print('>')
else:
    print('==')