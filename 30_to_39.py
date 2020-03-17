"""
夏目漱石の小説『吾輩は猫である』の文章（neko.txt）をMeCabを使って形態素解析し，その結果をneko.txt.mecabというファイルに保存せよ．このファイルを用いて，以下の問に対応するプログラムを実装せよ．

なお，問題37, 38, 39はmatplotlibもしくはGnuplotを用いるとよい．

30. 形態素解析結果の読み込み
形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．ただし，各形態素は表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をキーとするマッピング型に格納し，1文を形態素（マッピング型）のリストとして表現せよ．第4章の残りの問題では，ここで作ったプログラムを活用せよ．
==============================
point:
本家サイトのneko.txtは文字化けしていたため、青空文庫より直接全文引っ張ってきた。
正直これが面倒だった。。。

途中で入る if split_mecab[0] == "" or len(split_mecab) < 8: のif文は、
['', '']
['EOS', '']
['', '記号', '一般', '*', '*', '*', '*', '*', '']
['', '', '記号', '空白', '*', '*', '*', '*', '', '', '', '', '', '', '']
を除外する為。

mecabのエラーについて:
辞書をいじろうとしたときに、mecabがRunTimeErrorしか吐かなくなったことがあった。
インストールファイルからmecabを削除し再インストールしたり、環境変数を設定しなおしたり、PyCharmのインポート先を指定しなおしたら治った。
今後mecab自体をいじる場合はよく注意して行うべし。
"""

import codecs
import MeCab
import re
from collections import Counter
import matplotlib.pyplot as plt
import japanize_matplotlib

print("\n===\n30\n===")

with codecs.open("./neko.txt", 'r', 'utf-8') as neko_txt,\
    codecs.open("./neko.txt.mecab", 'w', 'utf-8') as mecab_nekos:
    mecab_nekos.write(MeCab.Tagger().parse(neko_txt.read()))

mecab_neko_dicts = []
with codecs.open("./neko.txt.mecab", 'r', 'utf-8') as mecab_nekos:

    for mecab_neko in mecab_nekos:
        split_mecab = re.split(",|\s", mecab_neko)

        if split_mecab[0] == "" or len(split_mecab) < 8:
            pass
        else:
            mecab_neko_dict = {'surface': split_mecab[0],
                               'base': split_mecab[7],
                               'pos': split_mecab[1],
                               'pos1': split_mecab[2]}

            mecab_neko_dicts.append(mecab_neko_dict)


    """
    結果表示。膨大になるため、10行だけ表示する。
    """
    for index, neko in enumerate(mecab_neko_dicts):
        if index > 10:
            break
        else:
            print(neko)

"""
31. 動詞
動詞の表層形をすべて抽出せよ．
"""

print("\n===\n31\n===")
dousis = []

for neko in mecab_neko_dicts:
    if neko['pos'] == '動詞':
        dousis.append(neko['surface'])

print(dousis)

"""
32. 動詞の原形
動詞の原形をすべて抽出せよ．
"""

print("\n===\n32\n===")
dousis = []

for neko in mecab_neko_dicts:
    if neko['pos'] == '動詞':
        dousis.append(neko['base'])

print(dousis)

"""
33. サ変名詞
サ変接続の名詞をすべて抽出せよ．
"""

print("\n===\n33\n===")
sahens = []

for neko in mecab_neko_dicts:
    if neko['pos'] == '名詞' and neko['pos1'] == 'サ変接続':
        sahens.append(neko['surface'])

print(sahens)

"""
34. 「AのB」
2つの名詞が「の」で連結されている名詞句を抽出せよ．
"""

print("\n===\n34\n===")
bridge_no_list = []
word1 = {}
word2 = {}

for neko in mecab_neko_dicts:
    if word1.get('pos') == "名詞" and word2.get('base') == "の" and neko['pos'] == "名詞":
        bridge_no_list.append(word1['surface'] + word2['surface'] + neko['surface'])

    word1 = word2
    word2 = neko

print(bridge_no_list)

"""
35. 名詞の連接
名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．
==============================
point:
正直、このあたりは辞書の精度的な問題でうまくとれていない。
また、本文を引用した際にルビも文章の一部として含まれてしまったため、正確なカウントが出来ていない。
この点の修正は今後の課題である。
"""

print("\n===\n35\n===")

max_meisis = []
max_meisis_range = 0
tmp_meisis = []
tmp_meisis_range = 0

for neko in mecab_neko_dicts:

    # 名詞であればtmpに追加
    if neko['pos'] == "名詞":
        tmp_meisis_range += 1
        tmp_meisis.append(neko['surface'])
    # 名詞の連続が終わって、連続値が最大値より小さかった場合
    elif max_meisis_range > tmp_meisis_range:
        tmp_meisis = []
        tmp_meisis_range = 0
    # 名詞の連続が終わって、連続値が最大値と同じだった場合、それをmaxに追加
    elif max_meisis_range == tmp_meisis_range:
        max_meisis.append(["".join(tmp_meisis)])
        tmp_meisis = []
        tmp_meisis_range = 0
    # 名詞の連続が終わって、連続値が最大値より大きかった場合、それをmaxに上書き
    elif max_meisis_range < tmp_meisis_range:
        max_meisis = ["".join(tmp_meisis)]
        max_meisis_range = tmp_meisis_range
        tmp_meisis = []
        tmp_meisis_range = 0
    # 名詞以外はスルー
    else:
        continue

print(max_meisis)
print(max_meisis_range)

"""
36. 単語の出現頻度
文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ．
==============================
point:
Counterにstrを渡すと、各文字にバラされて、文字の出現頻度が取れる。
今回は単語で渡したかったため、[]で囲んで、要素1のlistとして渡している。
"""

print("\n===\n36\n===")
words = Counter()

for neko in mecab_neko_dicts:
    words.update([neko['surface']])

print(words.most_common())

"""
37. 頻度上位10語
出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．
==============================
point:
matplotlibの日本語対応は、japanize_matplotlibをインポートすることでこなしている。
出力結果は"result_imgs/37.PNG"に保存してあるのでそちらから。
"""

print("\n===\n37\n===")

words_top10, words_count = zip(*words.most_common(10))

plt.bar(words_top10, words_count)
plt.grid(axis='y')
plt.show()

"""
38. ヒストグラム
単語の出現頻度のヒストグラム（横軸に出現頻度，縦軸に出現頻度をとる単語の種類数を棒グラフで表したもの）を描け．
==============================
point:
全単語をカウントすると、1度しか出ない単語が多すぎて他グラフが極小で見えない。
そのため、今回は1~10回登場した単語のみを表示している。
"""

print("\n===\n38\n===")

plt.hist(words.values(), bins=10, range=(1, 10.1), rwidth=0.9)
plt.xlim(xmin=1, xmax=10)  # 左右端の空白を詰める
plt.show()

print(Counter(words.values()).most_common())

"""
39. Zipfの法則
単語の出現頻度順位を横軸，その出現頻度を縦軸として，両対数グラフをプロットせよ．
"""

