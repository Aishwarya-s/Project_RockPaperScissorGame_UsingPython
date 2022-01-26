import random
from art import logo

print(logo)

possible_actions = ["rock", "paper", "scissors", "lizard", "spock"]
repeat_game = True
computer_score = 0
user_score = 0

def game(s):
    if s == "y":
        return True
    elif s == "n":
        return False
    else:
        print("Selection is not understandable")
        return game(input("Do you want to continue? Y/N").lower())
while repeat_game:
  computer_action = random.choice(possible_actions)
  user_action = int(input("Choose one from 1 to 5 -\n1.Rock\n2.Paper\n3.Scissors\n4.Lizard\n5.Spock "))
  user_action = user_action - 1
  user_action = possible_actions[user_action]
  print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")
#game logic
  if user_action == computer_action:
    print(f"Both players selected {user_action}. It's a tie!")
  elif user_action == "rock":
    if computer_action == "scissors":
        print("Rock smashes scissors! You win!")
        user_score = user_score + 1
    elif computer_action == "lizard":
        print("Rock crushes lizard! You win!")
        user_score = user_score + 1
    elif computer_action == "spock":
        print("Spock Vapourizes rock! You Lost!")
        computer_score = computer_score + 1
    elif computer_action == "paper":
        print("paper covers rock! You Lost!")
        computer_score = computer_score + 1
  elif user_action == "paper":
    if computer_action == "rock":
        print("Paper covers rock! You win!")
        user_score = user_score + 1
    elif computer_action == "spock":
        print("Paper disproves spock! You win!")
        user_score = user_score + 1
    elif computer_action == "lizard":
        print("Lizard Eats paper! You Lost!")
        computer_score = computer_score + 1
    elif computer_action == "scissors":
        print("scissor cuts paper! You Lost!")
        computer_score = computer_score + 1
  elif user_action == "scissors":
    if computer_action == "paper":
        print("Scissor cuts paper! You win!")
        user_score = user_score + 1
    elif computer_action == "spock":
        print("Scissor decapitates lizard! You win!")
        user_score = user_score + 1
    elif computer_action == "rock":
        print("Rock crushes scissors! You Lost!")
        computer_score = computer_score + 1
    elif computer_action == "smock":
        print("Smock smashes scissors! You Lost!")
        computer_score = computer_score + 1
  elif user_action == "lizard":
    if computer_action == "spock":
        print("lizard poisons spock! You win!")
        user_score = user_score + 1
    elif computer_action == "paper":
        print("lizard eats paper! You win!")
        user_score = user_score + 1
    elif computer_action == "rock":
        print("rock crushes lizard! You Lost!")
        computer_score = computer_score + 1
    elif computer_action == "scissors":
        print("scissors decapitates lizards! You Lost!")
        computer_score = computer_score + 1
  elif user_action == "spock":
    if computer_action == "scissors":
        print("spock smashes scissors! You win!")
        user_score = user_score + 1
    elif computer_action == "rock":
        print("spock vapourises rock! You win!")
        user_score = user_score + 1
    elif computer_action == "paper":
        print("paper disproves rock! You Lost!")
        computer_score = computer_score + 1
    elif computer_action == "lizard":
        print("lizards poisons spock! You Lost!")
        computer_score = computer_score + 1

  repeat_game = game(input("Do you want to continue? Y/N").lower())

# print the score
print("Total Score:\n Computer Score:" + str({computer_score}) + " , User Score:" + str({user_score}))
