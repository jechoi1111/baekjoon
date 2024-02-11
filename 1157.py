value = input().upper() # 입력어 대문자화
setValue = list(set(list(value))) # 겹치는 단어 제거

result = [0 for _ in range(len(setValue))]
for i in range(len(setValue)):
    for j in range(len(value)):
        if setValue[i] == value[j]:
            result[i] += 1

maxResult = max(result)
num = 0
for i in range(len(result)):
    if result[i] == maxResult:
        num += 1
    if num > 1:
        print('?')
        break

if num == 1:
    print(setValue[result.index(maxResult)])