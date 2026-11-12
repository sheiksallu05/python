# implement generator using any custom requirement

def student_marks():
    yield 85
    yield 90
    yield 75
    yield 95

marks = student_marks()

print(next(marks))
print(next(marks))
print(next(marks))
print(next(marks))
