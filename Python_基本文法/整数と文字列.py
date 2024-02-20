#計算と文字
print("計算と文字の結合")
print(1 + 1)
print("1" + "1")

#string関数で整数を文字にする
print("string関数で整数を文字にする")
print(str(100))


#計算結果を文字列にする
print("計算結果を文字列にする")
x=str(100*100)
print(x)

#integer関数で文字列を整数にする
print("integer関数で文字列を整数にする")
print(int("100"))

#結合した文字列を整数にする
print("結合した文字列を整数にする")
a=int("11"+"11")
print(a)

#文字列を整数にして、足し算
print("文字列を整数にして、足し算")
print(int("22")+22)

#int( )」の中で文字列の間に+があった場合、先に文字列の結合される、そのあとintで整数へ変換される
print("int( )」の中で文字列の間に+があった場合、先に文字列の結合される、そのあとintで整数へ変換される")
print(int("1" + "1"))

#ーーーーーーーーーーーーーーーーーーーーーーーーー
#変数の計算と結合を使いこなす
print("変数の計算と結合を使いこなす")

metamon=10
kabigon=1

pokemon=str(metamon+kabigon)
print(pokemon+"匹")

#別の例
print("別の例")
metamon=10
kabigon=1
print(str(metamon+kabigon)+"匹")

#型を明示的に書くことでわかりやすくなる
print("型を明示的に書くことでわかりやすくなる")


#（型を書いた）変数の計算と結合を使いこなす
print("（型を書いた）変数の計算と結合を使いこなす")

metamon_int=10
kabigon_int=1

pokemon_str=str(metamon_int+kabigon_int)
print(pokemon_str+"匹")

#（型を書いた）別の例
print("（型を書いた）別の例")
metamon_int=10
kabigon_int=1
unit_str="匹"
print(str(metamon_int+kabigon_int)+unit_str)

#ーーーーーーーーーーーーーーーーーーーーーーーーー


