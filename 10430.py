value = input().split()

A = int(value[0])
B = int(value[1])
C = int(value[2])

print((A + B) % C)
print(((A % C) + (B % C)) % C)
print((A * B) % C)
print((A % C) * (B % C) % C)