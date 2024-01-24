T = int(input())

for i in range(T):
    value = input().split()
    A = int(value[0])
    B = int(value[1])

    print('Case #'+str(i + 1)+': '+str(A + B))