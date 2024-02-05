a, b = map(str, input().split())

reverseA = ''
for i in range(len(a)):
    reverseA += a[len(a) - i - 1]

reverseB = ''
for i in range(len(b)):
    reverseB += b[len(b) - i - 1]

print(max(int(reverseA), int(reverseB)))