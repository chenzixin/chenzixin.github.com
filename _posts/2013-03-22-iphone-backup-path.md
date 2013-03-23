---
layout: post
title: "iPhone 在 Mac OS X 下的备份路径"
description: "iPhone 在 Mac OS X 下备份文件的存储路径"
category: blog
tags: [iphone, mac, backup]
---
{% include JB/setup %}

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