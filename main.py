x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y  

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    return x // y  


print("Sum:", add(x, y))
print("Difference:", subtract(x, y))
print("Product:", multiply(x, y))
print("Quotient:", divide(x, y))
