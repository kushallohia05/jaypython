start=int(input("enter the start of range:"))
end=int(input("enter end of range"))
squares=[x**2 for x in range(start, end+1)]

evensquares=[num for num in squares if num%2==0]
oddsquares=[num for num in squares if num%2!=0]
print("Squares:", squares)
print("Even squares:", evensquares)
print("Odd squares:", oddsquares)

         