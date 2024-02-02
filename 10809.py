s = input()

i = 97 # a
result = ''

while True:
    if i > 122: break

    for j in range(len(s)):
        if s[j] == chr(i):
            result += str(j) + ' '
            break
        else:
            if j == len(s) - 1:
                result += str(-1) + ' '

    i += 1

print(result)
