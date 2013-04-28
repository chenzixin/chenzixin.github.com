---
layout: post
title: "使用 nginx 测试 Jeyll demo"
description: "<p>最近写前端代码比较多，demo 都放在 Jekyll 的 demo 目录下，每次修改 html 或者 js/css，Jekyll 都要重新生成，太慢了。</p><p>很早就安装好了 nginx，今天把根目录直接指到 jsoops，这个世界瞬间就快了很多。</p>"
category: program
tags: [jekyll, nginx]
---
{% include JB/setup %}

最近写前端代码比较多，demo 都放在 Jekyll 的 demo 目录下，每次修改 html 或者 js/css，jekyll 都要重新生成，太慢了。

很早就安装好了 nginx，今天把根目录直接指到 jsoops，这个世界瞬间就快了很多。

#### 安装命令

`brew install nginx`

#### 安装路径

`/usr/local/Cellar/nginx/1.2.6/`

#### 配置文件

`/usr/local/etc/nginx/nginx.conf`

#### 命令列表

```
nginx -V 查看版本，以及配置文件地址
nginx -v 查看版本
nginx -c filename 指定配置文件
nginx -h 帮助
nginx -s [reload\reopen\stop\quit]
```

#### 常用命令

```
sudo nginx
sudo nginx -s reload
```

#### 配置手册

我只打开了 列目录功能，添加了几个虚拟路径

- 目录：<http://wiki.nginx.org/HttpAutoindexModule>

- 别名：<http://wiki.nginx.org/HttpCoreModule#alias>
