from sys import argv
script, file_name = argv
txt = open(file_name)
print("The file contents are: ")
print(txt.read())

