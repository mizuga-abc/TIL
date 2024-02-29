# tailコマンド
ログを確認するときに使用する。<br>
最終行から数行を表示させる。<br>
※head というコマンドは頭からの行数の逆バージョン。<br>
#### ログの表示から抜けるには「ctrl」+「c」

事前の準備としてVMでWebサーバーの検証をしたので<br>
そのファイルを見てみる。<br>
アクセス権ないと実行できない？？
>sudo tail /var/log/messages

コマンド実行例
![Alt text](<スクリーンショット 2024-02-29 17.41.49.png>)

![Alt text](<スクリーンショット 2024-02-29 17.43.56.png>)

- -n　オプション<br>
指定した行数遡れる

>sudo tail -n 5 /var/log/messages

コマンド実行例
![Alt text](<スクリーンショット 2024-02-29 17.52.10.png>)

- -f または -F　のオプションをよく使用するらしい<br>
>sudo tail -f /var/log/messages

- エラーログの絞り込みで、grepコマンドをあわせる例<br>
>sudo tail -f /var/log/messages | grep error