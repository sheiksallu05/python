
def decorator(func):

    def inner(name, amount):
        print("Welcome to Shopping!")

        func(name, amount)

        print("Thank You for Shopping!")

    return inner


@decorator
def shopping_bill(name, amount):

    print("Customer Name:", name)
    print("Total Amount: Rs.", amount)


name = input("Enter Customer Name: ")
amount = int(input("Enter Total Amount: "))

shopping_bill(name, amount)


