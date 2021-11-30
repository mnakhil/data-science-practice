import sys
while(True):
    print("Please chose your option among the following:\n1.Rock\n2.Paper\n3.Scissor\nPlease enter the number:")
    player1=int(input("First Palyer:"))
    player2=int(input("Second Player:"))
    if(player1==1 and player2==2):
        print("Player 2 wins.")
    elif(player1==2 and player2==1):
        print("Player 1 wins.")
    elif(player1==2 and player2==3):
        print("Player 2 wins.")
    elif(player1==3 and player2==2):
        print("Player 1 wins.")
    elif(player1==1 and player2==3):
        print("Player 1 wins.")
    elif(player1==3 and player2==1):
        print("Player 2 wins.")
    else:
        print("It's a draw.")
    ch=input("Do you want play again[y/n]")
    if(ch=='n'):
        sys.exit()