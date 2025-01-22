def print_board(board):
  """Prints the current state of the Tic-Tac-Toe board."""
  print("-------------")
  for row in board:
    print("|", end="")
    for cell in row:
      print(f" {cell} |", end="")
    print("\n-------------")

def check_win(board):
  """Checks if there is a winner."""

  for row in board:
    if row[0] == row[1] == row[2] and row[0] != ' ':
      return row[0]

  for col in range(3):
    if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
      return board[0][col]

  if (board[0][0] == board[1][1] == board[2][2] or
      board[0][2] == board[1][1] == board[2][0]) and board[1][1] != ' ':
    return board[1][1]

  return None

def check_draw(board):
  """Checks if the game is a draw."""
  for row in board:
    for cell in row:
      if cell == ' ':
        return False
  return True

def get_player_move(board):
  """Gets the player's move."""
  while True:
    try:
      row = int(input("Enter row (1-3): ")) - 1
      col = int(input("Enter column (1-3): ")) - 1
      if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == ' ':
        return row, col
      else:
        print("Invalid move. Try again.")
    except ValueError:
      print("Invalid input. Please enter numbers.")

def play_game():
  """Plays a game of Tic-Tac-Toe."""
  board = [[' ' for _ in range(3)] for _ in range(3)]
  current_player = 'X'

  while True:
    print_board(board)
    print(f"Player {current_player}'s turn.")

    row, col = get_player_move(board)
    board[row][col] = current_player

    winner = check_win(board)
    if winner:
      print_board(board)
      print(f"Player {winner} wins!")
      break

    if check_draw(board):
      print_board(board)
      print("It's a draw!")
      break

    current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
  play_game()