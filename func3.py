def add(a,b):
    return a+b
def subtract(a, b):  
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b


print ("please select the operation")
print("1. add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice=int(input("Please enter choice (1/2/3/4):"))
NUM1=int(input("Please enter the first number:"))
NUM2=int(input("Please enter the second number"))

if choice==1:
    print(add (NUM1, NUM2))
elif choice==2:
    print(subtract(NUM1, NUM2))    
elif choice==3: 
    print(multiply(NUM1, NUM2))  
elif choice==4:   
    print(divide(NUM1, NUM2))
else:   
    print("This is an invalid output")    




