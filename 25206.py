grade_dict = {
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F': 0.0,
}

result = 0 # 학점 * 과목평점
total = 0 # 학점의 총합
for _ in range(20):
    value = input().split()

    score = float(value[1])
    grade = value[2]

    if grade == 'P':
        continue
    else:
        total += score
        result += grade_dict[grade] * score

print(result / total)
