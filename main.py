import random
import sys

moves = {1 : "ROCK", 2: "PAPER", 3: "SCISSORS"}
nb_games_played = 0
nb_games_won = 0

def main():
    run = True
    while(run):
        # Present action to user
        print("---- POSSIBLE ACTIONS ----")
        print("h - Rules")
        print("s - Statistics")
        print("q - Quit game")
        print("----- MOVE SELECTION -----")
        for move in moves.items():
            print(move[0], "-", move[1])
        print("--------------------------")
        # Take input from user
        action = input()
        # Verify if user wants to quit
        if str(action).lower() == "q":
            # Quit game
            print("Thanks for playing!")
            # run = False
            sys.exit()

        # Help menu
        if str(action).lower() == "h":
            print("------ GAME RULES -------")
            print("#1",moves.get(1), "beats", moves.get(3))
            print("#2",moves.get(2), "beats", moves.get(1))
            print("#3",moves.get(3), "beats", moves.get(2))
            print("--------------------------")
            continue
        
        if str(action).lower() == "s":
            print("------ STATISTICS -------")
            print("Total of games played:", nb_games_played)
            print("Total of games won:", nb_games_won)
            if nb_games_played != 0:
                print("Win rate:", str(nb_games_won * 100 // nb_games_played) + "%")
            else:
                print("Win rate: No games played yet")
            print("--------------------------")
            continue

        # Verify if the input is a number
        try:
            int(action)
        except:
            print("Wrong action! Retry")
            continue
        user_move = int(action)
        # Verify it is a valid number (1,2,3)
        if moves.get(user_move):
            # Generate opponent move randomly
            opponent_move = random.randint(1,3)
            print("---------- GAME ----------")
            print("You:", moves.get(user_move))
            print("Opponent:", moves.get(opponent_move))
            # winner_2(moves.get(user_move), moves.get(opponent_move))
            # Who won
            winner(user_move, opponent_move)
            print("--------------------------")
        # Retry
        else:
            print("Wrong action! Retry")

"""
When user wins, user = opp + 1
When opp wins, opp = user + 1, i.e.
- user = 3 (Scissors) and opp = 1 (Rock) => (3 % 3) + 1 = 1 == 1
- user = 2 (Paper) and opp = 3 (Scissors) => (2 % 3) + 1 == 3
- user = 1 (Rock) and opp = 2 (Paper) => (1 % 1) + 1 == 2
When it's a tie, nothing is equal, i.e.
- user = 1 (Rock) and opp = 1 (Rock) => (1 % 3) + 1 != 1
"""
def winner(user_move, opponent_move):
    # User won
    if (opponent_move % 3) + 1 == user_move:
        global nb_games_won
        nb_games_won += 1
        print("WON ! :)")
    # Opponent won
    elif (user_move % 3) + 1 == opponent_move:
        print("LOST ! :(")
    # Tie
    else:
        print("TIE ! :|")
    global nb_games_played
    nb_games_played += 1

def winner_2(user_move, opponent_move):
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
    # Tie
    else:
        print("It's a tie ! :|")

main()