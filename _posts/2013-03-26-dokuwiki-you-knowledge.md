---
layout: post
title: "用 Dokuwiki 管理小团队知识"
description: "<p>DokuWiki 是一个针对小公司文件需求而開發的Wiki引擎。DokuWiki 是用程序设计语言 PHP 开发的并以 GPL 2 发布。DokuWiki 基于文本存储，所以不需要数据库，其数据文件在 Wiki 系统外也是可读的。DokuWiki 的功能齐全，支持 UTF-8，最新版支持中文链接。能够单独编辑页面中的某个章节，能够自动生成目录，适合中小企业、个人使用，用作资料归档、指南、读书笔记等。DokuWiki 安装很简单，默认提供配置工具。</p><p>DokuWiki 是由 Andreas Gohr 在2004年7月开发出来的。7月，第一个官方版本在 en:Freshmeat 发布。一个大的改进是2005年1月重新设计解析程序和渲染程序。新的设计带来了显著的性能改进，使得 DokuWiki 可以应用于更大的文档项目。同时也为 DokuWiki 引入了一种通用的插件接口，简化了插件的开发和管理。2005年4月和7月，在 Linux 發行版 Debian 和 Gentoo Linux 引入 DokuWiki 提高了其知名度。</p>"
category: pmp
tags: [php, wiki, pmp]
---
{% include JB/setup %}

### 一、概述

It’s better when it’s simple.

<p style='text-align:justify; text-justify:inter-ideograph'>
DokuWiki is a simple to use and highly versatile Open Source wiki software that doesn’t require a database. It is loved by users for its clean and readable syntax. The ease of maintenance, backup and integration makes it an administrator’s favorite. Built in access controls and authentication connectors make DokuWiki especially useful in the enterprise context and the large number of plugins contributed by its vibrant community allow for a broad range of use cases beyond a traditional wiki.</p>

<https://www.dokuwiki.org/dokuwiki>

<https://github.com/splitbrain/dokuwiki>

DokuWiki 是一个针对小公司文件需求而開發的Wiki引擎。DokuWiki 是用程序设计语言 PHP 开发的并以 GPL 2 发布。DokuWiki 基于文本存储，所以不需要数据库，其数据文件在 Wiki 系统外也是可读的。DokuWiki 的功能齐全，支持 UTF-8，最新版支持中文链接。能够单独编辑页面中的某个章节，能够自动生成目录，适合中小企业、个人使用，用作资料归档、指南、读书笔记等。DokuWiki 安装很简单，默认提供配置工具。

DokuWiki 是由 Andreas Gohr 在2004年7月开发出来的。7月，第一个官方版本在 en:Freshmeat 发布。一个大的改进是2005年1月重新设计解析程序和渲染程序。新的设计带来了显著的性能改进，使得 DokuWiki 可以应用于更大的文档项目。同时也为 DokuWiki 引入了一种通用的插件接口，简化了插件的开发和管理。2005年4月和7月，在 Linux 發行版 Debian 和 Gentoo Linux 引入 DokuWiki 提高了其知名度。

*   文本存储：DokuWiki 通过txt文件存储页面，不需要数据库。
*   版本控制：DokuWiki 存储每一个 Wiki 页面的所有版本，允许用户比较当前版本和任何历史版本。使用了和 MediaWiki 类似的差异引擎（比较版本间的差异的软件）。通过计时锁定机制，可以防止不同用户编辑同一个页面时产生冲突。
*   访问控制：访问控制可以通过用户管理程序完成，用户管理程序允许定义用户和用户组，以及定义访问控制列表，其中管理员用户可以定义页面和名字空间级别的权限。
*   插件：DokuWiki 具有一个通用的插件接口，这个接口简化插件的开发和维护的过程。目前已经有超过100个可用的插件。管理员用户在插件管理程序的帮助下可以很容易地集成和管理这些插件。
*   模板：Wiki的外观可以自定义。开发社群已经提供了许多不同的模板。
*   国际化和本地化：DokuWiki 全面支持 Unicode（UTF-8），所以可以显示如中文，泰文或希伯来文等语言。目前 DokuWiki 的界面已经有约40种语言。
*   缓存：DokuWiki 存储 Wiki 页面渲染后的的输出，以减少服务器的负载。
*   全文检索：DokuWiki 集成有一个索引搜索引擎，用户可以在 Wiki 上搜索关键字。
*   没有所見即所得的编辑器：DokuWiki 不提供所见即所得的编辑器，但有提供编辑工具条。


### 二、插件

####1. Color
----

<https://www.dokuwiki.org/plugin:color>

Opportunity to write colored text in DokuWiki.

Compatible with DokuWiki 2012-10-13 **Adora Belle** 

```
$ cd lib/plugins
$ mkdir -p color

$ wget https://www.dokuwiki.org/_export/code/plugin:color?codeblock=3 --no-check-certificate -O color/syntax.php
$ wget https://www.dokuwiki.org/_export/code/plugin:color?codeblock=4 --no-check-certificate -O color/colornames.php

$ chmod -R a+rX color
```

**Useage**

```
<color blue/lightgrey>text</color>
```

####2. Arctic
----

侧边栏插件，看起来更像 CMS 了

<https://www.dokuwiki.org/template:arctic>

源代码维护在

<https://github.com/samfisch/dokuwiki-template-arctic>

**Adding the Main Sidebar**

First of all, you would probably like to create the main sidebar, i.e. the sidebar associated with the root namespace. 

You simply have to create a wikipage called ''sidebar''---or whatever you set ''pagename'' to--- and add some links.

```
  ====== Navigation  ======
  [[wiki:playground]]\\
  [[wiki:syntax]]\\
  [[some:more:links]]\\
```

TIP: 

It is possible to create this page right in the wiki. Go to any page of your wiki and change the query string of the URL (in your browser's address bar) to '?id=sidebar'; then just create this page.

>注：在线安装插件，必须给 wiki/lib/plugins read + write 权限

####3. Tag
----

Assign category tags to wiki pages. (previous authors: Esther Brunner)

<https://www.dokuwiki.org/plugin:tag>

####4. Markdownextra
----

<https://www.dokuwiki.org/plugin:markdownextra>

<https://github.com/naokij/dokuwiki-plugin-markdownextra/tarball/master>

更多 Markdown 知识：

<http://daringfireball.net/projects/markdown/>

<http://michelf.ca/projects/php-markdown/extra/>

**Useage**

```
<markdown>
- A
- simple
- list

1. And
2. numbered
3. list

Quite intuitive? *emphasis*, **strong**, etc.
</markdown>
```

####5. rename plugin

DokuWiki 默认不支持词条重命名，这里有几个插件可供选择：

*  [editx](https://www.dokuwiki.org/plugin:editx) ✔ 测试通过
*  [mediarename](https://www.dokuwiki.org/plugin:mediarename) Adora Belle untested.

诚如它的目标：小公司文件需求而開發的Wiki引擎

简明轻快，但是功能不能和 Confluence 相比。

### 三、配置

#### 1. 禁用升级自检

<https://www.dokuwiki.org/update_check>

If you don't want to upgrade to an announced release you can simply increase the number in doku.php. 

note: in older versions, this number was at the top of the file ./conf/msg.

OR

Advanced Settings - updatecheck

Check for updates and security warnings? DokuWiki needs to contact update.dokuwiki.org for this feature.

NO

#### 2. 禁用trace

you can disable it by setting the breadcrumbs config option to 0.


一个不错的个人Wiki：<http://wiki.lynxworks.eu/start>


