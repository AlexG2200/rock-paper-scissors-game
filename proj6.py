# CSCI 1170-004
# 11/11/25
# This project will allow you to play rock,paper,scizzors with a computer
import random


def main():
    random.seed(451) 

    # giving my functions variables to be called easier
    Player_name = introduction()
    x = get_user_play(Player_name)
    y = get_computer_play()

    # setting the counter values for my print statics function
    User_wins = 0
    Computer_wins = 0
    Ties = 0
    Games_played = 0

    # I initialize the loop here for the game 
    while x != -1:
        # This logic tests to see if its a tie game
        if x == y:
            print(f"{Player_name} plays {x}, Computer plays {y}")
            print("Its a tie!")
            Ties += 1

            #this is to check if the user wins
        elif x == "Rock" and y == "Scissors":
            print(f"{Player_name} plays {x}, Computer plays {y}")
            print(f"{x} breaks scissors. {Player_name} wins!")
            User_wins += 1

        elif x == "Paper" and y == "Rock":
            print(f"{Player_name} plays {x}, Computer plays {y}")
            print(f"{x} covers rock. {Player_name} wins!")
            User_wins += 1

        elif x == "Scissors" and y == "Paper":
            print(f"{Player_name} plays {x}, Computer plays {y}")
            print(f"{x} cuts paper. {Player_name} wins!")
            User_wins += 1

            # this below validates and checks for the computers win
        elif y == "Rock" and x == "Scissors":
            print(f"{Player_name} plays {x}, Computer plays {y}")
            print(f"{y} breaks scissors. Computer wins!")
            Computer_wins += 1
        elif y == "Paper" and x == "Rock":
            print(f"{Player_name} plays {x}, Computer plays {y}")
            print(f"{y} covers rock. Computer wins!")
            Computer_wins += 1
        elif y == "Scissors" and x == "Paper":
            print(f"{Player_name} plays {x}, Computer plays {y}")
            print(f"{y} cuts paper. Computer wins!")
            Computer_wins += 1

        # this adds to game count and re runs the loop as long as input value is not -1
        Games_played +=1
        x = get_user_play(Player_name)
        y = get_computer_play()

    # prints the games stats at the exit of the loop
    print_statistics(Games_played, User_wins, Computer_wins, Ties, Player_name)
    

                           
def get_user_play(Player_name):
    choice = int(input("Enter your move (0 for Rock, 1 for Paper, 2 for Scissors): "))

    if choice == 0:
        return "Rock"
    elif choice == 1:
        return "Paper"
    elif choice == 2:
        return "Scissors"
    elif choice == -1:
        return -1


def get_computer_play():
    number = random.random()
    
    if number < 0.25:
        return "Rock"
    elif number <= 0.65:
        return "Paper"
    else:
        return "Scissors"
    

def introduction():
    Name = input("What is your name? ")
    
    print("Welcome to the game Rock, Paper, Scissors. you will be playing against the computer.")
    print(f"Here are the rules {Name}: ")
    print("if a player chooses Rock and the other chooses Scissors, Rock Wins.")
    print("If a player chooses Scissors and the other chooses Paper, Scissors Wins.")
    print("If a player chooses Paper and the other chooses Rock, Paper Wins.")
    print("If both players make the same choice, it's a tie.")
    print("Enter -1 to quit the game")
    return Name
    


def print_statistics(Games_played, User_wins, Computer_wins, Ties, Player_name):
    print(f"There were {Games_played} games: {Player_name} won {User_wins} games, The computer won {Computer_wins} games, and there were {Ties} ties.")



main()
    