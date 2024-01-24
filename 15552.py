import sys

T = sys.stdin.readline().rstrip()

for i in range(int(T)):
    value = sys.stdin.readline().rstrip().split()
    A = int(value[0])
    B = int(value[1])

    print(A + B)