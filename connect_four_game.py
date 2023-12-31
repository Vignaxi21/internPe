def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 29)
    print("   1   2   3   4   5   6   7")

def check_win(board, player):
    # Check horizontal
    for row in board:
        for col in range(4):
            if row[col:col + 4] == [player] * 4:
                return True

    # Check vertical
    for col in range(7):
        for row in range(3):
            if [board[row + i][col] for i in range(4)] == [player] * 4:
                return True

    # Check diagonal (top-left to bottom-right)
    for row in range(3):
        for col in range(4):
            if [board[row + i][col + i] for i in range(4)] == [player] * 4:
                return True

    # Check diagonal (top-right to bottom-left)
    for row in range(3):
        for col in range(3, 7):
            if [board[row + i][col - i] for i in range(4)] == [player] * 4:
                return True

    return False

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def main():
    board = [[" " for _ in range(7)] for _ in range(6)]
    current_player = "X"

    while True:
        print_board(board)
        column = int(input(f"Player {current_player}, enter column (1-7): ")) - 1

        if column < 0 or column >= 7 or board[0][column] != " ":
            print("Invalid move. Try again.")
            continue

        # Make the move
        for row in range(5, -1, -1):
            if board[row][column] == " ":
                board[row][column] = current_player
                break

        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    main()