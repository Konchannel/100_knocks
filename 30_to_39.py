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
"""

import codecs
import MeCab
import re

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
        sahens.append(neko['base'])

print(sahens)

"""
34. 「AのB」
2つの名詞が「の」で連結されている名詞句を抽出せよ．
"""

print("\n===\n34\n===")
bridge_no_list = []
word1 = ""
word2 = ""

for neko in mecab_neko_dicts:
    if word1['pos'] != "名詞":
        continue
    elif word2 == "の":
        bridge_no_list.append(word1['base'] + word2['base'] + neko['base'])

    word1 = word2
    word2 = neko


"""
35. 名詞の連接
名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．
"""


"""
36. 単語の出現頻度
文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ．
"""


"""
37. 頻度上位10語
出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．
"""


"""
38. ヒストグラム
単語の出現頻度のヒストグラム（横軸に出現頻度，縦軸に出現頻度をとる単語の種類数を棒グラフで表したもの）を描け．
"""


"""
39. Zipfの法則
単語の出現頻度順位を横軸，その出現頻度を縦軸として，両対数グラフをプロットせよ．
"""

