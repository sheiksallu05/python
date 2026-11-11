# print armstrong numbers beteen 1 to 1000

i = 1

while i <= 1000:
    temp = i
    total = 0

    while temp > 0:
        digit = temp % 10
        total = total + digit ** 3
        temp = temp // 10

    if total == i:
        print(i)

    i = i + 1

# print palindrome numbers beteen 1 to 1000

i = 1

while i <= 1000:
    temp = i
    reverse = 0

    while temp > 0:
        digit = temp % 10
        reverse = reverse * 10 + digit
        temp = temp // 10

    if reverse == i:
        print(i)

    i = i + 1
