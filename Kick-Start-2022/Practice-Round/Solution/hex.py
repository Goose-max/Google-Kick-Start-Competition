"""
Hex
Input: NxN array
Output: State of game board
Limit: Maximum board sizes increases between test sets

Graph travesal using flood fill
    Start from left edge, visit adjacent hexes with blue stones, repeat
    No more hexes to visit, check if any hexes on right edge have been visited
    Repeat process for red (top to bottom)
    Note: Cannot be connected paths for both Blue and Red
"""
DIRECTIONS = ((0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1), (1, 0))


def flood(board, row, col, n, color):
    """
    Flood fill approach
    """
    board[row][col] = color.lower()
    for directions in DIRECTIONS:
        new_row, new_col = row + directions[0], col + directions[1]
        if (0 <= new_row < n) and (0 <= new_col < n):
            if board[new_row][new_col] == color:
                flood(board, new_row, new_col, n, color)


def check_winner(board, n):
    """
    Check each hexes -  marking visited hexes with lower case letter
    """
    for i in range(n):
        if board[i][0] == "B":
            flood(board, i, 0, n, "B")
        if board[0][i] == "R":
            flood(board, 0, i, n, "R")

    for i in range(n):
        if board[i][n - 1] == "b":
            return "B"
        if board[n - 1][i] == "r":
            return "R"

    return "."


def game_status(board_size, board):
    # TODO: implement this method to determine the status of the game board
    # red, blue = count_stones(board_size)

    return ""


def main():
    test_cases = int(input())
    for test_case in range(1, test_cases + 1, 1):
        board_size = int(input())
        board = []
        for _ in range(board_size):
            board.append(list(input().strip()))

        ans = game_status(board_size, board)

        print("Case #{}: {}".format(test_case, ans))


if __name__ == "__main__":
    main()
