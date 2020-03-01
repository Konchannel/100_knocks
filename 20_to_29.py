"""
Wikipediaの記事を以下のフォーマットで書き出したファイルjawiki-country.json.gzがある．

1行に1記事の情報がJSON形式で格納される
各行には記事名が"title"キーに，記事本文が"text"キーの辞書オブジェクトに格納され，そのオブジェクトがJSON形式で書き出される
ファイル全体はgzipで圧縮される
以下の処理を行うプログラムを作成せよ．

20. JSONデータの読み込み
Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．問題21-29では，ここで抽出した記事本文に対して実行せよ．
==============================
Point:
Jsonの扱いに関しては知識が無かったため、下書き無しで勉強していくことにする。
gzip.openのmode引数は、何をするか（読み込み、上書きなど）とモード（バイナリ、テキスト）によって変わる。
ちなみにrtは読み込み+テキストモード。
"""

import gzip
import json
import re
import math

with gzip.open("./jawiki-country.json.gz", mode="rt", encoding="utf-8") as jawiki_text:
    for line in jawiki_text:
        data_json = json.loads(line)
        if data_json['title'] == 'イギリス':
            print(data_json['text'])
            base_lines = data_json['text']  # これ以降の問題で扱いやすくするため
            break

"""
21. カテゴリ名を含む行を抽出
記事中でカテゴリ名を宣言している行を抽出せよ．
==============================
Improvement:
正規表現で書いてみたらなんとなく理解できた。書いた後読み返してみたが直感的でないのであまり好きな記法ではない。
でもできることが多いため、他のコードをキレイに保った短いコードが書けるんだと思っている。

それと、リスト内法表記でprintしてみた。1行で済むのでいいね。ただこれも好きとはいえない。やっぱり直感的に理解できるコードが好きだ。
"""
print("\n===\n21\n===")

for base_line in base_lines.split():
    if 'Category:' in base_line:
        print(base_line)

# Improvement

print("\n===\n21 -Improvement\n===")
pattern21 = re.compile('^(.*\[\[Category:.*\]\].*)$', re.MULTILINE)
[print(x) for x in pattern21.findall(base_lines)]

"""
22. カテゴリ名の抽出
記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．
==============================
Point:
正規表現ほんと難しいので参考コードほぼまんまで書いてしまった。
この章が終わるまでにマスターするぞ！ひとまず1周書いてみてから正規表現の書き方でもう1週するぞ！！

Improvement:
非貪欲マッチというものを覚えた。キャプチャ対象外の文字列も理解したので、出来る幅がかなり広かった！
"""

print("\n===\n22\n===")

for base_line in base_lines.split():
    if 'Category:' in base_line:
        print(re.sub("\[\[Category:|]]|\|\*", "", base_line))

# Improvement

print("\n===\n22 -Improvement\n===")
pattern22 = re.compile('^.*\[\[Category:(.*?)(?:\|.*)?\]\].*$', re.MULTILINE)
[print(x) for x in pattern22.findall(base_lines)]

"""
23. セクション構造
記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ．
==============================
Point:
コードで書くとアホほど汚くなりそうだったので正規表現を調べながら書いた。
後方参照というものを知った。前にマッチしたものと同じパターンを使えるとのこと。ただし1始まりな点に注意が必要。
"""

print("\n===\n23\n===")

repattern = re.compile(r'^(={2,})\s*(.+?)\s*\1.*$', re.MULTILINE + re.VERBOSE)
results23 = repattern.findall(base_lines)
for line in results23:
    level = len(line[0]) - 1
    print('{indent}{sect}({level})'.format(
        indent='\t' * (level - 1), sect=line[1], level=level))

"""
24. ファイル参照の抽出
記事から参照されているメディアファイルをすべて抜き出せ．
==============================
Point:
stripは空白区切りで複数文字列の除去ができる。知らなかった。

Improvement:
今度は独力で正規表現を書いてみた。キレイな記述が出来たと思う。
非貪欲マッチの重要性をひしひしと感じることができた。

Improvement 02:
めっちゃくちゃキレイ。正規表現の美しさを垣間見た。
さっき自分で書いたコードから無駄をそぎ落としたミニマルなコード。読みやすく直感的。はーすげぇ。
"""

print("\n===\n24\n===")

for base_line in base_lines.split('\n'):
    if 'File:' in base_line or 'ファイル:' in base_line:
        print(base_line.split(':')[1].split('|')[0].lstrip('[[ File ファイル'))

# Improvement

print("\n===\n24 -Improvement\n===")
pattern24 = re.compile('^.*?(?:File:|ファイル:)(.*?)\|.*$', re.MULTILINE)
[print(x) for x in pattern24.findall(base_lines)]

# Improvement 02

print("\n===\n24 -Improvement 02\n===")
pattern24 = re.compile('(?:File|ファイル):(.+?)\|')
[print(x) for x in pattern24.findall(base_lines)]

"""
25. テンプレートの抽出
記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ．
==============================
Point:
split使いすぎ問題。'{{基礎情報 国'　から　'}}\n'　までを取ってくるうまいやり方が浮かばなかった。
こういう時にこそ正規表現が役立つんだなぁと思う。

Improvement:
肯定の先読みという指定方法を学んだ。(?=hoge)で指定すると、hogeの前までで終了してくれてhogeは消費されない(次の指定はじまりとして使える)もの。
"""

print("\n===\n25\n===")
dict_25 = {}

base_line = base_lines.split('{{基礎情報 国')[1].split('}}\n')[0]

split_lines = base_line.split('\n|')
for n in split_lines:
    m = n.split(' = ')
    if len(m) == 2:
        dict_25[m[0]] = m[1]

for k, L in dict_25.items():
    print('{0} : {1}'.format(k, L))

# Improvement

print("\n===\n25 -Improvement\n===")
pattern25 = re.compile('\{\{基礎情報 国\n(.*?)\}\}\n', re.MULTILINE + re.DOTALL)
capture_range25 = pattern25.findall(base_lines)

capture25 = re.compile('\|(.+?)\s=\s(.+?)(?=\n\|)|(?=\n$)', re.MULTILINE + re.DOTALL)
word_list25 = capture25.findall(capture_range25[0])

dict_25 = {}

for field in word_list25:
    dict_25[field[0]] = field[1]

[print(x + ' : ' + y) for x, y in dict_25.items()]

"""
26. 強調マークアップの除去
25の処理時に，テンプレートの値からMediaWikiの強調マークアップ（弱い強調，強調，強い強調のすべて）を除去してテキストに変換せよ（参考: マークアップ早見表）．
"""



"""
27. 内部リンクの除去
26の処理に加えて，テンプレートの値からMediaWikiの内部リンクマークアップを除去し，テキストに変換せよ（参考: マークアップ早見表）．
"""



"""
28. MediaWikiマークアップの除去
27の処理に加えて，テンプレートの値からMediaWikiマークアップを可能な限り除去し，国の基本情報を整形せよ．
"""



"""
29. 国旗画像のURLを取得する
テンプレートの内容を利用し，国旗画像のURLを取得せよ．（ヒント: MediaWiki APIのimageinfoを呼び出して，ファイル参照をURLに変換すればよい）
"""
