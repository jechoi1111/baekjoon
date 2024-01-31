m = int(input())
result = list(map(int, input().split()))

max = max(result) # 최대값

newResult = 0
for i in result:
    newResult += (i / max * 100)

print(newResult / m)


