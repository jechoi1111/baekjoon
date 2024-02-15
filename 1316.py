count = int(input())

result = 0
for _ in range(count):
    word = input()

    isGroup = True
    for i in range(len(word) - 1): # 맨 마지막 문자를 제외 하고 반복문을 돈다
        if word[i] != word[i + 1]: # 현재 문자와 다음 문자가 다른 경우에 그 문자가 연속하지 않은 곳에 위치한 경우 그룹 문자가 아님
            if word[i] in word[i + 1:]:
                isGroup = False
                break

    if isGroup: # 그룹 문자인 경우 count + 1
        result += 1

print(result)