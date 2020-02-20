"""
hightemp.txtは，日本の最高気温の記録を「都道府県」「地点」「℃」「日」のタブ区切り形式で格納したファイルである．以下の処理を行うプログラムを作成し，hightemp.txtを入力ファイルとして実行せよ．さらに，同様の処理をUNIXコマンドでも実行し，プログラムの実行結果を確認せよ．
==============================
point:
windows機にて実行しているため、以下に登場するコマンドは実行できてません...つらたん、macbookro買お
"""

import codecs
temp_text = "./hightemp.txt"
with codecs.open(temp_text, 'r', 'utf-8') as ht:
    for line in ht:
        ...
        # print(line)

"""
10. 行数のカウント
行数をカウントせよ．確認にはwcコマンドを用いよ．
==============================
point:
ブラウザでhightemp.txtを開くと表示崩れが起きていたので一応utf-8指定で開いている。

Improvement:
長さを計るだけなら、readlinesでとったlistの長さを見ればいい。for文で回すだけ遅いかも。
"""

with codecs.open(temp_text, 'r', 'utf-8') as ht:
    num_line = 0
    for line in ht:
        num_line += 1
    print(num_line)

# Improvement

with codecs.open(temp_text, 'r', 'utf-8') as ht:
    print(len(ht.readlines()))

"""
11. タブをスペースに置換
タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．
==============================
point:
比較のため、置換後のテキストは別ファイルに保存している。

Improvement:
codecs.openモジュールを使ううまみは、python2でエンコードしたファイルを開くときらしい。
今回はうまみがなさそう。普通にopenでよさげ。
"""

with codecs.open(temp_text, 'r', 'utf-8') as ht:
    with codecs.open("./testfile.txt", 'w', 'utf-8') as test_text:
        for line in ht:
            test_text.write(line.replace('	', ' '))

# Improvement
with open(temp_text, encoding='utf-8') as tt:
    for line in tt:
        print(line.replace('	', ' '))

"""
12. 1列目をcol1.txtに，2列目をcol2.txtに保存
各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．
==============================
Improvement:
withの中にopen関数を複数入れることができるらしい。すごい。
それと、open関数で開こうとしたファイルがない場合作成し、ある場合は上書きする命令をmode='w'で実現できる。
引数名の指定が必要な分、codecs.openよりコードが長くなっちゃう。(処理時間は早いっぽい？)
"""

with codecs.open(temp_text, 'r', 'utf-8') as ht:
    with codecs.open("./col1.txt", 'w', 'utf-8') as col1:
        with codecs.open("./col2.txt", 'w', 'utf-8') as col2:
            for line in ht:
                words = line.split(' ')
                col1.write(words[0] + '\n')
                col2.write(words[1] + '\n')

# Improvement

with open(temp_text, encoding='utf-8') as ht, open("./col1_imp.txt", mode='w', encoding='utf-8') as col1_i,\
        open("./col2_imp.txt", mode='w', encoding='utf-8') as col2_i:
    for line in ht:
        words = line.split(' ')
        col1_i.write(words[0] + '\n')
        col2_i.write(words[1] + '\n')

"""
13. col1.txtとcol2.txtをマージ
12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを用いよ．
==============================
Improvement:
複数リストから同時に値を取得するzip関数を使ってより見やすくスマートに。
"""

with codecs.open("./col1.txt", 'r', 'utf-8') as col1:
    with codecs.open("./col2.txt", 'r', 'utf-8') as col2:
        with codecs.open("./merged_col1_and_col2.txt", 'w', 'utf-8') as merged:
            col1_list = col1.readlines()
            col2_list = col2.readlines()
            for i in range(len(col1_list)):
                split_col1 = col1_list[i].rstrip('\n')
                split_col2 = col2_list[i].rstrip('\n')
                merged.write(split_col1 + ' ' + split_col2 + '\n')

# Improvement

with open("merged_imp.txt", mode='w', encoding='utf-8') as m_i,\
        open("./col1_imp.txt", mode='r', encoding='utf-8') as col1_i,\
        open("./col2_imp.txt", mode='r', encoding='utf-8') as col2_i:
    for one_i, two_i in zip(col1_i, col2_i):
        m_i.write(one_i.rstrip() + "\t" + two_i)

"""
14. 先頭からN行を出力
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．
==============================
Improvement:
ループを使うなら、breakのタイミングも考えて設置したい。
"""
print("\n先頭から何行欲しいですか？:", end="")
get_lines_num = int(input())

with codecs.open(temp_text, 'r', 'utf-8') as ht:
    for index, line in enumerate(ht):
        if get_lines_num > index:
            print(line.rstrip('\n'))

# Improvement

with codecs.open(temp_text, 'r', 'utf-8') as ht:
    for index, line in enumerate(ht):
        if get_lines_num > index:
            print(line.rstrip('\n'))
        else:
            break

"""
15. 末尾のN行を出力
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．
==============================
point:
いい加減に、hightempを読み込む処理をメソッドに切り出した、もっと早くやればよかった。
Improvement:
全て読み込んで該当の部分だけprintするよりも、該当の部分だけ読み込んでprintしたほうが早い。スライスってべんりだなぁ
"""


