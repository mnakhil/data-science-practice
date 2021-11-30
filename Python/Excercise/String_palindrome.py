import sys
str=input("Enter the string: ")
limit=int((len(str))/2)
print(str[0])
for i in range(limit):
    if(str[i]!=str[-(i+1)]):
        print("Given string is not a palindrome.")
        sys.exit()
print("Given string is a palindrom")