num=int(input("Enter a number:"))
check=int(input("Enter the number for check:"))
if(num%check==0):
    print(f"{num} is divisible by {check}")
else:
    print(f"{num} is not divisible by {check}")