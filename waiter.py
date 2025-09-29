def cube(number):  
    print(number*number*number)
n=int(input("enter number"))
if n %3==0:
    cube(n)
else:
    print("Not divisible by three")