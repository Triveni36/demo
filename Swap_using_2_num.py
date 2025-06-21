a=int(input("enter the first number"))
b=int(input("enter the second number "))
print("Value of a and b before swapping are {} and {}".format(a,b))
a=a+b
b=a-b
a=a-b
print("Value of a and b after swapping are {} and {}".format(a,b))
