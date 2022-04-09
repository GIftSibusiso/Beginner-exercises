from random import choice


print(f"\nWELCOME TO MY ROCK, PAPER SCISSORS GAME!!!!\n{'-'*50}")

while True:
    response = input("Do you wanna play?:  ").lower()
    if response == "no":
        print("Alright then, your loss...")
        quit()
    elif response == "yes":
        print("Let the games begin\n\n")
        break
    else:
        print("Invalid input try again")

options, computers_score, players_score, game_plays = ["rock", "paper", "scissors"], 0, 0, 0

while game_plays < 3:
    players_selection = input("Choose between rock, paper, scissors: ")
    if players_selection not in options:
        print("Invalid selection")
        continue
    computers_selection = choice(options)

    if players_selection == "rock" and computers_selection == "scissors":
        players_score += 1
        print("You win this round")
    elif players_selection == "paper" and computers_selection == "rock":
        players_score += 1
        print("You win this round")
    elif players_selection == "scissors" and computers_selection == "paper":
        players_score += 1
        print("You win this round")
    elif players_selection == computers_selection:
        print("Draw game")
    else:
        computers_score += 1
        print("Computer wins")
    
    print(f"Computer chose: {computers_selection}")
    game_plays += 1

print(f"\nYou scored {players_score}")
if players_score > computers_score:
    print("You have won the game!!!")
elif players_score < computers_score:
    print("You lost to a computer, Imbecile")
else:
    print("It's a draw game")
