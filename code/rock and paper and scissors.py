import random
from tkinter import X
# list contents rock and paper and scissors:
words =["s","p","r"]
# loop of all game:
while True:  
    # two counter of game: 
    counntwon=0
    counntlose=0
    
    # Sentence of Hello Every One:
    for i in range(0,4):
        if i==0:
            print("*"*50)
        elif i==1:
            print("<<<<<<<<<<<<<<<<< Hello Every One >>>>>>>>>>>>>>>>".center(50," "))
        elif i==2:
            print("<<<<<<<<<<<<< By Eng :: Mohamed Elsayed >>>>>>>>>>".center(50," ")) 
        else:
            print("*"*50)

    # Sentence of The Game Start: 
    for i in range(0,3):
        if i==0:
            print("*"*50)
        elif i==1:
            print("<<<<<<<<<<<<<<<<< The Game Start >>>>>>>>>>>>>>>>>".center(50," "))
        else:
            print("*"*50)

   # single or multiple:   
    print("Do you play single or two player ??",end="")
    a=input("".strip().capitalize())

    # signle player:  
    if a == "single player":
        # loop of the game:
        while True:
            # Enter your Answer:
            print ("what's your choice ? 'r' for rock , 'p' for paper , 's' for scissors ")
            answer=input("the choose is :".strip().capitalize())
            word = random.choice(words)
            
            # Check Answer:
            if answer == word:
                print(f"\nIt is a tie. You and the computer have both chosen ({word}).\n")
                counntwon+=1
                counntlose+=1
            elif answer == "r" and word == "s":
                print(f"\nYou have chosen ({answer}) and the computer has chosen ({word}). \"<You won!>\"\n")
                counntwon+=1
            elif answer == "p" and word == "r":
                print(f"\nYou have chosen ({answer}) and the computer has chosen ({word}). \"<You won!>\"\n")
                counntwon+=1
            elif answer == "s" and word == "p":
                print(f"\nYou have chosen ({answer}) and the computer has chosen ({word}). \"<You won!>\"\n")
                counntwon+=1     
            elif answer == "p" and word == "s":
                print(f"\nYou have chosen ({answer}) and the computer has chosen ({word}). \"<You lost!>\"\n")
                counntlose+=1
            elif answer == "r" and word == "p":
                print(f"\nYou have chosen ({answer}) and the computer has chosen ({word}). \"<You lost!>\"\n")
                counntlose+=1
            elif answer == "s" and word == "r":
                print(f"\nYou have chosen ({answer}) and the computer has chosen ({word}). \"<You lost!>\"\n")
                counntlose+=1     
        
        # check if you and computer are Equal in count:
            if (counntwon == 9 and counntlose == 9) or (counntwon == 8 and counntlose == 8) or (counntwon == 7 and counntlose == 7) or (counntwon == 6 and counntlose == 6) or (counntwon == 3 and counntlose == 3) or (counntwon == 2 and counntlose == 2) or (counntwon == 1 and counntlose == 1) or (counntwon == 4 and counntlose == 4) or (counntwon == 5 and counntlose == 5):
                continue
           # the counter is full: 
            elif (counntwon == 10 and counntlose == 10):
                  print("you are equal in counter its luckly . your score is 10")
                  break
            
            # Check if You Win:
            elif (counntwon == 10 and counntlose == 9) or (counntwon == 9 and counntlose == 8) or (counntwon == 8 and counntlose == 7) or (counntwon == 7 and counntlose == 6) or (counntwon == 6 and counntlose == 5) or (counntwon == 5 and counntlose == 4) or (counntwon == 3 and counntlose == 2) or (counntwon == 4 and counntlose == 3) or (counntwon == 3 and counntlose == 1) or (counntwon ==3 and counntlose == 0):
                for i in range(0,3):
                    if i==0: 
                        print("-"*50)
                    elif i==1:
                        print("|",end="")
                        print("Congratulation You Win".center(48," "),end="")
                        print("|")
                    else:
                        print("-"*50)                                   
                break   
            
            # Check if you Lost: 
            elif (counntwon == 4 and counntlose == 5) or (counntwon == 5 and counntlose == 6) or (counntwon == 6 and counntlose == 7) or (counntwon == 7 and counntlose == 8) or (counntwon == 8 and counntlose == 9) or (counntwon == 9 and counntlose == 10)or (counntwon == 2 and counntlose == 3) or (counntwon == 3 and counntlose == 4) or (counntwon == 1 and counntlose == 3) or (counntwon == 0 and counntlose == 3):
                for i in range(0,3):
                    if i==0:
                        print("-"*50) 
                    elif i==1:
                        print("|",end="")
                        print("You Lost. Game Over".center(48," "),end="")
                        print("|")
                    else:
                            print("-"*50)                              
                break            
        
        # Sentence of The Game End:
        for i in range(0,4):
            if i==0:
                print("\n")
                print("*"*50)
            elif i==1:
                print("<<<<<<<<<<<<<<<<<< The Game END >>>>>>>>>>>>>>>>>>".center(50," "))
            elif i==2:
                print("<<<<<<<<<<<< By Eng :: Mohamed Elsayed >>>>>>>>>>>".center(50," "))
            else:
                print("*"*50)
                print("\n")
   
   # two player (mulitple):
    elif a == "two player":
        # loop of the game:
        while True:
            # Enter your Answer:
            print ("what's your choice ? 'r' for rock , 'p' for paper , 's' for scissors ")
            answer1=random.choice(words)
            answer2=random.choice(words)
            print(f"player 1 :{answer1}")
            print(f"player 2 :{answer2}")


            
            # Check Answer:
            if answer1 == answer2:
                print(f"\nIt is a tie. Player 1  and Player 2 have both chosen ({answer1}).\n")
                counntwon+=1
                counntlose+=1
            elif answer1 == "r" and answer2 == "s":
                print(f"\nPlayer 1 has chosen ({answer1}) and Player 2 has chosen ({answer2}). \"<Player 1 has win!>\"\n")
                counntwon+=1
            elif answer1 == "p" and answer2 == "r":
                print(f"\nPlayer 1 has chosen ({answer1}) and Player 2 has chosen ({answer2}). \"<Player 1 has won!>\"\n")
                counntwon+=1
            elif answer1 == "s" and answer2 == "p":
                print(f"\nPlayer 1 has chosen ({answer1}) and Player 2 has chosen ({answer2}). \"<Player 1 has  won!>\"\n")
                counntwon+=1     
            elif answer1 == "p" and answer2 == "s":
                print(f"\nPlayer 1 has chosen ({answer1}) and Player 2 has chosen ({answer2}). \"<Player 2 has  win!>\"\n")
                counntlose+=1
            elif answer1 == "r" and answer2 == "p":
                print(f"\nPlayer 1 has chosen ({answer1}) and Player 2 has chosen ({answer2}). \"<Player 2 has  win!>\"\n")
                counntlose+=1
            elif answer1 == "s" and answer2 == "r":
                print(f"\nPlayer 1 has chosen ({answer1}) and Player 2 has chosen ({answer2}). \"<Player 2 has  win!>\"\n")
                counntlose+=1     
        
        # check if Player 1 and Player 2 are Equal in count:
            if (counntwon == 9 and counntlose == 9) or (counntwon == 8 and counntlose == 8) or (counntwon == 7 and counntlose == 7) or (counntwon == 6 and counntlose == 6) or (counntwon == 3 and counntlose == 3) or (counntwon == 2 and counntlose == 2) or (counntwon == 1 and counntlose == 1) or (counntwon == 4 and counntlose == 4) or (counntwon == 5 and counntlose == 5):
                continue
           # the counter is full: 
            elif (counntwon == 10 and counntlose == 10):
                  print("you are equal in counter its luckly . your score is 10")
                  break

            # Check if Player 1  Win:
            elif (counntwon == 10 and counntlose == 9) or (counntwon == 9 and counntlose == 8) or (counntwon == 8 and counntlose == 7) or (counntwon == 7 and counntlose == 6) or (counntwon == 6 and counntlose == 5) or (counntwon == 5 and counntlose == 4) or (counntwon == 3 and counntlose == 2) or (counntwon == 4 and counntlose == 3) or (counntwon == 3 and counntlose == 1) or (counntwon ==3 and counntlose == 0):
                for i in range(0,3):
                    if i==0: 
                        print("-"*50)
                    elif i==1:
                        print("|",end="")
                        print("Congratulation Player 1".center(48," "),end="")
                        print("|")
                    else:
                        print("-"*50)                                   
                break   
            
            # Check if Player 2 win: 
            elif (counntwon == 4 and counntlose == 5) or (counntwon == 5 and counntlose == 6) or (counntwon == 6 and counntlose == 7) or (counntwon == 7 and counntlose == 8) or (counntwon == 8 and counntlose == 9) or (counntwon == 9 and counntlose == 10)or (counntwon == 2 and counntlose == 3) or (counntwon == 3 and counntlose == 4) or (counntwon == 1 and counntlose == 3) or (counntwon == 0 and counntlose == 3):
                for i in range(0,3):
                    if i==0:
                        print("-"*50) 
                    elif i==1:
                        print("|",end="")
                        print("Congratulation Player 2".center(48," "),end="")
                        print("|")
                    else:
                            print("-"*50)                              
                break            
        
        # Sentence of The Game End:
        for i in range(0,4):
            if i==0:
                print("\n")
                print("*"*50)
            elif i==1:
                print("<<<<<<<<<<<<<<<<<< The Game END >>>>>>>>>>>>>>>>>>".center(50," "))
            elif i==2:
                print("<<<<<<<<<<<< By Eng :: Mohamed Elsayed >>>>>>>>>>>".center(50," "))
            else:
                print("*"*50)
                print("\n")

    # Do you play again: 

    print("         Do you Want to  play again (yes or no) !! : ",end="")
    ans1=input("".strip().capitalize())
    
    if ans1 == "yes" or ans1 =="y":
        print("\n")
        continue
    elif ans1 == "no" or ans1 =="n":
        print("\n")
        print("the program has end !!".center(70," "))
        print("\n")
        break;  


