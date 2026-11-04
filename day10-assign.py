# 1. Implement Odd or Even Logic using Lambda Function

check = lambda num: "Even" if num % 2 == 0 else "Odd"

print(check(10))
print(check(7))

# 2. Implement Any Custom Requirement using Recursive Function

def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)

print(factorial(4))
