try:
    age=int(input("enter u r age"))
    print("u r age is ", age)
except ValueError as ex:
    print("Exception ", ex)