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
"""

with codecs.open(temp_text, 'r', 'utf-8') as ht:
    num_line = 0
    for line in ht:
        num_line += 1
    print(num_line)

"""
11. タブをスペースに置換
タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．
==============================
point:
比較のため、置換後のテキストは別ファイルに保存している。
"""

with codecs.open(temp_text, 'r', 'utf-8') as ht:
    with codecs.open("./testfile.txt", 'w', 'utf-8') as test_text:
        for line in ht:
            test_text.write(line.replace('	', ' '))

"""
12. 1列目をcol1.txtに，2列目をcol2.txtに保存
各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．
"""

with codecs.open(temp_text, 'r', 'utf-8') as ht:
    with codecs.open("./col1.txt", 'w', 'utf-8') as col1:
        with codecs.open("./col2.txt", 'w', 'utf-8') as col2:
            for line in ht:
                words = line.split('	')
                col1.write(words[0] + '\n')
                col2.write(words[1] + '\n')

"""
13. col1.txtとcol2.txtをマージ
12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを用いよ．
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

"""
14. 先頭からN行を出力
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．
"""
print("\n先頭から何行欲しいですか？:", end="")
get_lines_num = int(input())

with codecs.open(temp_text, 'r', 'utf-8') as ht:
    for index, line in enumerate(ht):
        if get_lines_num > index:
            print(line.rstrip('\n'))

"""
15. 末尾のN行を出力
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．
==============================
point:
いい加減に、hightempを読み込む処理をメソッドに切り出した、もっと早くやればよかった。
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


"""
16. ファイルをN分割する
自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．
"""

print("\n何行ずつに分けたいですか？", end="")
split_group_num = int(input())
ht_cluster = []
splitted_line = ''

with codecs.open(temp_text, 'r', 'utf-8') as ht:
    ht_cluster = ht.read().split('\n')
    for line_index, ht_line in enumerate(ht_cluster):
        splitted_line += ht_line + '\n'
        if (line_index + 1) % split_group_num == 0:
            print(splitted_line)
            splitted_line = ''
    if splitted_line is not '':
        print(splitted_line)


"""
17. １列目の文字列の異なり
1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはsort, uniqコマンドを用いよ．
"""

ht_lines = read_hightemp()

for ht_line in ht_lines:
    print(set(ht_line))
    break

"""
18. 各行を3コラム目の数値の降順にソート
各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．
"""


"""
19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．確認にはcut, uniq, sortコマンドを用いよ．
"""