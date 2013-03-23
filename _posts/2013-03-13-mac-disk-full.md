---
layout: post
title: "Linux 磁盘空间管理"
description: "<p>磁盘是 Linux 系统中一项非常重要的资源，如何对其进行有效的管理直接关系到整个系统的性能问题。对 Linux 磁盘管理稍微有一些学习和经验的朋友们应该都知道 df、du 和 fdisk 这三个常用命令：df 用于检查文件系统磁盘占用情况，du 检查磁盘空间占用情况，而 fdisk 用于磁盘分区。</p><p>本文主要针对Mac OS X，讲解 du df 命令。</p>"
category: mac
tags: [mac, linux]
---
{% include JB/setup %}

今天下午开会的时候，MBP 的电池耗尽，回到工位充电，没多久，系统提示：

>Start Up Disk is Almost Full…

网上搜到[这个文章](http://www.ehow.com/how_4592058_start-up-disk-almost-full.html)，回答得不错，条理很清晰。

----

No matter how big your hard disk is, somehow it always gets filled. This can happen due to decreased viligance regarding unneeded files as well as ballooning file sizes. When your start-up disk -- the disk that contains Mac OS X -- is nearly full, your Mac notifies you so you can free space, since your system may crash or behave in unexpected ways if the hard disk gets completely filled.

**Instructions**

1、Delete files you no longer need. Some users allow files to accumulate on the desktop, for example. You can also delete files from your iTunes library -- media files can be quite large.

2、Move files that you need only infrequently to an external disk or USB thumb drive, and access them in that location when you need them.

3、Uninstall programs you don't use. To uninstall a program, open the Applications folder; right-click the program's icon and select "Move to Trash."

4、Empty your browser cache, which contains temporary files from the Web sites you visit. To empty Safari's cache, launch Safari and press "Option-Command-E".

5、Empty the Trash by right-clicking the Trash icon on the dock and selecting "Empty Trash."

----

但是磁盘已满是硬伤，需要了解一些 Linux 磁盘管理的命令。

这里提一件伤心事，这台 MBP 购于2012年12月10日，12,488元，昨天查苹果官网，同款已经调价为 10,988元，现在 12,488的那款，已经升级为 2.6GHZ，这个我其实不太在意，关键的关键，**256GB 闪存**，Oops…

我只能这样安慰自己，虽然只用了三个多月，但是我已经基本适应其操作，并且在这台电脑上，做了很多有价值的事情，因此我具备了冲刺七月的能力，这笔钱，我已经提前赚回来了！

继续磁盘空间的问题。

磁盘是Linux系统中一项非常重要的资源，如何对其进行有效的管理直接关系到整个系统的性能问题。对Linux磁盘管理稍微有一些学习和经验的朋友们应该都知道 df、du 和 fdisk 这三个常用命令：df 用于检查文件系统磁盘占用情况，du 检查磁盘空间占用情况，而 fdisk 用于磁盘分区。

## du 命令

----

**用途**

概述磁盘使用。

**语法**

du \[ -a | -s ] \[ -k ] \[ -m ] \[ -g ] \[ -l ] \[ -r ] \[ -x ] \[ -H | -L ] \[ File ... ]

**描述**

du命令显示用于文件的块的数量。如果指定的 File 参数实际上是一个目录，就要报告该目录内的所有文件。如果没有提供 File 参数，du命令使用当前目录内的文件。

如果 File 参数是一个目录，那么报告的块的数量就是分配到目录中文件以及分配到目录自身的块之和。

指定 -a 标志，报告个体文件中块数量。不管是否使用了 -a 标志，由 File 参数指定的个体文件总是要列出。

指定 -s 标志，报告用于所有指定文件和目录中所有文件的全部块。 

块计数包括每个文件的间接块。块计数是通过 512 字节单位计算的，它与系统使用的群集大小无关。指定 -k 标志，通过 1024 字节单位计算块数。

**注意**

1、具有多个链接的文件只为一个条目计数和书写。

2、由于块计数只基于文件大小，所以在报告的块数中，未分配的块是没有包含进去的。

3、如果du得不到文件属性，或者无法读取目录，它就报告一个错误，并且会影响命令的退出状态。


参数：

<table class='table table-bordered table-hover table-striped'>
<tbody>
<tr>
<th style="width:10%">参数</th>
<th>释义</th>
</tr>
<tr>
<td> -a </td>
<td> 为每个指定文件显示磁盘使用情况，或者为目录中每个文件显示各自磁盘使用情况。将该标志与-s标志进行对比。 </td>
</tr>
<tr>
<td> -g </td>
<td> 用 GB 单位计算块数，而不是用缺省的 512 字节单位。对磁盘使用情况的输出值要用浮点数，这是因为如果用字节为单位的话，值会非常大。 </td>
</tr>
<tr>
<td> -H </td>
<td> 如果在命令行指定了符号链接，du&nbsp;命令将统计链接引用的文件或文件层次结构的大小。 </td>
</tr>
<tr>
<td> -k </td>
<td> 用 1024 字节单位计算块数，而不是用缺省的 512 字节单位。 </td>
</tr>
<tr>
<td> -l </td>
<td> 在文件链接和多链接之间均匀地分配块。根据缺省值，有两个或者更多链接的文件只计数一次。 </td>
</tr>
<tr>
<td> -L </td>
<td> 如果在命令行指定了符号链接或者在文件层次结构的遍历中多次遇到符号链接，则&nbsp;du&nbsp;命令应统计链接引用的文件或文件层次结构的大小。 </td>
</tr>
<tr>
<td> -m </td>
<td> 用 MB 单位计算块数，而不是用缺省的 512 字节单位。对磁盘使用情况的输出值要用浮点数，这是因为如果用字节为单位的话，值会非常大。 </td>
</tr>
<tr>
<td> -r </td>
<td> 报告不可访问的文件或者目录名。此为缺省设置。 </td>
</tr>
<tr>
<td> -s </td>
<td> 为所有指定文件显示整个磁盘使用情况，或者为一个目录中的所有文件显示总的磁盘使用情况。将该标志与-a标志进行对比。 </td>
</tr>
<tr>
<td> -x </td>
<td> 在评估文件大小时，只评估那些与File参数指定的文件或者目录驻留在相同设备上的文件。例如，您可以指定一个在多个设备上包含文件的目录。这种情况下，-x标志就为与目录驻留在相同设备的所有文件显示块的大小。 </td>
</tr>
</tbody></table>

## df 命令

----

**功能**

显示磁盘相关信息

**语法**

df \[-b | -H | -h | -k | -m | -g | -P] \[-ailn] \[-T type] \[-t] \[filesystem ...]


参数：

<table class='table table-bordered table-hover table-striped'><tbody>
<tr>
<th style="width:20%">参数</th>
<th>释义</th>
</tr>
<tr>
<td>-a</td>
<td> 包含全部的文件系统。</td>
</tr>
<tr>
<td>-b</td>
<td> Use (the default) 512-byte blocks. This is only useful as a way to override an BLOCKSIZE specification from the environment.</td>
</tr>
<tr>
<td>-h </td>
<td>以可读性较高的方式来显示信息。</td>
</tr>
<tr>
<td>-H </td>
<td>与-h参数相同，但在计算时是以1000 Bytes为换算单位而非1024 Bytes。</td>
</tr>
<tr>
<td>-k </td>
<td>指定区块大小为1024字节。</td>
</tr>
<tr>
<td>-l </td>
<td>仅显示本地端的文件系统。</td>
</tr>
<tr>
<td>-m </td>
<td>指定区块大小为1048576字节。</td>
</tr>
<tr>
<td>-P </td>
<td>使用POSIX的输出格式。</td>
</tr>
<tr>
<td>-t&lt;文件系统类型&gt; </td>
<td>仅显示指定文件系统类型的磁盘信息。</td>
</tr>
<tr>
<td>-T </td>
<td>显示文件系统的类型。</td>
</tr>
</tbody></table>

不同的操作系统下，参数不尽相同。请使用：

`$ man df`

查看文档。

示例：

`df -h /opt`

[参考51开源社区](http://wiki.51osos.com/wiki/Df)

全文完。
