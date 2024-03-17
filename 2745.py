num_list = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

n, b = input().split(' ') # b: 진법

answer = 0
for i, num in enumerate(n[::-1]):
    answer += int(b) ** i * num_list.find(num)


print(answer)