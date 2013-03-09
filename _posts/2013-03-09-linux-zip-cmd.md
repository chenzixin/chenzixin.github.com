---
layout: post
title: "Linux 常用压缩解压命令"
description: "Linux 常用压缩解压命令"
category: linux
tags: [zip, tar, linux]
---
{% include JB/setup %}

##1.tar
{% highlight ruby %}
tar -cf archive.tar foo bar # Create archive.tar from files foo and bar.
tar -tvf archive.tar # List all files in archive.tar verbosely.
tar -xf archive.tar # Extract all files from archive.tar.

tar -zcvf archive.tgz foobar/ # Use gzip

tar -zxvf archive.tgz #解压至当前shell执行目录下
tar -zxvf archive.tgz -C foobar/ #解压至指定路径
{% endhighlight%}

##2.zip

{% highlight ruby %}
zip archive.zip foo bar
zip -r archive.zip foobar/

unzip archive.zip
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


Extract a single file

`$ tar xvf archive_file.tar /path/to/file`

Extract a single directory or multiple directories

`$ tar xvf archive_file.tar /path/to/dir/`

`$ tar xvf archive_file.tar /path/to/dir1/ /path/to/dir2/`

Extract group of files from  archives using regular expression

`$ tar xvf archive_file.tar –wildcards '*.pl'`

Adding a file or directory to an existing archive using option -r

`$ tar rvf archive_name.tar newfile`

`$ tar rvf archive_name.tar newdir/`

Note: You cannot add file or directory to a compressed archive.

全文完。