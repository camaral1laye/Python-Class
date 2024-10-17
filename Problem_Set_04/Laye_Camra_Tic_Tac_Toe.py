# Function to initialize the board
def initialize_board():
    return [[" " for _ in range(3)] for _ in range(3)]

# Function to print the board
def print_board(board):
    print("\n+---+---+---+")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("+---+---+---+")

# Function to check for a winner
def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]) or all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

# Function to check if the board is full (tie)
def is_board_full(board):
    return all([cell != " " for row in board for cell in row])

# Function to get the player's move
def get_move(player):
    while True:
        try:
            row = int(input(f"{player}'s turn. Pick a row (1, 2, 3): ")) - 1
            col = int(input(f"Pick a column (1, 2, 3): ")) - 1
            if row in range(3) and col in range(3):
                return row, col
            else:
                print("Invalid input. Please enter a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter valid numbers.")

# Function to play Tic Tac Toe
def play_game():
    board = initialize_board()
    current_player = "X"
    
    while True:
        print_board(board)
        row, col = get_move(current_player)
        
        if board[row][col] == " ":
            board[row][col] = current_player
        else:
            print("This cell is already taken. Choose another one.")
            continue
        
        # Check for winner
        if check_winner(board, current_player):
            print_board(board)
            print(f"{current_player} wins! \nGame over!")
            break
        
        # Check for tie
        if is_board_full(board):
            print_board(board)
            print("It's a tie! Game over!")
            break
        
        # Switch player
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    print("Welcome to Tic Tac Toe")
    play_game()