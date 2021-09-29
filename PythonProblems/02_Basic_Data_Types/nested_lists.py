import sys
from io import StringIO

test_input = """5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39"""

test_input_2 = """5
Harsh
20
Beria
20
Varun
19
Kakunami
19
Vikas
21"""
sys.stdin = StringIO(test_input_2)

students = []

for _ in range(int(input())):
    name = input()
    score = float(input())
    students.append([name, score])


min_grade = min([x[1] for x in students])
students = [x for x in students if not x[1] == min_grade]
second_worst_score = float("inf")
for student in students:
    if student[1] <= second_worst_score:
        second_worst_score = student[1]

[print(x[0]) for x in sorted([x for x in students if x[1] == second_worst_score])]
