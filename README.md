# SlidingPuzzle-Solver

## 遊びたい
python3 play.py  
列数，行数を入力したら始まります．  
ピースを動かす方向をLRUDで指定してプレイを進めて下さい．  
空きマスの右のピースを左に動かしたいとき，押すボタンはLです．  
途中辛くなったらsolve.pyを起動してクリアまで動かしてみればいいんじゃないでしょうか  


## 解かせたい  
python3 solve.py  
入力例に従って盤面を入力して下さい．  
A-starアルゴリズムが走ります．ヒューリスティック関数は現在の盤面の各ピースの正解位置までのマンハッタン距離の総和です．  
このヒューリスティック関数は許容的な評価関数ではないので，必ずしも最小の手数での攻略にはなりません．  


4 * 4の盤面で1分くらいかかるかと思います．  
Python重いですね．なんでPythonで書いたんだろ  