def read_hightemp():
    with codecs.open(temp_text, 'r', 'utf-8') as ht:
        ht_lines = ht.readlines()
        return ht_lines


print("\n末尾から何行欲しいですか？:", end="")
n = int(input())
ht_lines = read_hightemp()


for index, ht_line in enumerate(ht_lines):
    if 0 >= len(ht_lines) - index - n:
        print(ht_line.rstrip('\n'))

# Improvement
if n > 0:
    for ht_line in ht_lines[-n:]:
        print(ht_line.rstrip('\n'))

"""
16. ファイルをN分割する
自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．
==============================
Improvement-01:
スライス指定ではIndexErrorが発生しないことを利用した実装
Improvement-02:
Errorも出ないように実装した。やや冗長。
Improvement-03:
シンプルにはなったけど、計算量は増えたっぽい。つらいー

/ と % をうまく使って実現できそうだけども、それは今後の課題とする。
"""

print("\n何行ずつに分けたいですか？", end="")
split_lines_num = int(input())
ht_cluster = []
splitted_line = ''

with codecs.open(temp_text, 'r', 'utf-8') as ht:
    ht_cluster = ht.read().split('\n')
    for line_index, ht_line in enumerate(ht_cluster):
        splitted_line += ht_line + '\n'
        if (line_index + 1) % split_lines_num == 0:
            print(splitted_line)
            splitted_line = ''
    if splitted_line is not '':
        print(splitted_line)

# Improvement-01

print("\n何ブロックに分けたいですか？", end="")
split_group_num = int(input())

if split_group_num > 0:
    with open(temp_text, mode="r", encoding="utf-8") as tt:
        import math

        tt_main = tt.readlines()
        total_range = len(tt_main)
        one_group_num = math.ceil(total_range / split_group_num)

        for split_index in range(split_group_num):
            slice_start = one_group_num * split_index
            for i in tt_main[slice_start: slice_start + one_group_num]:
                print(i, end="")
            print("")

# Improvement-02
print("")

if split_group_num > 0:
    with open(temp_text, mode="r", encoding="utf-8") as tt:
        import math

        tt_main = tt.readlines()
        total_range = len(tt_main)
        one_group_num = math.ceil(total_range / split_group_num)

        for split_index in range(split_group_num):
            if total_range / one_group_num:
                slice_start = one_group_num * split_index
                for i in tt_main[slice_start: slice_start + one_group_num]:
                    print(i, end="")
                print("")
            else:
                for i in tt_main[slice_start: slice_start + total_range % one_group_num]:
                    print(i, end="")

# Improvement-03
print("")

if split_group_num > 0:
    with open(temp_text, mode="r", encoding="utf-8") as tt:
        import math

        tt_main = tt.readlines()
        total_range = len(tt_main)
        one_group_num = math.ceil(total_range / split_group_num)

        for tt_index, tt_value in enumerate(tt_main, start=1):
            print(tt_value.rstrip())
            if tt_index % one_group_num == 0:
                print("")
        print("")

"""
17. １列目の文字列の異なり
1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはsort, uniqコマンドを用いよ．
==============================
Improvement:
そもそも、問題文の読み間違えがあった。一列目を一行目に空目していた。こういうとこ慎重にいかなきゃなーと毎回思ってできてない。次こそは！
set使うのは変わらず。split()の時点でlistが返却されるのがわかるので、いきなりスライス使いだせる。素敵記法に感じた。
"""

# ht_lines = read_hightemp()

for ht_line in ht_lines:
    print(set(ht_line))
    print()
    break

# Improvement

ken_unique = set()

for ht_line in ht_lines:
    ken_unique.add(ht_line.split()[0])

print(ken_unique)

"""
18. 各行を3コラム目の数値の降順にソート
各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．
==============================
Improvement:
split()で分割区切りになるのは、タブやスペースなので、正規表現せずともよかった。
問題文の
> 注意: 各行の内容は変更せずに並び替えよ
っていうのは、 /n もとっちゃだめってことなんだろうか。なーんか不格好だけど指定されてるので変にいじらないようにする。
"""

print()
# ht_lines = read_hightemp()

ht_columns = []
import re

for index, ht in enumerate(ht_lines):
    ht_columns.append(list(re.split('   | |\t', ht.rstrip())))

print(sorted(ht_columns, key=lambda ht_val: ht_val[2]))
print()

# Improvement

ht_sort = ht_lines
print(sorted(ht_sort, key=lambda ht_val: ht_val.split()[2], reverse=True))


"""
19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．確認にはcut, uniq, sortコマンドを用いよ．
==============================
Improvement:
問題の読み違えがひどかった。県の出現数の降順、なのに各行の文字の頻出数で出してた。それはそれで難しいぞ。
使うモジュールは同じでいけたのでちょっと得した気持ち。
"""

import collections

for ht_line in ht_lines:
    ht_counter = collections.Counter(ht_line)
    values, counts = zip(*ht_counter.most_common())
    print(values)

# Improvement

kens = []

for ht_line in ht_lines:
    kens.append(ht_line.split()[0])

print(collections.Counter(kens).most_common())

