value = input()

alpha = ['c=', 'c-', 'dz=', 'd-', 'lj',  'nj', 's=', 'z=']

result = 0
while True:
    for al in alpha:
        while True:
            if al in value:
                result += 1
                value = value.replace(al, ' ', 1)
            else:
                break

    break

print(result + len(value.replace(' ', '')))