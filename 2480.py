value = input().split()

first = int(value[0])
two = int(value[1])
three = int(value[2])

if first == two and first == three:
    print(10000 + first * 1000)
elif first == two or first == three or two == three:
    if first == two or first == three:
        print(1000 + first * 100)
    else:
        print(1000 + two * 100)
else:
    print(max(first, two, three) * 100)
