#sum( )関数、リストの数の合計を調べる
print("sum( )関数、リストの数の合計を調べる")
numbers_int = [1,2,3]
numbers_X = sum(numbers_int)
print(numbers_X)

#小数は間違えることあるので注意
print("小数は間違えることあるので注意、")
numbers_int = [1.1,1.1,1.1]
numbers_Y = sum(numbers_int)
print(numbers_Y) #結果が「3.3000000000000003」になる・・・



"""
「max( )」関数、「min( )」関数,「len( )」関数はリストでなくても使用できる。（整数の関数より）
"""

#「max( )」関数、リストの最大の数を調べる
print("「max( )」関数、リストの最大の数を調べる")
numbers_int = [1,2,3]
numbers_A = max(numbers_int)
print(numbers_A) #3が出力される。


#「min( )」関数、リストの最小の数を調べる
print("「min( )」関数、リストの最小の数を調べる")
numbers_int = [1,2,3]
numbers_B = min(numbers_int)
print(numbers_B) #3が出力される。


#「len( )」関数、リストの要素数
print("「len( )」関数、リストの要素数")
numbers_int = [122,222,322,422,500]
numbers_C = len(numbers_int)
print(numbers_C) #5が出力される。

#「len( )」関数は入ってるのが、文字と数字の混在でも要素数を返してくれる
print("「len( )」関数は入ってるのが、文字と数字の混在でも要素数を返してくれる")
numbers_int = ["犬",222,322]
numbers_D = len(numbers_int)
print(numbers_D) #3が出力される。


#「sorted( )」関数はリストを昇順に並び替え。
#「sorted」とは「整った」みたいな意味。（ソートみたいな）
print("sorted( )」関数はリストを昇順に並び替え。")
numbers_sort = [1222,322,3,4,500]
numbers_E = sorted(numbers_sort)
print(numbers_E) #[3, 4, 322, 500, 1222] が出力。

#「sorted()」は文字の並び替えも可能、なお漢字は五十音順に並び替えられるわけじゃない
print("「sorted()」は文字の並び替えも可能、なお漢字は五十音順に並び替えられるわけじゃない")
numbers_sort = ["ああ","あア","うう","うウ","い","雨"]
numbers_F = sorted(numbers_sort)
print(numbers_F) #['ああ', 'あア', 'い', 'うう', 'うウ', '雨'] が出力。
