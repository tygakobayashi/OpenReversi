import sys
#reversi操作ファイル
import reversi
#評価値を返す
import evaluate

print('Welcome to Reversi.')

while True:
    mainBoard = reversi.getNewBoard()
    reversi.resetBoard(mainBoard)
    #playerTileには'●', '○'のいずれかが格納される．
    playerTile, computerTile = reversi.enterPlayerTile()
    showHints = False
    turn = reversi.whoGoesFirst(playerTile)
    print('The ' + turn + ' will go first.')

    while True:
        if turn == 'player':
            if showHints:
                validMovesBoard = reversi.getBoardWithValidMoves(mainBoard, playerTile)
                reversi.drawBoard(validMovesBoard)
            else:
                reversi.drawBoard(mainBoard)
            reversi.showPoints(mainBoard, playerTile, computerTile)
            move = reversi.getPlayerMove(mainBoard, playerTile)
            if move == 'quit':
                print('Thank you for playing.')
                sys.exit()
            elif move == 'hints':
                showHints = not showHints
                continue
            else:
                reversi.makeMove(mainBoard, playerTile, move[0], move[1])

            if reversi.getValidMoves(mainBoard, computerTile) == []:
                break
            else:
                turn = 'computer'

        else:
            reversi.drawBoard(mainBoard)
            reversi.showPoints(mainBoard, playerTile,computerTile)
            input('Press Enter to see the computer\'s move.')
            x,y = reversi.getComputerMove(mainBoard, computerTile)
            reversi.makeMove(mainBoard, computerTile, x, y)
            print('>computer:(%d, %d)'%(x+1,y+1))

            if reversi.getValidMoves(mainBoard, playerTile) == []:
                break
            else:
                turn = 'player'

    reversi.drawBoard(mainBoard)
    scores = reversi.getScoreOfBoard(mainBoard)
    print('White scored %d points. Black scored %d points.'%(scores['●'], scores['○']))
    if scores[playerTile] > scores[computerTile]:
        print('You beat the computer by %d points. Congratulations!'%(scores[playerTile] - scores[computerTile]))
    elif scores[playerTile] < scores[computerTile]:
        print('You lost. The computer beat you by %d points.'%(scores[computerTile] - scores[playerTile]))
    else:
        print('The game was a tie.')

    if not reversi.playAgain():
        break
