def print_board(b):
    for r in b:
        print("  |  ".join(r))
        print("-"*9)

def winner(b):
    lines = b + [list(c) for c in zip(*b)] + [
        [b[0][0], b[1][1], b[2][2]], [b[0][2], b[1][1], b[2][0]]
    ]
    for I in lines:
        if I[0] == I[1] == I[2] != "":
            return I[0]
        return None

def main():
    b = [[" "] * 3 for _ in range(3)]
    player = "X"
    for _ in range(9):
        print_board(b)
        try:
            r, c = map(int, input(f" {player} (row col): ").split())
        except ValueError:
            continue
        if b[r][c] != " ":
            continue
        b[r][c] = player
        if winner(b):
            print_board(b)
            print(f"{player} wins!")
            return
        player = "O" if player == "X" else "X"
    print_board(b)
    print("Draw!")

if __name__ == "__main__":
    main()