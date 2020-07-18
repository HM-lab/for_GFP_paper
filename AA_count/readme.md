# AA_count.py

## 酵母のプロテオーム中のアミノ酸の出現頻度に関するbarplot

### csvファイル

* AA_count.csv
Swissprotデータベースに保存されている配列データから算出。全タンパク質について。

* AA_count_100000.csv
(Kulak et al., 2014)の発現量 (copy number) が100,000以上のものについて算出。

"""
- pro: probability. ランダムな場合の出現頻度
- num: number. 出現回数
- per: percentage. プロテオーム中の出現頻度
"""

### 算出

* pro
各アミノ酸をコードするコドン数を終始コドンを除く全コドン数で割ったものとして算出された (例えばシステインなら、2 / (64 - 3) ) 。

* per
num ÷ プロテオーム中の全アミノ酸数
