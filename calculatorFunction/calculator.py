def plus(a, b):
    return a + b
def minus(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b
number1 = int(input("Enter the first number: "))
operation = input("Enter '+' , '-' , '*' , '/' ")
number2 = int(input("Enter the second number: "))
match operation:
    case '+': print(plus(number1, number2))
    case '-': print(minus(number1, number2))
    case '*': print(multiply(number1, number2))
    case '/': print(divide(number1, number2))

