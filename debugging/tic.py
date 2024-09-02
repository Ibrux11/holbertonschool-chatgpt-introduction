#!/usr/bin/python3

def print_board(board):
    """
    Prints the current state of the board in a formatted way.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board):
    """
    Checks if there is a winner in the game.
    
    Returns:
        bool: True if there is a winner, False otherwise.
    """
    # Check rows for a win
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns for a win
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals for a win
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False


def check_tie(board):
    """
    Checks if the game is a tie, meaning the board is full and no player has won.
    
    Returns:
        bool: True if the board is full and there is no winner, False otherwise.
    """
    for row in board:
        if " " in row:
            return False
    return True


def tic_tac_toe():
    """
    Main function to play the Tic-Tac-Toe game between two players.
    """
    board = [[" "] * 3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        # Input validation
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
            if row < 0 or row > 2 or col < 0 or col > 2:
                print("Invalid input. Please enter a valid row and column between 0 and 2.")
                continue
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue

        # Check if the spot is already taken
        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        # Make the move
        board[row][col] = player

        # Check for a winner
        if check_winner(board):
            print_board(board)
            print(f"Player {player} wins!")
            break

        # Check for a tie
        if check_tie(board):
            print_board(board)
            print("It's a tie!")
            break

        # Switch players
        player = "O" if player == "X" else "X"


# Run the game
tic_tac_toe()
