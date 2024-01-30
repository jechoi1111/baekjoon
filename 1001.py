value = input().split()

result = int(value[0])
for index, i in enumerate(value):
    if index != 0:
        result -= int(i)

print(result)