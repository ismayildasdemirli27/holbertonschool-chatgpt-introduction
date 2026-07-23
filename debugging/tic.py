#!/usr/bin/python3

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

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
    while True:
        print_board(board)
        try:
            row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
            col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
            
            # Sərhədlərin yoxlanılması (IndexError qarşısını alır)
            if row not in range(3) or col not in range(3):
                print("Coordinates must be 0, 1, or 2. Try again.")
                continue

            if board[row][col] == " ":
                board[row][col] = player
                
                # Qalibiyyəti oyunçu dəyişməmişdən əvvəl yoxlayırıq
                if check_winner(board):
                    print_board(board)
                    print("Player " + player + " wins!")
                    return
                
                # Heç-heçə vəziyyətini yoxlayırıq
                is_tie = True
                for r in board:
                    if " " in r:
                        is_tie = False
                
                if is_tie:
                    print_board(board)
                    print("It's a tie!")
                    return

                # Oyunçunu növbəti dövr üçün dəyişirik
                if player == "X":
                    player = "O"
                else:
                    player = "X"
            else:
                print("That spot is already taken! Try again.")
        except ValueError:
            # Hərf yazılmasının qarşısını alır
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    tic_tac_toe()
