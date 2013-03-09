---
layout: post
title: "Wamp 配置备忘"
description: "Wamp 配置备忘"
category: program
tags: [wamp]
---
{% include JB/setup %}

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
