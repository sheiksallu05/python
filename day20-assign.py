
class SalmanException(Exception):
    pass

name = input("Who are you : ")

try:

    if name == "i am salman":
        raise SalmanException("Welcome Salman!")
    else:
        print("Invalid Name")

except SalmanException as ex:
    print(ex)
