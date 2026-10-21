# Program-1: Number Checker

num = int(input("Enter a number: "))

match num:
    case 0:
        print("Zero")
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case 4:
        print("Four")
    case _:
        print("Other number")



# Program-2: Selecting Menu

print("1. Pizza")
print("2. Burger")
print("3. Sandwich")

choice = int(input("Enter your choice: "))

match choice:
    case 1:
        print("You selected Pizza")
    case 2:
        print("You selected Burger")
    case 3:
        print("You selected Sandwich")
    case _:
        print("Invalid choice")

