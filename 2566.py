result = [[0 for _ in range(9)] for _ in range(9)]

for i in range(9):
    inputInt = list(map(int, input().split()))
    for j in range(9):
        result[i][j] = inputInt[j]


max = -1 # 자연수는 0 부터 시작
col = 0
row = 0
for i in range(9):
    for j in range(9):
       if max < result[i][j]:
           max = result[i][j]
           row = i + 1
           col = j + 1

print(max)
print(str(row) + ' ' + str(col))