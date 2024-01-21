import math

a = int(input())
b = int(input())

one = b % 10
two = math.floor(b % 100 / 10)
three = math.floor(b / 100)

oneResult_result = a * one
twoResult_result = a * two
threeResult_result = a * three

print(oneResult_result)
print(twoResult_result)
print(threeResult_result)

print(oneResult_result + twoResult_result * 10 + threeResult_result * 100)