num1= int(input("Enter a number: "))
num2= int(input(("Enter another number: ")))

def add(num1 , num2):
    return num1 + num2

sum_result= add(num1,num2)
print(f'Result: {sum_result}')

def subtract(num1, num2):
    return num1 - num2

subtract_result= subtract(num1, num2)
print(f'Result: {subtract_result}')

def multiply(num1, num2):
    return num1 * num2

multiply_result= multiply(num1, num2)
print(f'Result: {multiply_result}')

def divide(num1, num2):
    return num1/num2

divide_result= divide(num1, num2)
print(f'Result: {divide_result}')