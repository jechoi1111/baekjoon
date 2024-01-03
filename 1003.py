testCase = int(input())

def fibonacci(n, result):
    if n == 0:
        result[0] += 1
        return 0
    elif n == 1:
        result[1] += 1
        return 1
    else:
        return fibonacci(n - 1, result) + fibonacci(n - 2, result)


for _ in range(testCase):
    n = int(input())
    result = [0, 0]
    fibonacci(n, result)

    print(result[0], result[1])