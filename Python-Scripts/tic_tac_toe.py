import random

def display_board(board): #game board
    print(f"\n{board[0][0]} | {board[0][1]} | {board[0][2]}")
    print("--+---+--")
    print(f"{board[1][0]} | {board[1][1]} | {board[1][2]}")
    print("--+---+--")
    print(f"{board[2][0]} | {board[2][1]} | {board[2][2]}\n")

def enter_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): "))
            if move < 1 or move > 9:
                print("Please enter a number between 1 and 9.")
                continue
            row, col = divmod(move - 1, 3)

            if board[row][col] not in ['X', 'O']:  # Check if the square is free
                board[row][col] = 'O'     #player places an 'O' on the board
                break
            else:
                print("The square is already taken, try again.")
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 9.")

def make_list_of_free_fields(board): # Returns a list of free spots 
    free_fields = []
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ['X', 'O']:  # If the spot is free
                free_fields.append((row, col))
    return free_fields

def victory_for(board, sign): # Checks who won
    for i in range(3):
        if all([board[i][j] == sign for j in range(3)]) or all([board[j][i] == sign for j in range(3)]):
            return True
    
    # Check diagonals for a win
    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return True
    if board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        return True
    
    return False 

def draw_move(board): # The computer randomly places an 'X' on the board
    free_fields = make_list_of_free_fields(board)
    if free_fields:
        row, col = random.choice(free_fields)  # Randomly choose a free spot
        board[row][col] = 'X'  # Computer places an 'X' on the board

def is_board_full(board): # Returns True if the board is full (no empty spots left)
    for row in board:
        if any(cell not in ['X', 'O'] for cell in row):
            return False
    return True

def main():
    board = [[str(i + 1 + j * 3) for i in range(3)] for j in range(3)] # Initialize the board as a 3x3 matrix with numbers 1-9
    
    # The game continues until there's a winner or the board is full
    while True:
        display_board(board)

        # Player's move
        enter_move(board)

        # Check if the player has won
        if victory_for(board, 'O'):
            display_board(board)
            print("Congratulations! You win!")
            break

        # Check if the board is full
        if is_board_full(board):
            display_board(board)
            print("It's a tie!")
            break
        
        # Computer's move
        draw_move(board)
        
        # Check if the computer has won
        if victory_for(board, 'X'):
            display_board(board)
            print("Computer wins!")
            break
        
        # Check if the board is full
        if is_board_full(board):
            display_board(board)
            print("It's a tie!")
            break

if __name__ == "__main__":
    main()
