---
layout: post
title: "在线考试系统设计"
description: "<p>我曾经管理过一个失败的项目，行政部在线考试系统。历时两个月的开发，测试上线之后，没有担负起一场真正的考试，深以为恨。</p><p>在查过诸多资料之后，我也相信，在线考试，这不是一个简单的系统，也的确难为了那位应届毕业生。在这个系统中的挫折感，再加上一直没有挑战性的活动，和技术关怀的缺失，最终导致他工作不满一年就提出辞职。关于这件事情的反思，我会在以后的文章中详细分析。</p>"
category: program
tags: [online, exam]
---
{% include JB/setup %}

我曾经管理过一个失败的项目，行政部在线考试系统。历时两个月的开发，测试上线之后，没有担负起一场真正的考试，深以为恨。

在查过诸多资料之后，我也相信，在线考试，这不是一个简单的系统，也的确难为了那位应届毕业生。在这个系统中的挫折感，再加上一直没有挑战性的活动，和技术关怀的缺失，最终导致他工作不满一年就提出辞职。关于这件事情的反思，我会在以后的文章中详细分析。

这里回归考试。

因为是自己的过错，这次的失败从未在我的记忆中模糊，一直在寻找重构 或者 重写的机会。今天在OSchina上找到一款开源的在线考试系统：

[项目首页](http://www.tcexam.org/)

[项目文档](http://www.tcexam.org/docs.php)

也在本机安装成功，没有深入试用，但感觉也是一个庞大的系统，折腾了很久，也未能成功的组织一场考试。

先记下安装错误：

>PHP Warning: date(): It is not safe to rely on the system's timezone settings. You are *required* to use the date.timezone setting or the date_default_timezone_set() function….

我查了 phpinfo，时区设置没有问题，参考网上的方法，去除了警告：

{% highlight php %}
<?php
    //文件头
    date_default_timezone_set("PRC");
?>
{% endhighlight %}

接下来一段时间，我会先学习使用这套系统，相信会有助于以后的设计。
