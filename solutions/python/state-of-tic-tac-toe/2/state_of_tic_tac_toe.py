from collections import defaultdict
def gamestate(board):
    # check wins
    hm = defaultdict(int)
    wins = set()

    for i in range(3):

        # tracking the frequency
        for j in range(3):
            hm[board[i][j]] += 1

        # check rows
        if board[i][0] == board[i][1] == board[i][2] != " ":
            wins.add(board[i][0])

        # check columns
        if board[0][i] == board[1][i] == board[2][i] != " ":
            wins.add(board[0][i])

    # check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        wins.add(board[0][0])
    if board[0][2] == board[1][1] == board[2][0] != " ":
        wins.add(board[0][2])

    if len(wins) > 1:
        raise ValueError("Impossible board: game should have ended after the game was won")
    if hm["O"] > hm["X"]:
        raise ValueError("Wrong turn order: O started")
    if hm["X"] - hm["O"] > 1:
        raise ValueError("Wrong turn order: X went twice")

    if not wins:
        return "ongoing" if hm["O"] + hm["X"] < 9 else "draw"

    return "win"
    
