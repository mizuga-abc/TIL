#文字列の文字数を調べる、length関数
print("文字列の文字数を調べる、length関数")
hello = "こんにちは"
print(len(hello))

#文字列の文字数を調べる,それに整数を足す。
print("#文字列の文字数を調べる,それに整数を足す。")
hello = "こんにちは"
print(len(hello)+100)


#何文字目から始まるのか調べる、「.find( )」メソッド
#find／rfindメソッドとindex／rindexメソッドの違いは、
#前者は文字列が見つからなければ-1を返し、後者は例外（エラー）を発生させる点にある。
#どちらも文字列の数を出すので、計算をすることもできる、　print(usi_find + 1)　　　みたいな・・

print("何文字目から始まるのか調べる、「.find( )」メソッド")
animal="鼠、牛、羊、馬"
usi_find=animal.find("牛")  #「.find( )」メソッドの引数は文字列にする
print(usi_find) #変数なので””はいらない、そのままprintに入れる。
print(usi_find + 1) #文字列の数を出すので、計算をすることもできる

test_find=animal.find("鶏")  #「.find( )」メソッドの引数は文字列にする
print(test_find) #findで見つからない場合は（-1）を返す。


#文字列のindexを調べる「.index()」メソッド
#「index」は「複数のデータの通し番号」を指す言葉
print("文字列のindexを調べる「.index()」メソッド")
animal="鼠、牛、羊、馬"
usi_find=animal.index("牛")  #「.index( )」メソッドの引数は文字列にする
print(usi_find) #変数なので””はいらない、そのままprintに入れる。

"""
test_find=animal.index("鶏")  #「.index( )」メソッドの引数は文字列にする
print(test_find) #indexで見つからない場合は,エラーを返す。(ここではコメントアウトしておく)
"""


#文字列の一部を入れ替れ変える、「.replace()」メソッド
print("文字列の一部を入れ替え変える、「.replace()」メソッド")
metamon = "メタモンはヒトカゲになった！"
print(metamon)
#文字を入れ替えてみる。
metamon = metamon.replace("ヒトカゲ","ゼニガメ")
print(metamon)
#文字列の中の該当する部分が全て入れ替わる動作
metamon = "メタモンはヒトカゲになった！　　メタモンはヒトカゲになった！"
print(metamon)
metamon = metamon.replace("ヒトカゲ","ゼニガメ")
print(metamon)

#特定の文字列を数える、「.count( )」メソッド
print("特定の文字列を数える、「.count( )」メソッド")
specific_str = "隣の客はよく柿食う客だ"
specific_str_mouth = specific_str.count("客")   #客の数を数えてみる,この場合は「2」を返す
print(specific_str_mouth)

specific_str_tarou = specific_str.count("太郎")   #いない文字の場合は「0」を返す
print(specific_str_tarou)