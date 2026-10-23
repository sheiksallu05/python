# Program 1
num = int(  input("Enter a number : ") )
s = 0 
temp = num
while num > 0:  
    r = num % 10 
    s = s+r
    if(num > 9):
        s = s*10
    num=num // 10
if(temp == s):
    print(s," is Palindrome")
else:
    print(s," not a Palindrome")


# Program 2

num = int(input("Enter a number : "))
s = 0
temp = num
while num > 0:
    r = num % 10
    s = s * 10 + r
    num = num // 10
if s == temp:
    print(s,"is Palindrome")
else:
    print(s," not a Palindrome")
