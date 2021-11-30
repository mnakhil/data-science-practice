import sys
def checkPrime(num):
    
    for i in range(2,int(num/2)):
        if num%i==0:
            print(f"{num} is not a prime num.")
            sys.exit()
    print(f"{num} is a prime number")

num=int(input("Enter a number:"))
checkPrime(num)