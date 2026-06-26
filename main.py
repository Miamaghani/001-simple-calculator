operation= input("Choose an operation: "
"\n use '+' as sum" 
"\n use '-' as sub" \
"\n use '*' as multiply" \
"\n use '/' as divide \n")

a= int(input("Enter an number:"))
b= int(input("Enter an number:"))

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

if operation == "+":
    print(add(a,b))
elif operation == "-":
    print(subtract(a,b))
elif operation == "*":
    print(multiply(a,b))
elif operation == "/":
    print(divide(a,b))
else:
    print("Invalid choice")
