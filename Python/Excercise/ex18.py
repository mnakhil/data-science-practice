def add(*args):
    arg1,arg2 = args
    sum=arg1+arg2
    print(f"Sum of {arg1} and {arg2} is {sum}")
#`print("akhil","akhi")
print("Assign values directly:")
add(12,24)
print("Assign values for variable and using variable:")
n1=10
n2=11
add(n1,n2)
print("Taking input from the user:")
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
add(num1,num2)
