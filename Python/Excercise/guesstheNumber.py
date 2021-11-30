import random,sys
low=0
high=0
exact=0
while(True):
    
    randNum=random.randint(1,9)
    userNum=int(input("Enter a number between 1 and 9: "))
    
    print(f"The number is {randNum}.")
    if randNum==userNum:
        print("You have guessed the number correctly.")
        exact=exact+1
    elif userNum>randNum:
        print("You have guessed high.")
        high=high+1
    else:
        print("You guessed low.")
        low=low+1
    choice=input("Press any letter to continue, press n to stop: ")
    if(choice=='n'):
        print(f"You have mad:\n {exact} correct guesses.\n{low} low gusses.\n{high} high guesses.")
        sys.exit()
   
