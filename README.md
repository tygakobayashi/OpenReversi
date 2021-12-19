# OpenReversi
The algorithm for Reversi has 2 principles.
One is to put your piece in a corner whenever it's available.
The second is to evaluate all possibilities based on the weight for each place on the board.
And then you choose the move which has the highest evaluation.

## Reference
othello.py by Daniel Connelly:
http://dhconnelly.com/paip-python/docs/paip/othello.html

# NPC for リバーシ，オセロ
アルゴリズムは２つの基本ルールから成ります．
1つ目は，タイルはコーナーに置けるとき，必ず置きます．
2つ目は，ボード上のマス目に重みを設定し，それに従った評価値を計算します．コンピューターは置ける手すべての評価値を計算し，
そのなかから最も評価値の高い選択をします．
