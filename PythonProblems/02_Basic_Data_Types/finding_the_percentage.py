def get_average(grades):
    return f"{sum(grades) / len(grades):.2f}"


n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()

print(get_average(student_marks[query_name]))
