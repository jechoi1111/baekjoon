value = int(input())

for i in range(9):
    print(str(value) + str(" * ") + str(i + 1) + str(" = ") + str(value * (i + 1)))