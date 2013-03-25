---
layout: post
title: "Jekyll 使用笔记"
description: "<p>整个周末，基本上都是窝在家里，整理 Jekyll 上的文章，修改配置，更新模版，现在总体看来，像个博客的样子了，接下来最重要的，就是坚持写作。</p><p>最初使用 Jekyll ，完全参照官方的入门例子，用 rake 新建文章，用 Mou 编辑 MarkDown，用 git 命令发布。</p><p>如果能一直保持，那肯定不是我。</p><p>折腾和受虐是我的天性。慢慢的，我学会了用 shell 脚本运行本地测试，用 Mac 的 GitHub GUI 程序提交代码，嫌 Mou 速度太慢，直接改用 ST2，为此还用了研究了 ST2 的插件、主题、配色等，现在用起来特别的顺手。今天又写一个<a href='http://www.pyivy.com/program/2013/03/25/simplify-post-in-jekyll/'>Python 脚本</a> 来简化 MD 文件的生成，总体说来，效率提升不了。</p>"
category: program
tags: [jekyll, blog, github]
---
{% include JB/setup %}

整个周末，基本上都是窝在家里，整理 Jekyll 上的文章，修改配置，更新模版，现在总体看来，像个博客的样子了，接下来最重要的，就是坚持写作。

最初使用 Jekyll ，完全参照官方的入门例子，用 rake 新建文章，用 Mou 编辑 MarkDown，用 git 命令发布。

如果能一直保持，那肯定不是我。

折腾和受虐是我的天性。慢慢的，我学会了用 shell 脚本运行本地测试，用 Mac 的 GitHub GUI 程序提交代码，嫌 Mou 速度太慢，直接改用 ST2，为此还用了研究了 ST2 的插件、主题、配色等，现在用起来特别的顺手。今天又写一个 [Python 脚本](http://www.pyivy.com/program/2013/03/25/simplify-post-in-jekyll/) 来简化 MD 文件的生成，总体说来，效率提升不了。

我最初的首页，只是一个简单的文章列表，简陋得令人发指，后来参考[官方的文档](https://github.com/mojombo/jekyll/wiki/Pagination)，终于整出一个像样的首页：

*   看起来有文章摘要了
*   文章支持分页了
*   删除鸡肋导航 手机上看起来更舒服了

个人觉得比较得意是"文章摘要"，我不是按 WP 的风格，取 more 标签之前的内容，而是直接抓取 post.description，然后在 description 中植入 HTML 代码，内容和形式都可以完全控制。在页面的 meta.description 中，参考 [Liquid for Designers](https://github.com/shopify/liquid/wiki/liquid-for-designers) 用 strip_html 过滤 HTML 标签，最后的结果近乎完美。

感觉默认的插入代码的写法过于繁琐，又安装了 [redcarpet](https://github.com/mojombo/jekyll/wiki/Install#pygments-usage) ，插入高亮代码瞬间方便了很多。

折腾至此，差不多了。

这里列出一些资源，为以后的二次折腾打下基础：

*   [Jekyll](https://github.com/mojombo/jekyll) [Blog](http://tom.preston-werner.com)

*   [Jekyll Maillist](https://groups.google.com/forum/?fromgroups#!forum/jekyll-rb)

*   [Jekyll Wiki](https://github.com/mojombo/jekyll/wiki)

*   [Jekyll Sites](https://github.com/mojombo/jekyll/wiki/Sites)

*   [Jekyll-bootstrap](https://github.com/plusjade/jekyll-bootstrap)  [Developer Documentation](http://jekyllbootstrap.com/developers/index.html)


