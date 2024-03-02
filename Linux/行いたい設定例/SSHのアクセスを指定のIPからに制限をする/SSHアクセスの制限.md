# SSHアクセスの制限

２つやり方がある？

#### hosts.allow|deny の書式を使用する方法.

**TCP Wrapperが廃止されたのでCentOS7までらしい。**  
TCP Wrapperについて  
https://e-words.jp/w/TCP_wrapper.html  
  
書式の参考  
https://blog.katsubemakito.net/linux/sshd-ipaddress-check#%E6%B3%A8%E6%84%8F%E7%82%B9

#### ファイアウォール（firewalld）で制限をかける方法

https://w.atwiki.jp/sanosoft/pages/150.html

>SSHでのログインに対してIPアドレスでの制限をかけます。  
>※CentOS 8では、TCP Wrapperが廃止されたため、
>「/etc/hosts.allow」、「/etc/hosts.deny」が使用できません。  

https://blog.netandfield.com/shar/2021/09/almalinux-ssh-ip.html

>AlmaLinux 8.4 は、CentOS 8 の互換 OS だ。
>そのため、CentOS 8 と同じで、TCP Wrapper が廃止され、今までのように /etc/hosts.allow や /etc/hosts.deny で IP アドレスによるアクセス制限がかけられなくなった。ファイアウォール（firewalld）で制限をかけることになる。

