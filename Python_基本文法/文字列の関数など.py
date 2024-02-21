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
#文字を入れ替えてみる。.replace("","")左の引数を右に入れ替え。
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


#スライスの動作。文字列から指定の数の文字を取り出す
print("スライスの動作。文字列から指定の数の文字を取り出す")
test_str = "あいうえお"
first_str = test_str[0] #１文字目を抜き出してみる
print(first_str)
secound_str = test_str[2] #3文字目を抜き出してみる
print(secound_str)

#スライスの動作。文字列から指定の数の文字を取り出す、変数に代入された整数を[]内に入力もできる例
print("スライスの動作。文字列から指定の数の文字を取り出す、変数に代入された整数を[]内に入力もできる例")
x = 4
test_str = "あいうえお"
fifth_str = test_str[x] #xに入れた整数の5を指定する
print(fifth_str)


#スライスの動作。文字列の後ろから指定の数の文字を取り出す
#マイナスの場合はそのまま後ろから1つ目、2つ目と数える
#動作的には前２つの例と同じように動かせる。
print("スライスの動作。文字列の後ろから指定の数の文字を取り出す")
y = -1
test_str = "あいうえお"
fifth_str = test_str[y] #yに入れた整数の-1を指定する
print(fifth_str)

#文字列の途中まで取り出す、スライスの動作の応用みたいな感じ、例[:1]のように
print("文字列の途中まで取り出す、スライスの動作の応用みたいな感じ、例[:1]のように")
test_str = "かきくけこ"
extract_str = test_str[:3] #3文字目までを抜き出してみる,///この時は0,1,2,3という数え方ではない。///
print(extract_str)

#文字列後ろから-1の文字を取り除いた文字列を抽出する、この場合は「かきくけ」まで。
print("文字列後ろから-1の文字を取り除いた文字列を抽出する、この場合は「かきくけ」まで。")
pull_out_str = test_str[:-1] #文字列後ろから-1の文字を取り除いた文字列を抽出する、この場合は「かきくけ」まで。
print(pull_out_str)


#指定の文字列を除外して途中から抜き出す。[2:]のように書く
print("指定の文字列を除外して途中から抜き出す。[2:]のように書く")
test_str = "さしすせそ"
extract_str = test_str[2:] #前から2文字目までを除外して抜き出してみる,///この時は0,1,2,3という数え方ではない。///
print(extract_str)

#負の整数を入力して、文字列の後ろから指定の文字列の数**だけを**抜き出す。[-2:]のように書く
print("負の整数を入力して、文字列の後ろから指定の文字列の数**だけを**抜き出す。[-2:]のように書く")
test_str = "さしすせそ"
extract_str = test_str[-2:] #この時の表示は「せそ」になる。
print(extract_str)

#文字列の途中を取り出す。
#[:]の左に整数を入力すると、その数だけ文字を飛ばす。
#[:]の右に整数を入力すると、その数までの指定になる。

print("文字列の途中を取り出す。")
test_str = "あああメタモンあああ"
metamon_str = test_str[3:7] #メタモンという文字を取り出す。///この時は0,1,2,3という数え方ではない。///
print(metamon_str)


#[:]の左に負の整数を入力すると、文字列の最後から-の整数の分がスタートになる、(-何番目がスタート)
#[:]の右に負の整数を入力すると、文字列の最後から-の整数が取り除かれる。(-何番目が取り除かれる)

test_str = "あああメタモンあああ"
metamon_str = test_str[-7:-3] #-の数を使ってメタモンという文字を取り出す。///この時は0,1,2,3という数え方ではない。///
print(metamon_str)
