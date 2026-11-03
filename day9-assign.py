# Sum of Digits Using No parameter & No return type

def sum_digits():
    num=1234
    total=0
    
    while num>0:
        digit=num%10
        total=total+digit
        num=num//10
    print("Sum of digits :",total)
sum_digits()
            
# Sum of Digits Using With parameter & No return type

def sum_digits(num):
    total=0
    
    while num>0:
        digit=num%10
        total=total+digit
        num=num//10
    print("Sum of digits :",total)
sum_digits(12345)

# Sum of Digits Using With parameter & With return type

def sum_digits(num):
    total=0
    
    while num>0:
        digit=num%10
        total=total+digit
        num=num//10

    return total
    
result=sum_digits(1234567)
print("Sum of digits :",result)

# Sum of Digits Using No parameter & With return type

def sum_digits():
    num=123456
    total=0
    
    while num>0:
        digit=num%10
        total=total+digit
        num=num//10

    return total
    
result=sum_digits()
print("Sum of digits :",result)
