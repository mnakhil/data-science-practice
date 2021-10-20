import random
class game:
    def __init__(self) :
        self.cscore=0
        self.yscore=0
    def game1(self,comp,you):
        if(comp=="s" and you=="w"):
            self.yscore=self.yscore+1
            print(f"You won. You got one point")
           
        elif(comp=="w" and you=="s"):
            self.cscore=self.cscore+1
            print(f"Computer won. Computer got one point")
        elif(comp=="w" and you=="g"):
            self.cscore=self.cscore+1
            print(f"Computer won. Computer got one point") 
        elif(comp=="g" and you=="w"):
            self.yscore=self.yscore+1
            print(f"You won. You got one point")
        elif(comp=="g" and you=="s"):
            self.cscore=self.cscore+1
            print(f"Computer won. Computer got one point") 
        elif(comp=="s" and you=="g"):
            self.yscore=self.yscore+1
            print(f"You won. You got one point")
        else:
            print("Turns out nobody is lucky, please try again.")
            
    def print_scores(self):
        
        print(f"You have secured {self.yscore}.")
        print(f"The computer has scored {self.cscore}.")
        if self.yscore>self.cscore:
            print("Congragtulations! You have one the game.")
        elif self.yscore==self.cscore:
            print("Well both did good.The game is a tie!")
        else:
            print("The computer has won the game, better luck next time")
ob=game()
flag=0
gamedic ={"w":"water","s":"snake","g":"gun"}
while flag==0:
    print("Computers turn. Let the computer pick one:")
    print("1.Snake(s) 2.Water(w) 3.Gun(g):")
    cchoice=random.randint(1,3)
    if cchoice==1:
        comp="s"
    elif cchoice==2:
        comp="w"
    else:
        comp="g"
    print("Your turn. Please pick one:")
    print("1.Snake(s) 2.Water(w) 3.Gun(g):")
    you=input()
    print(f"Computer chose {gamedic[comp]}")
    print(f"You chose {gamedic[you]}")
    ob.game1(comp,you)
    ch=input("Do you want to continue the game[y/n]")
    if ch=="y":
        flag==0
    elif ch=="n":
        ob.print_scores()
        flag=1
   # else:
    #    print("Wrong choice, guess you want to go back to the game.")

