"""
夏目漱石の小説『吾輩は猫である』の文章（neko.txt）をMeCabを使って形態素解析し，その結果をneko.txt.mecabというファイルに保存せよ．このファイルを用いて，以下の問に対応するプログラムを実装せよ．

なお，問題37, 38, 39はmatplotlibもしくはGnuplotを用いるとよい．

30. 形態素解析結果の読み込み
形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．ただし，各形態素は表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をキーとするマッピング型に格納し，1文を形態素（マッピング型）のリストとして表現せよ．第4章の残りの問題では，ここで作ったプログラムを活用せよ．
"""

import codecs
import MeCab
import re

print("\n===\n30\n===")

with codecs.open("./neko.txt", 'r', 'utf-8') as neko_txt,\
    codecs.open("./neko.txt.mecab", 'w', 'utf-8') as mecab_nekos:
    mecab_nekos.write(MeCab.Tagger().parse(neko_txt.read()))

with codecs.open("./neko.txt.mecab", 'r', 'utf-8') as mecab_nekos:
    mecab_neko_dicts = []

    for mecab_neko in mecab_nekos:
        split_mecab = re.split(",|\s", mecab_neko)
        if split_mecab[0] == "":
            pass
        else:
            mecab_neko_dict = {}
            mecab_neko_dict['surface'] = split_mecab[0]



"""
31. 動詞
動詞の表層形をすべて抽出せよ．
"""

"""
32. 動詞の原形
動詞の原形をすべて抽出せよ．
"""


"""
33. サ変名詞
サ変接続の名詞をすべて抽出せよ．
"""


"""
34. 「AのB」
2つの名詞が「の」で連結されている名詞句を抽出せよ．
"""


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

