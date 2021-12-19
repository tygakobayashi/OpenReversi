import random
import sys
import math
import evaluate

def drawBoard(board):
    HLINE = ' +---+---+---+---+---+---+---+---+'
    VLINE = ' |   |   |   |   |   |   |   |   |'
    print('   1   2   3   4   5   6   7   8')
    print(HLINE)
    for y in range(8):
        #print(VLINE)
        print(y+1, end='')
        for x in range(8):
            print('| %s '%(board[y][x]),end = '')
        print('|',end = '')
        print(y+1)
        #print(y+1, end='')
        #print(VLINE)
        print(HLINE)
    print('   1   2   3   4   5   6   7   8')

def resetBoard(board):
    for x in range(8):
        for y in range(8):
            board[x][y] = ' '

    #initialise the game.
    board[3][3] = '●'   #white
    board[3][4] = '○'   #black
    board[4][3] = '○'
    board[4][4] = '●'

    #board[3][3] = '○'   #white
    #board[3][4] = '●'   #black
    #board[4][3] = '●'
    #board[4][4] = '○'

def getNewBoard():
    board = []
    for i in range(8):
        board.append([' '] * 8)

    return board

def isValidMove(board, tile, xstart, ystart):
    #その場所が空である，またはボード上ではないときFalseを返す．
    #if board[xstart][ystart] != ' ' or not isOnBoard(xstart,ystart):
        #return False
    if board[xstart][ystart] != ' ':
        return False
    if not isOnBoard(xstart, ystart):
        return False
    #一時的に置く
    board[xstart][ystart] = tile
    #プレイヤーの置いたタイルの色を見て，otherTileを決定する．
    if tile == '●':
        otherTile = '○'
    else:
        otherTile = '●'
    #フリップできるタイルを格納する．
    tilesToFlip = []
    #置いた場所に隣接する８方向を探索する．
    for xdirection, ydirection in [[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]:
        x,y = xstart, ystart
        x += xdirection
        y += ydirection
        #探索先がボード上かつ，そこに相手のタイルがある場合，その方向の探索を続ける．
        if isOnBoard(x,y) and board[x][y] == otherTile:
            x += xdirection
            y += ydirection
            #進んだ先がボード上でなくなった時，53行目のfor loopに戻り，次の方向の探索を開始する．
            if not isOnBoard(x,y):
                continue
            #探索先上に相手のタイルがある限り続ける．
            while board[x][y] == otherTile:
                x += xdirection
                y += ydirection
                #ボード上から外れた時while文を抜ける．
                if not isOnBoard(x,y):
                    break
            #while文を抜けた後，53行目のfor loopへ戻るための操作．
            if not isOnBoard(x,y):
                continue
            #65行目のwhile文を抜けたボード上にプレイヤーと同じ色のタイルがある場合．
            if board[x][y] == tile:

                while True:
                    x -= xdirection
                    y -= ydirection
                    if x == xstart and y == ystart:
                        break
                    #プレイヤーのタイルから，置いたタイルまで逆に戻り，その場所をtilesToFlipへ格納する．
                    tilesToFlip.append([x,y])
    #仮に置いたタイルを空に戻す．
    board[xstart][ystart] = ' '
    #フリップできる相手のタイルがどの方向にもなかった場合，タイルをその場所へは置けないと判断する．
    if len(tilesToFlip) == 0:
        return False
    #tilesToFlipに値が格納されていた場合，それを返す．
    return tilesToFlip

def isOnBoard(x,y):
    #Return True if the coodinates are located on the board.
    #その場所がボード上か否かを返す．
    return x >= 0 and x <= 7 and y >= 0 and y <= 7

#dupeBoardにboardをコピーし，有効な手を'.'で表したボードに上書きし，それを返す．
def getBoardWithValidMoves(board, tile):
    dupeBoard = getBoardCopy(board)
    for x, y in getValidMoves(dupeBoard, tile):
        dupeBoard[x][y] = '.'
    return dupeBoard

#ボード上のその色のタイルが置ける場所を返す．
def getValidMoves(board,tile):
    validMoves = []
    for x in range(8):
        for y in range(8):
            if isValidMove(board, tile, x, y) != False:
                validMoves.append([x,y])
    return validMoves

def getScoreOfBoard(board):
    whiteScore = 0
    blackScore = 0
    for x in range(8):
        for y in range(8):
            if board[x][y] == '●':
                whiteScore += 1
            if board[x][y] == '○':
                blackScore += 1
    #ディクショナリを返す．
    return {'●': whiteScore, '○': blackScore}

#先手をランダムに決定させる．
def randomPlayerTile():
    if random.randint(0,1) == 0:
        return 'w'
    else:
        return 'b'

#プレイヤーはタイルの色を選ぶ．
def enterPlayerTile():
    tile = ' '
    while not (tile == 'w' or tile == 'b' or tile == 'r'):
        print('Do you want to play White or Black?')
        print('Enter "w" to play White or "b" to play Black.')
        print('Or Enter "r" to choose your colour randamly.')
        tile = input().lower()

    #ランダムに先手を決定する．
    if tile == 'r':
        tile = randomPlayerTile

    if tile == 'w':
        tile == '●'
        return ['●','○']
    else:
        tile == '○'
        return ['○','●']

#whiteが先手となる．
def whoGoesFirst(playerTile):
    if playerTile == '●':
        return 'player'
    else:
        return 'computer'

def playAgain():
    print('Do you want to play again?(yes/no)')
    return input().lower().startswith('y')

def makeMove(board, tile, xstart, ystart):
    #isValidMove関数でタイルが置けるか判定，置けた場合，tilesToFlipにフリップするマスのリストを格納する．
    tilesToFlip = isValidMove(board, tile, xstart, ystart)
    #置ける手でない場合Falseを返す．
    if tilesToFlip == False:
        return False
    #置ける場合，マスにタイルを置き，tilesToFlipに格納された座標のタイルをすべてフリップさせる．
    board[xstart][ystart] = tile
    for x, y in tilesToFlip:
        board[x][y] = tile
    return True

def getBoardCopy(board):
    #getNewBoard関数でboard構造体を作成．
    dupeBoard = getNewBoard()

    for x in range(8):
        for y in range(8):
            #現在のボード上のタイルの情報をdupeBoardへコピーする．
            dupeBoard[x][y] = board[x][y]

    return dupeBoard

def isOnCorner(x,y):
    #コーナーである場合，真を返す．
    return (x == 0 and y == 0) or (x == 7 and y == 0) or (x == 0 and y == 7) or (x == 7 and y == 7)

def getPlayerMove(board, playerTile):
    DIGIT1TO8 = '1 2 3 4 5 6 7 8'.split()
    while True:
        print('Enter your move, or type quit to end the game, or hints to turn off/on hints.')
        move = input().lower()
        if move == 'quit':
            return 'quit'
        if move == 'hints':
            return 'hints'

        if len(move) == 2 and move[0] in DIGIT1TO8 and move[1] in DIGIT1TO8:
            x = int(move[0]) - 1
            y = int(move[1]) - 1
            print('>player:(%d, %d)'%(x+1,y+1))
            #有効な手でなかった場合，下のelseへ続き，有効な手を入力するようメッセージを出力させる．
            if isValidMove(board, playerTile, x, y) == False:
                continue
            else:
                break
        else:
            print('That is not a valid move. Type the x digit(1-8), then the y digit(1-8).')
            print('For example, 81 will be the top-right corner.')

    return [x,y]

def getComputerMove(board, computerTile):
    #getValidMoves関数で，有効な座標をpossibleMovesへ格納する．
    possibleMoves = getValidMoves(board, computerTile)
    #リストの要素をシャッフルする．
    #コーナーに置ける場合，確実に置く．
    random.shuffle(possibleMoves)
    for x, y in possibleMoves:
        if isOnCorner(x,y):
            return [x,y]
    #置ける盤面の中で，最も評価値の高くなるマスに置く．
    bestScore = -1
    bestEval = -1000
    for x, y in possibleMoves:
        dupeBoard = getBoardCopy(board)
        makeMove(dupeBoard, computerTile, x, y)
        eval = evaluate.staticEvaluate(dupeBoard, computerTile)
        if(bestEval < eval):
            bestEval = eval
            bestMove = [x,y]
    return bestMove

def showPoints(board, playerTile, computerTile):
    scores = getScoreOfBoard(board)
    print('You have %s points. The computer has %s points.'%(scores[playerTile], scores[computerTile]))
