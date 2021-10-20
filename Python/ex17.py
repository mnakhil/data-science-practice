from sys import argv
script, file1, file2 = argv
print("Hit enter if you want to read the first file:")
input()
f1=open(file1) #opening the first file
f1read=f1.read() #reading the first file
print(f1read)
print("Hit enter if you want to copy the file:")
input()
f2 = open(file2, 'w') # opening second file
f2.write(f1read) # writing the info of first file to the second one.
print("The file has been successfully copied.")
f1.close()
f2.close()
print("End of program.")