---
layout: post
title: "查尔斯·巴贝奇的差分机与分析机"
description: "<p>四月初，我从 ITPUB 上转载了一个帖子：<a href='blog/2013/04/04/the-greatest-computer-programmer/'>世界上最伟大的程序员</a>，讲到了高德纳和他的《计算机程序设计艺术》。在四月的最后一天，我终于得见庐山真面，从 <a href='http://www.par-anoia.net/assessment/books/coding/'>www.par-anoia.net</a> 下载到扫描版的电子书。</p><p>我知道我此生都没有办法把它读完，不完全是因为没有时间，主要是因为我没有这个能力。但是偶尔翻看，亦能发现很多有趣，而且有用的东西。</p>"
category: blog
tags: [computer, math]
---
{% include JB/setup %}

四月初，我从 ITPUB 上转载了一个帖子：[世界上最伟大的程序员](blog/2013/04/04/the-greatest-computer-programmer/)，讲到了高德纳和他的《计算机程序设计艺术》。在四月的最后一天，我终于得见庐山真面，从 [www.par-anoia.net](http://www.par-anoia.net/assessment/books/coding/) 下载到扫描版的电子书。

我知道我此生都没有办法把它读完，不完全是因为没有时间，主要是因为我没有这个能力。但是偶尔翻看，亦能发现很多有趣，而且有用的东西。

卷一第一章第一节，《算法》里有一段导言：

<p class='justify'>Many persons who are not conversant with mathematical studies, imagine that because the business of the engine is to give its results in numerical notation, the nature of its processes must consequently be arithmetical and numerical, rather than algebraical and analytical. This is an error. The engine can arrange and combine its numerical quantities exactly as if they were letters or any other general symbols; and in fact it might bring out its results in algebraical notation, were provisions made accordingly.</p>

作者是名副其实的女神：Ada Lovelace，世界上第一位计算机程序员。

这段话可以在[这里](http://history-computer.com/ModernComputer/thinkers/Ada.html)找到上下文，我循着路径，发现了[这个伟大的网站](http://history-computer.com/index.html)。

延伸阅读：

[Lord Byron](http://en.wikipedia.org/wiki/George_Gordon_Byron)

[Anne Isabella Milbanke](http://en.wikipedia.org/wiki/Anne_Isabella_Milbanke) 

[Ada Lovelace](http://en.wikipedia.org/wiki/Ada_Lovelace)

沿着这条路，我们去瞻仰一下现代计算机的起源。

>现实中分析机并未真正被制造出来，但差分机与分析机的思想为现代计算机设计奠定了基础，巴贝奇也因此被称作“计算机之父”。

差分机 和 分析机

差分机又称差分引擎（Difference Engine），是巴贝奇毕生的研究所在。和你想象的可能有些不同，这其实并不是一台一般意义上的「计算器」，当时可以做简单的加减乘除的机械装置已经存在，而巴贝奇的机器也没打算和他们抢工作。准确的说，巴贝奇的机器是一台「多项式求值机」，只要将欲求值的一元多次方程式输入到机器里，机器每运转一轮，就能产生出一个值来。

假设我们以 F(x) = x² + 4 做为例子好了，差分引擎吐出来的结果，就会是：

F(1) = 5，F(2) = 8，F(3) = 13，F(4) = 20 ... etc. 

直到系统停止为止。

巴贝奇耗费了整整十年光阴，于1822年完成了第一台差分机，它可以处理 3 个不同的 5 位数，计算精度达到 6 位小数，当即就演算出好几种函数表。

1834年，巴贝奇设计出了一台更加野心勃勃的机器，称为分析机引擎（Analytical Engine）。列出它的功能可以让人眼睛都突出来：

首先，它的机械结构被分成了「计算单元」和「储存单元」两个部份，其中计算单元不仅内建四则运算，而且还可以「存」四组不同的运算方程式，用穿孔卡片（Punch Card）加载到机器里。

这台机器在设计上甚至有能力进行条件分支（if）、循环、平行处理等程序逻辑，只是巴贝奇的年代自然还没有这些名词的出现。

最后的结果还可以选择印刷、打卡、绘图等多种输出方式，从某些方面来说，它计算、储存、I/O 三项分离的设计，和今日的计算机并无二致，只是最后分析机引擎只停留在了纸上，从没做成实机过。

延伸阅读：

[Charles Babbage](http://en.wikipedia.org/wiki/Charles_Babbage)

[Luigi Menabrea](http://en.wikipedia.org/wiki/Luigi_Menabrea)

[Analytical Engine](http://en.wikipedia.org/wiki/Analytical_engine)




