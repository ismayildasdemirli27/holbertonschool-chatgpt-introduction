#!/usr/bin/python3

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    
    while not check_winner(board):
        print_board(board)
        try:
            row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
            col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
            
            if not (0 <= row <= 2 and 0 <= col <= 2):
                print("Invalid input. Please enter 0, 1, or 2.")
                continue
                
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
        except EOFError:
            print("\nGame interrupted.")
            return

        if board[row][col] == " ":
            board[row][col] = player
            
            if check_winner(board):
                break
            
            if all(all(cell != " " for cell in r) for r in board):
                print_board(board)
                print("It's a draw!")
                return
                
            if player == "X":
                player = "O"
            else:
                player = "X"
        else:
            print("That spot is already taken! Try again.")

    print_board(board)
    print("Player " + player + " wins!")

if __name__ == "__main__":
    tic_tac_toe()
