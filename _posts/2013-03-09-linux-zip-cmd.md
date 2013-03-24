---
layout: post
title: "Linux 常用压缩解压命令"
description: "<p>压缩、解压是日常电脑操作中常用的工具，Windows 平台之下，似乎并没有太多的学问，大多数人用一款破解的 WinRAR 全部搞定，开源爱好者可能会选择 <a href='http://sparanoid.com/lab/7z/' target='_blank'>7Zip</a>，而熟练操作 <a href='http://www.ghisler.com/' target='_blank'>Total Commander</a> 的高手，用其内置的 压缩/解压 工具即可。</p><p>本文主要记录 Linux 平台下常用的 压缩/解压 命令，作为日常安装软件时的速查手册，深入分析就没有了。</p><p>别小看了压缩，水很深，比如 LZMA2 算法。更多压缩的学问，以后还会保持关注。</p>"
category: linux
tags: [zip, tar, linux]
---
{% include JB/setup %}

压缩、解压是日常电脑操作中常用的工具，Windows 平台之下，似乎并没有太多的学问，大多数人用一款破解的 WinRAR 全部搞定，开源爱好者可能会选择 [7Zip](http://sparanoid.com/lab/7z/)，而熟练操作 [Total Commander](http://www.ghisler.com/) 的高手，用其内置的 压缩/解压 工具即可。

本文主要记录 Linux 平台下常用的 压缩/解压 命令，作为日常安装软件时的速查手册，深入分析就没有了。

别小看了压缩，水很深，比如 LZMA2 算法。更多压缩的学问，以后还会保持关注。

##1.tar

{% highlight tex %}
$ tar -cf archive.tar foo bar # Create archive.tar from files foo and bar.
$ tar -tvf archive.tar # List all files in archive.tar verbosely.
$ tar -xf archive.tar # Extract all files from archive.tar.

$ tar -zcvf archive.tgz foobar/ # Use gzip

$ tar -zxvf archive.tgz # 解压至当前shell执行目录下
$ tar -zxvf archive.tgz -C foobar/ #解压至指定路径
{% endhighlight%}

##2.zip

{% highlight java %}
$ zip archive.zip foo bar
$ zip -r archive.zip foobar/

$ unzip archive.zip
{% endhighlight%}

##3.option

c – create a new archive

v – verbosely list files which are processed.

f – following is the archive file name

z – filter the archive through gzip

j – filter the archive through bzip2

x – extract files from archive

##4.note

1. .tgz is same as .tar.gz

2. .tbz and .tb2 is same as .tar.bz2

3. In all the above commands v is optional, which lists the file being processed

4. View the tar archive file content without extracting using option tvf

##5. ext


1 ). Extract a single file

`$ tar xvf archive_file.tar /path/to/file`

2 ). Extract a single directory or multiple directories

```java
$ tar xvf archive_file.tar /path/to/dir/
$ tar xvf archive_file.tar /path/to/dir1/ /path/to/dir2/
```

3 ). Extract group of files from  archives using regular expression

`$ tar xvf archive_file.tar –wildcards '*.pl'`

4 ). Adding a file or directory to an existing archive using option -r

```java
$ tar rvf archive_name.tar newfile
$ tar rvf archive_name.tar newdir/
```

*Note: You cannot add file or directory to a compressed archive.*

5 ). Subsection compression

```java
tar cvzpf - somedir | split -b 500m
cat x* > somedir.tar.gz
```

全文完。