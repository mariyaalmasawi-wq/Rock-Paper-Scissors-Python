import random 


rock_ascii = """
🤜
"""
paper_ascii = """
✋
"""
scissors_ascii = """
✌
"""
#welcome 
print("Welcome to the Rock, Paper, Scissors game:")
answer = input("Press Enter to continue or type (Help) for the rules help ").capitalize()
if answer == "Help" :
    print("""
          *************** RULES ***************
          1) You choose and the computer chooses
          2)Rock smashes Scissors -> Rock wins
          3) Scissors cut Paper -> Scissors win
          4)Paper covers Rock -> Paper wins
           """)
chooce = input("Enter your chooce (rock, paper, scissors): ").lower()
chooce_computer = random.choice(["rock","paper","scissors"])
if chooce not in ["rock","paper","scissors"]:
    print ("Invalid choice. Please run the program again ")
elif chooce == "rock" :
    if chooce_computer == "rock" :
        print (f"You chose: \n{rock_ascii}\n computer chose: \n{rock_ascii}")
        print ("It's a draw")
    elif chooce_computer == "paper" :
        print (f"You chose: \n{rock_ascii}\n computer chose: \n{paper_ascii}")
        print ("You lose!")
    else :
        print (f"You chose: \n{rock_ascii}\n computer chose: \n{scissors_ascii}")
        print ("You win!")
elif chooce == "paper" :
    if chooce_computer == "paper" :
        print (f"You chose: \n{paper_ascii}\n computer chose: \n{paper_ascii}")
        print ("It's a draw")
    elif chooce_computer == "rock" :
        print (f"You chose: \n{paper_ascii}\n computer chose: \n{rock_ascii}")
        print ("You win!")
    else :
        print (f"You chose: \n{paper_ascii}\n computer chose: \n{scissors_ascii}")
        print ("You lose!")
elif chooce == "scissors" :
    if chooce_computer == "scissors" :
        print (f"You chose: \n{scissors_ascii}\n computer chose: \n{scissors_ascii}")
        print ("It's a draw")
    elif chooce_computer == "paper" :
        print (f"You chose: \n{scissors_ascii}\n computer chose: \n{paper_ascii}")
        print ("You win!")
    else :
        print (f"You chose: \n{scissors_ascii}\n computer chose: \n{rock_ascii}")
        print ("You lose!")
else :
    print ("Invalid choice. Please run the program again ")