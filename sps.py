import random
user_score = 0
computer_score = 0
while True:
    choices = input("enter a choice: ")
    choices = choices.lower()
    print("your choice is",choices)


    options = ["stone","paper","scissor"]
    if choices not in options:
        print("invalid input\n")
        continue
    computer_option = random.choice(options)

    print("computer's choice is",computer_option)
   # if choices in options:
    if "stone" in choices:
        if "scissor" in computer_option:
            print("you won!! \n")
            user_score += 1
        elif "paper" in computer_option:
            print("you lost :(, maybe next time!\n")
            computer_score += 1
        elif "stone" in computer_option:
            print("it's a tie!\n")
    elif "scissor" in choices:
        if "paper" in computer_option:
            print("you won!!\n")
            user_score += 1
        elif "stone" in computer_option:
            print("you lost :(, maybe next time!\n")
            computer_score += 1
        elif "scissor" in computer_option:
            print("it's a tie!\n")
    elif "paper" in choices:
        if "stone" in computer_option:
            print("you won!!\n")
            user_score += 1
        elif "scissor" in computer_option:
            print("you lost :(, maybe next time!\n")
            computer_score += 1
        elif "paper" in computer_option:
            print("it's a tie!\n")
    if user_score == 5:
        print("you have won the game and your score was",user_score)
        print("The computer lost and it's score was",computer_score)

        answer = input("Do you want to continue? Enter Y for yes and N for no: ").lower()
        if answer == "y":
            user_score = 0
            computer_score = 0
            print()
            continue
        elif answer == "n":
            print()
            print("thanks for playing")
            break
        else:
            break
    if computer_score == 5:
        print("The computer won and it's score was",computer_score)
        print("You lost and your score was",user_score)

        answer = input("Do you want to continue? Enter Y for yes and N for no: ").lower()
        if answer == "y":
            user_score = 0
            computer_score = 0
            print()
            continue
        elif answer == "n":
            print()
            print("thanks for playing")
            break
        else:
            break
