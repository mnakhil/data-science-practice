
def fibonacci(num1):
    first=0
    second=1
    fib=[first,second]
    
    for i in range(num1):
        third=first+second
        fib.append(third)
        first=second
        second=third
    return fib

num1=int(input("Enter the number:"))
print(fibonacci(num1))