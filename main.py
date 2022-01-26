import random
import art

print(logo)
possible_actions = ["rock", "paper", "scissors"]
repeat_game = True
computer_score=0
user_score=0

def game(s):
    if s == "y":
        return True
    elif s == "n":
        return False
    elif s=="q" :
        return "end"
    else:
        print(" Sorry .Input is not valid.!!")
        return game(input("Do you want to continue? Y/N"))

while repeat_game:
    #computer selecting random value from rock, paper and scissors
    computer_action = random.choice(possible_actions)
    #user input taken from console
    user_action = input("Enter a choice (rock, paper, scissors): ")
    #print values chosen b computer and user
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")
    #game logic
    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    #user chose rock
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
            user_score = user_score + 1
        else:
            print("Paper covers rock! You lose.")
            computer_score = computer_score + 1
    #user chose paper
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
            user_score = user_score + 1
        else:
            print("Scissors cuts paper! You lose.")
            computer_score = computer_score + 1
    #user chose scissors
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
            user_score = user_score + 1
        else:
            print("Rock smashes scissors! You lose.")
            computer_score = computer_score + 1
    repeat_game=game(input("Do you want to continue? Y/N ").lower())
    if repeat_game == "end":
        break;
print("Total Score : \n Computer Score: "+{computer_score}+" ,User Score: "+{user_score})
if user_score > computer_score :
    print("User won the Game !!!")
elif user_score < computer_score :
    print("User Lost. Computer won the Game !!")
else:
    print("Its a draw overall.!!")
