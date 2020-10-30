import random
import sys

moves = {1 : "ROCK", 2: "PAPER", 3: "SCISSORS"}

def main():
    run = True
    print("Welcome to Rock, Paper, Scissors !")
    while(run):
        # Present action to user
        for move in moves.items():
            print(move[0], "-", move[1])
        print("q - Quit game")
        # Take input from user
        action = input()
        # Verify if user wants to quit
        if str(action).lower() == "q":
            # Quit game
            print("Thanks for playing !")
            # run = False
            sys.exit()

        # Verify if the input is a number
        try:
            int(action)
        except:
            print("Wrong action ! Retry")
            continue
        user_move = int(action)
        # Verify it is a valid number (1,2,3)
        if moves.get(user_move):
            print("You have chosen : ", moves.get(user_move))
            opponent_move = random.randint(1,3)
            print("Opponent has chosen : ", moves.get(opponent_move))
            winner(moves.get(user_move), moves.get(opponent_move))
        # Retry
        else:
            print("Wrong action ! Retry")
        
def winner(user_move, opponent_move):
    # User won
    # User = Rock > Opponent = Scissors
    if user_move == moves.get(1) and opponent_move == moves.get(3):
        print("You won ! :)")
    # User = Paper > Opponent = Rock
    elif user_move == moves.get(2) and opponent_move == moves.get(1):
        print("You won ! :)")
    # User = Scissors > Opponent = Paper
    elif user_move == moves.get(3) and opponent_move == moves.get(2):
        print("You won ! :)")
    # Opponent won
    # User = Rock < Opponent = Paper
    elif user_move == moves.get(1) and opponent_move == moves.get(2):
        print("You lost ! :(")
    # User = Paper < Opponent = Scissors
    elif user_move == moves.get(2) and opponent_move == moves.get(3):
        print("You lost ! :(")
    # User = Scissors < Opponent = Rock
    elif user_move == moves.get(3) and opponent_move == moves.get(1):
        print("You lost ! :(")
    # Neither won nor lost
    else:
        print("It's a tie ! :|")

main()