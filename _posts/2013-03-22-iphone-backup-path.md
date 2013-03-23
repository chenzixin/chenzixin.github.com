---
layout: post
title: "iPhone 在 Mac OS X 下的备份路径"
description: "<p>研究源于需求。随着年龄的增加，越来越疏于对计算机的打理。想当年在学校，系统稍微有点问题，就潜心捣鼓，甚至熬夜重装系统。但是现在一切都变了。如果不是硬盘吃紧，我绝不会苦苦的寻找这些烦人的路径。</p><p>但同时，你也要相信，一切努力，都会有结果，而且大多时候，会衍生意外的惊喜，只要你能保持这个状态：对美好的事物，要有心动的感觉。</p>"
category: blog
tags: [iphone, mac, backup]
---
{% include JB/setup %}

前言：

研究源于需求。随着年龄的增加，越来越疏于对计算机的打理。想当年在学校，系统稍微有点问题，就潜心捣鼓，甚至熬夜重装系统。但是现在一切都变了。如果不是硬盘吃紧，我绝不会苦苦的寻找这些烦人的路径。

但同时，你也要相信，一切努力，都会有结果，而且大多时候，会衍生意外的惊喜，只要你能保持这个状态：

对美好的事物，要有心动的感觉。

iPhone 在 Mac OS X 下备份文件的存储路径：

>~/Library/application\ support/mobilesync 

只是 Lion 将用户下面的资料库瘾藏了。

可以通过快捷方式进行，在 Finder 下

 `commnd + shift + G`

输入以下路径并回车：

>~/Library/application support/mobilesync 

打开 Backup 里面的就是。

全是自动生成的乱码文件名，只能按时间选择你的备份。

附：ipa 文件的路径

>~/Music/iTunes/iTunes Media/Mobile Applications

注：目录中有空格，在控制台下 `cd` 的技巧

>cd ~/Music/iTunes/iTunes\ Media/Mobile\ Applications

>cd ~/Music/iTunes/'iTunes Media'/'Mobile Applications'

即对空格进行转义，或者将目录名用引号括起来。

全文完。