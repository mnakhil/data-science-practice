import random
import string
char_list=list(string.ascii_letters+string.digits+"#$%&*")
shuffle_char=random.shuffle(char_list)
def creatPassword(length):
    password=[]
    for i in range(length):
       password.append(random.choice(char_list))
    password1="".join(password)
    print(f"Your password is: {password1}")
length=int(input("Enter the length of password: "))
creatPassword(length)