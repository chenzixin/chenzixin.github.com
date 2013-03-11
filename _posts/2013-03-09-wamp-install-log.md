---
layout: post
title: "Wamp 备忘 TBC"
description: "从 2005 年开始直到今天，我一直在使用 WampServer，感情很深。"
category: program
tags: [wamp]
---
{% include JB/setup %}

[WampServer](http://www.wampserver.com/en/) is a Windows web development environment. 

It allows you to create web applications with Apache2, PHP and a MySQL database.

以上文字摘录于 WampServer 的官网，从 2005 年开始直到今天，我一直在使用 WampServer，感情很深。

我以自己的视角来写这款软件，也是对网事的回忆。

待续...

### Apache 列表页 不能显示ICONS

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

### PHP 上传文件大小限制

修改 php.ini

{% highlight ruby%}
upload_max_filesize = 8M
post_max_size = 10M
memory_limit = 20M
{% endhighlight %}

待续...
