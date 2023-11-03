# importing random module
import random
choice_list = ['rock','paper','scissor']
com_win = 0
user_win = 0
choice = True

while(choice):

    com_choice = random.choice(choice_list)
    user_choice = input("\nrock paper scissor\n\nEnter your choice : ")

    if(com_choice == user_choice):
        print("IT'S TIE\n")
    elif(com_choice == "rock"):
        if(user_choice == "paper"):
            user_win += 1
            print("WOH YOU WIN !\n")
        else:
            com_win += 1
            print("OH YOU LOSS\n")
    elif(com_choice == "paper"):
        if(user_choice == "scissor"):
            user_win += 1
            print("WOH YOU WIN !\n")
        else:
            com_win += 1
            print("OH YOU LOSS\n")
    elif(com_choice == "scissor"):
        if(user_choice == "rock"):
            user_win += 1
            print("WOH YOU WIN !\n")
        else:
            com_win += 1
            print("OH YOU LOSS\n")
    else:
        print("YOU INTERED WRONG CHOICE\n") 

    print(f"you choose : {user_choice}")
    print(f"computer choose : {com_choice}\n")
    

    ch = input("Do  you want to repeat yes or no : ")
    if(ch == "yes"):
        choice = True
    elif(ch == "no"):
        choice = False
        print(f"You win {user_win} time")
        print(f"Computer win {com_win} time\n")
    else:
        choice = False
        print(f"\nYou win {user_win} time")
        print(f"Computer win {com_win} time\n")
        print("You enter incorrect option\n")   

