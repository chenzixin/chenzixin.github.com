---
layout: post
title: "我和 Wamp 的故事"
description: "<p>从 2005 年开始直到今天，我一直在使用 WampServer，感情很深。</p><p>我以自己的视角来写这款软件，也是对网事的回忆。</p><p>最初结识 Wamp，记得它的名字还是 Wamp5，是为了在本地搭建一个 Discuz! 论坛，傻瓜式安装，几乎零配置，对当时身为<a href='http://www.pcgames.com.cn' target='_blank'>游戏网</a>编辑的我，再合适不过了。</p>"
category: program
tags: [wamp, ssi, apache, mysql, php]
---
{% include JB/setup %}

[WampServer](http://www.wampserver.com/en/) is a Windows web development environment. 

It allows you to create web applications with Apache2, PHP and a MySQL database.

以上文字摘录于 WampServer 的官网，从 2005 年开始直到今天，我一直在使用 WampServer，感情很深。

我以自己的视角来写这款软件，也是对网事的回忆。

最初结识 Wamp，记得它的名字还是 Wamp5，是为了在本地搭建一个 Discuz! 论坛，傻瓜式安装，几乎零配置，对当时身为[游戏网](http://www.pcgames.com.cn)编辑的我，再合适不过了。

之后的几年，Wamp 从来都是装机必备软件，伺服过的程序，也越来越多：

* WordPress
* SaBlog
* Typecho
* MediaWiki
* DotProject
* DokuWiki

还有各种 API Doc，学习 HTML + JS + CSS 时写的 Demo 等等。

功能亮点：

1、方便的离线/在线状态切换

2、快捷的 MySQL 控制台入口

3、图形化的 PHP 设置和扩展配置

4、80 端口测试

5、图形化的 Apache 模块和 Alias 配置  

6、版本查询方便

7、集成的 phpMyAdmin 非常好用

8、www 目录快捷入口

但在正式转开发之前，基本不懂配置，偶尔遇到一些问题，Google 之后，也都稀里糊涂的解决了，盛赞图形化的模块配置界面。

随着开发经验的积累，逐步倾向于通过

* httpd.conf
* php.ini
* my.ini

来配置，效率更高。

注：不要自己去 Wamp 的安装目录找这些文件，通过 TayIcon 里的菜单去编辑为好。

这里记录两个故障解决方案，以后碰到有代表性的，再补上：

**Apache 列表页 不能显示ICONS**

修改 conf/extra/httpd-autoindex.conf

{% highlight ruby%}
IndexOptions FancyIndexing HTMLTable VersionSort

Alias /icons/ "d:/Wamp/bin/apache/Apache2.2.17/icons/"
 
<Directory "d:/Wamp/bin/apache/Apache2.2.17/icons/">
    Options Indexes MultiViews
    AllowOverride None
    Order allow,deny
    Allow from all
</Directory>
{% endhighlight %}

**PHP 上传文件大小限制**

修改 php.ini

{% highlight ruby%}
upload_max_filesize = 8M
post_max_size = 10M
memory_limit = 20M
{% endhighlight %}

不过，因为转战 Mac OS X，可能鲜有以后。

我有 Mac 上试用过一段时间的 Xampp，虽然也是很优秀的套件，而且跨平台，但未能情深，虽然我坚信这两个转变是对：

1、从闭源转开源

2、从独占平台转跨平台

我的同事曾分享过

1、.htaccess 配置

2、SSI 配置

但我用得不多，谈不上有心得，`以后` 补记。

全文完。
