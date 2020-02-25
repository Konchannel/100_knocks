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
"""
print("\n===\n21\n===")

for base_line in base_lines.split():
    if 'Category:' in base_line:
        print(base_line)

"""
22. カテゴリ名の抽出
記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．
==============================
Point:
正規表現ほんと難しいので参考コードほぼまんまで書いてしまった。
この章が終わるまでにマスターするぞ！
"""

print("\n===\n22\n===")

for base_line in base_lines.split():
    if 'Category:' in base_line:
        print(re.sub("\[\[Category:|]]|\|\*", "", base_line))

"""
23. セクション構造
記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ．
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
"""

print("\n===\n24\n===")

for base_line in base_lines.split('\n'):
    if 'File:' in base_line or 'ファイル:' in base_line:
        print(base_line.split(':')[1].split('|')[0].lstrip('[[ File ファイル'))

"""
25. テンプレートの抽出
記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ．
"""



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
