def AddTwoIntegers():
    num1 = 20
    num2 = 30
    print(num1 + num2)
AddTwoIntegers()


def AddTwoIntegers2():
    num1 = int(input("Enter the first number you want to add: "))
    num2 = int(input("Enter the Second number you want to add: "))
    print(num1 + num2)
AddTwoIntegers2()

def AddTwoIntegers3(num1, num2):
    sum = num1 + num2
    return sum
AddTwoIntegers3(20, 32)
print(f"Total sum is {sum}")