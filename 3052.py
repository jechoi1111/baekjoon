tmp = []
for i in range(10):
    n = int(input())
    left = n % 42
    if left not in tmp:
        tmp.append(left)

print(len(tmp))