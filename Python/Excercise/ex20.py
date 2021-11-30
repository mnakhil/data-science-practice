#function for reading each lines of the given file
def readline(n, f): 
    print(f"Line {n}:",f.readline())

#function used to close the file
def closefile(f):
    f.close()

#function to write to the file
def writef(f,content):
       f.writeline(content) 

#seeking the file name from the user    
print("Enter the file name:")
f1=input()

#opening the file
file=open(f1,'w')
n=0
m=1

#while loop to print the contents of the given file line by line
while(n==0):      
    print("Do you want to read the next line [y/n]?")
    ans=input()
    if(ans=="y"):
        readline(m,file) #calling the readline function
        m+=1
    elif(ans=="n"):
        n=1
    else:
        print("Invalid Input, Please try agian.")
        n=0

#writing somethin into the file
x=0
while(x==0):
    ans=input("Do you want to write something into the file [y/n]")
    if(ans=="y"):
        cont=input("Enter the contents you want to write:")
        writef(file,cont)
    elif(ans=="n"):
        x=1
    else:
        print("Invalid Input, Please try again.")

#calling the closeline function
closefile(file)
