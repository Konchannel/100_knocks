"""
00. 文字列の逆順
文字列"stressed"の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．
==============================
point:
pythonのstr, tupleはイミュータブル(更新不可)なのでreversedが適用できない。
listに型変換してreversedを適用後、joinでstrに戻す実装をしていた。
しかしスライスの指定によって、逆順にprintしていくことでも実装可能だった。

スライスは[start:stop:step]で指定していく。stopに指定した場所は含まれないことに注意。
また、全体を指定する場合はstartとstopは省略可能。
"""

str00 = "stressed"
print(''.join(list(reversed(str00))))

# -Improvement
print(str00[::-1])

"""
01. 「パタトクカシーー」
「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．
==============================
point:
スライスの応用。
"""
patatoku = "パタトクカシーー"
str01 = ""

for index, string in enumerate(patatoku):
    if index % 2 == 0:
        str01 += string

print(str01)

# -Improvement
print(patatoku[::2])

"""
02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
"""
pato = "パトカー"
taku = "タクシー"
str02 = ""

for j in range(4):
    str02 += pato[j]
    str02 += taku[j]

print(str02)

"""
03. 円周率
"Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．
==============================
point:
ピリオドなど、正規表現でエスケープが必要な文字はなんとなくでいいから覚えておきたい
だいたいバックスラッシュを付けてエスケープする
"""
import re

pi_gemstone = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
pi_cut = re.sub("\.|,", "", pi_gemstone).split(" ")
py_list = []

for k in pi_cut:
    py_list.append(len(k))

print(py_list)

"""
04. 元素記号
"Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause.
 Arthur King Can."という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭に2文字を取り出し，
 取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．
 ==============================
point:
分割してゴミ(ピリオドなど)を取り除く処理に、先ほどは正規表現を使ったが
今回はsplit後にrstripを使用している。
余談だが、list型への要素追加はappend、dict型への要素追加はupdateで行う。
enumerateでindexも取得している設計のためlistからdictに変更も容易い。
"""

elements_gemstone = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause.　Arthur King Can."
get_only_one_numbers = {1, 5, 6, 7, 8, 9, 15, 16, 19}
elements_list = []

elements_splitted = elements_gemstone.split(" ")

for index, m in enumerate(elements_splitted):
    m = m.rstrip(".")
    if int(index + 1) in get_only_one_numbers:
        elements_list.append(m[0:1])
        continue
    else:
        elements_list.append(m[0:2])

print(elements_list)

"""
05. n-gram
与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，
"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．
==============================
point:
list(string)で、stringを1文字ずつにバラしたlistが生成される。
ちょっとだけエラーハンドリングもしててえらい。セキュアなコードですね(?)。
"""


def make_bi_gram(sentence, process_param):
    n_gram_list = []

    if process_param == "word":  # 単語bi-gram
        sentences = sentence.split(" ")
    elif process_param == "chara":  # 文字bi-gram
        sentences = list(sentence)
    else:
        return "The parameter cannot be accepted"

    for p in range(len(sentences) - 1):
        if sentences[p + 1]:
            n_gram_list.append(sentences[p] + sentences[p + 1])
    return n_gram_list


print(make_bi_gram("I am an NLPer", "word"))
print(make_bi_gram("I am an NLPer", "chara"))
print(make_bi_gram("I am an NLPer", "error"))

"""
06. 集合
"paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．
さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．
==============================
point:
標準ライブラリであるtypesにはunion, intersection, differenceのメソッドがある。
なんかあっけなかったので自前でも書いてみた。
"""
survey_target_str01 = "paraparaparadise"
survey_target_str02 = "paragraph"

X = set(make_bi_gram(survey_target_str01, "chara"))
Y = set(make_bi_gram(survey_target_str02, "chara"))

Unions = X.union(Y)
Intersections = X.intersection(Y)
Differences = X.difference(Y)

""" # メソッドを使わず自前で実装した場合
Unions = []
Intersections = []
Differences = []

for r in make_gram(survey_target_str01, "chara"):
    # process for make Unions
    if r not in Unions:
        Unions.append(r)
    for s in make_gram(survey_target_str02, "chara"):
        # process for make Unions
        if s not in Unions:
            Unions.append(s)

        # process for make Intersections
        if r == s and r not in Intersections:
            Intersections.append(r)

# process for make Differences
Differences = [x for x in Unions if x not in Intersections]
"""

print(Unions)
print(Intersections)
print(Differences)

print("se" in X)
print("se" in Y)

"""
07. テンプレートによる文生成
引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．さらに，x=12, y="気温", z=22.4として，実行結果を確認せよ．
"""

x = 12
y = "気温"
z = 22.4


def return_template_str(x, y, z):
    return "{}時の{}は{}".format(x, y, z)


print(return_template_str(x, y, z))

"""
08. 暗号文
与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．

英小文字ならば(219 - 文字コード)の文字に置換
その他の文字はそのまま出力
この関数を用い，英語のメッセージを暗号化・復号化せよ．
==============================
point:
asciiコード上で"a"は97、"z"は122である。
よって、足した219から英子文字のasciiコードを引くと、対応した英子文字に暗号化される。
(例えばaならz、bならy、cならx)
islower()は文字列が英子文字か判別するメソッド。
ordは文字をasciiコードに、chrはasciiコードを文字に変換するメソッド。
"""


def cipher(messages):
    cipher_messages = []

    for t in messages:
        if t.islower():
            cipher_messages.append(chr(219 - ord(t)))
        else:
            cipher_messages.append(t)

    return ''.join(cipher_messages)


encryption_str = cipher("At Coder-0123")
decryption_str = cipher(encryption_str)

print(encryption_str)
print(decryption_str)

"""
09. Typoglycemia
スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
ただし，長さが４以下の単語は並び替えないこととする．適当な英語の文（例えば"I couldn't believe that I could actually understand 
what I was reading : the phenomenal power of the human mind ."）を与え，その実行結果を確認せよ．
==============================
point:
random.sampleでは、抽選元となるリストから重複のないように指定個数ぶんだけ要素をランダムに取り出す。(そして出来た新しいリストを返す)
pythonのスライスは新しいリストを作るため、random.sampleの引数にスライスを使用することもできる。
"""

words_to_be_shuffle = "I couldn't believe that I could actually understand " \
                      "what I was reading : the phenomenal power of the human mind ."


def words_shuffle(words):
    import random

    word_list_to_be_shuffle = words.split(" ")
    shuffled_word_list = []

    for u in word_list_to_be_shuffle:
        if len(u) <= 4:
            shuffled_word_list.append(u)
        else:
            u_slice_shuffled = random.sample(u[1:-1], len(u[1:-1]))
            shuffled_word = u[0] + "".join(u_slice_shuffled) + u[-1]
            shuffled_word_list.append(shuffled_word)

    return " ".join(shuffled_word_list)


print(words_shuffle(words_to_be_shuffle))
