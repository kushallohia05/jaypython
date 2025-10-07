try:
    Age=int(input("Enter your age"))

except ValueError:
    print("write the code in numerals")

if (Age>=100):
    print("HMM are you actually that old")  

elif (Age==0):
    print("You can't be that young")    

elif (Age%2==0):
    print("Even")

else:
    print("Odd")