#ボードを静的評価する．
def staticEvaluate(board, tile):
#def staticEvaluate(board, playerTile, computerTile):
    if tile == '●':
        opTile = '○'
    else:
        opTile = '●'

    total = 0
    weight = [
        [120, -20, 20,  5,  5,  20, -20, 120],
        [-20, -40, -5, -5, -5,  15, -40, -20],
        [ 20,  -5, 15,  3,  3,  15,  -5,  20],
        [  5,  -5,  3,  3,  3,   3,  -5,   5],
        [  5,  -5,  3,  3,  3,   3,  -5,   5],
        [ 20,  -5, 15,  3,  3,  15,  -5,  20],
        [-20, -40, -5, -5, -5,  15, -40, -20],
        [120, -20, 20,  5,  5,  20, -20, 120],
    ]
    for x in range(8):
        for y in range(8):
            if board[x][y] == opTile:
                total -= weight[x][y]
            if board[x][y] == tile:
                total += weight[x][y]
    return total
