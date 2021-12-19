# OpenReversi
## The algorithm
The algorithm for Reversi consists of two principles.
1. The computer always places its own tile in a corner of the board when that corner is available.
2. The computer evaluates all possible positions. Then it executes the move with the highest evaluation value.

## Board evaluation
In the file, "evaluation.py", you can find the matrix below which defines each weight of the board.
  [
        [120, -20, 20,  5,  5,  20, -20, 120],
        [-20, -40, -5, -5, -5,  15, -40, -20],
        [ 20,  -5, 15,  3,  3,  15,  -5,  20],
        [  5,  -5,  3,  3,  3,   3,  -5,   5],
        [  5,  -5,  3,  3,  3,   3,  -5,   5],
        [ 20,  -5, 15,  3,  3,  15,  -5,  20],
        [-20, -40, -5, -5, -5,  15, -40, -20],
        [120, -20, 20,  5,  5,  20, -20, 120],
    ]
For example, if you put your piece in a corner, the evaluation of the board will be added 120.

## Japanese
リバーシ（オセロ）の対戦コンピューターです．
アルゴリズムは２つの基本ルールから成ります．
1. ボードの角のマス目に置けるとき，必ず置きます．
2. 次の考えられる手を打った後のボードの評価値を計算し，最も高い手を打ちます．

## Reference
othello.py by Daniel Connelly:
http://dhconnelly.com/paip-python/docs/paip/othello.html
