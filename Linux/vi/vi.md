# viコマンド
Linuxのテキストエディタ。

事前の準備としてVMでWebサーバーの検証をしたので<br>
そのファイルを見てみる。

/var/www/html  のindex.htmlファイルを編集してみる。
ファイルをviで編集する。<br>
編集できる権限、例えば管理者権限でないとファイルの保存ができない

- ファイルの編集できる<br>
>sudo vi ファイルのパス

コマンド実行例
![Alt text](<スクリーンショット 2024-02-29 17.25.46.png>)

中が見れて編集できる。
![Alt text](<スクリーンショット 2024-02-29 17.28.14.png>)

#### ファイル内に文字を書いて、保存「:wq」<br>
#### ※なお、保存しないで抜ける際は「:q!」