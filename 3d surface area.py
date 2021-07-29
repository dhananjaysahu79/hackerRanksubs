def surfaceArea(board,h,w):
    total = 0
    for i in range(h):
        for j in range(w):
            total += 4 * board[i][j] + 2
            if j < w - 1:
                total -= (board[i][j] + board[i][j+1] - abs(board[i][j] - board[i][j+1]))
            if i < h - 1:
                total -= (board[i][j] + board[i+1][j] - abs(board[i][j] - board[i+1][j]))
    return total


h,w = map(int,input().split())
board = []
for _ in range(h):
    board.append(list(map(int,input().split())))
print(surfaceArea(board,h,w))
