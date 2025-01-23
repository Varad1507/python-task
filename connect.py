ROWS, COLS = 6, 7

def create_board():
    return [[" " for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    for row in board: print("|" + "|".join(row) + "|")
    print("-" * (2 * COLS + 1))
    print(" " + " ".join(map(str, range(1, COLS + 1))))

def drop_piece(board, col, piece):
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == " ":
            board[row][col] = piece
            return row

def is_winner(board, piece):
    for r in range(ROWS):  # Horizontal
        for c in range(COLS - 3):
            if all(board[r][c + i] == piece for i in range(4)): return True
    for r in range(ROWS - 3):  # Vertical
        for c in range(COLS):
            if all(board[r + i][c] == piece for i in range(4)): return True
    for r in range(ROWS - 3):  # Diagonal \
        for c in range(COLS - 3):
            if all(board[r + i][c + i] == piece for i in range(4)): return True
    for r in range(3, ROWS):  # Diagonal /
        for c in range(COLS - 3):
            if all(board[r - i][c + i] == piece for i in range(4)): return True
    return False

def is_full(board):
    return all(board[0][c] != " " for c in range(COLS))

def play_game():
    board = create_board()
    turn, game_over = 0, False
    print_board(board)
    pieces = ["\033[31m●\033[0m", "\033[34m●\033[0m"]  # Red and Blue small circles
    
    while not game_over:
        player = pieces[turn % 2]
        try:
            col = int(input(f"Player {player}, choose column (1-{COLS}): ")) - 1
            if 0 <= col < COLS and board[0][col] == " ":
                row = drop_piece(board, col, player)
                print_board(board)
                if is_winner(board, player):
                    print(f"Player {player} wins!")
                    game_over = True
                elif is_full(board):
                    print("It's a draw!")
                    game_over = True
                else:
                    turn += 1
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Enter a number between 1 and 7.")

if __name__ == "__main__":
    play_game()
