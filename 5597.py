value = [i + 1 for i in range(30)]

i = 0
while True:
    if i == 28: break

    n = int(input())
    value = list(filter(lambda i: i != n, value))

    i += 1


print(value[0])
print(value[1])
