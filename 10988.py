value = input()

i = 0
while True:
    if i == len(value) - 1:
        print(1)
        break
    if value[i] == value[len(value) - i - 1]:
        i += 1
    else:
        print(0)
        break