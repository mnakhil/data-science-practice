#from sys import argv
#script, filename = argv
filename=input("Enter the filename:")
#print("If you want to continue to edit the text file press enter or press cntr+c:")
input("Hit enter?")
file=open(filename, 'w')
file.truncate()
#item1=input("line 1: ")
#item2=input("line 2: ")
file.write("This file is truncated.")
file.write("\n")
file.write("File is updated, new lines added.")