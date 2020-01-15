"""
00. 文字列の逆順
文字列"stressed"の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．
==============================
point:
pythonのstr, tupleはイミュータブル(更新不可)なのでreversedが適用できない。
listに型変換してreversedを適用後、joinでstrに戻す。
"""

str01 = "stressed"
print(''.join(list(reversed(str01))))
