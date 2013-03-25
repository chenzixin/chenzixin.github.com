---
layout: post
title: "简化 Jekyll 的文章编写"
description: "<p>Jekyll 中一个典型的文章发布操作，要输入很长的命令，而且还有等于、引号，有点繁琐。看到网上有高手重写  Rakefile，但是我的 Ruby 水平，连打酱油都不够，更别说 rake 了。</p><p>后来尝试用 Python 脚本调用 Rake 命令，总算还可用。</p>"
category: program
tags: [rake, jekyll, python]
---
{% include JB/setup %}

Jekyll 中一个典型的文章发布操作：

`rake post title='simplify post in jekyll'`

每次都要输入这么多内容，有些烦，于是尝试改进。

## 尝试 Rake
----

Jekyll 是用 Ruby rake 发布文章的，但是我的 Ruby 水平，连打酱油都不够，更别说 rake 了。

按照 rake 的[官方教程](http://rake.rubyforge.org/)做了一个 helloworld 之后，再无进展：

1、在工作目录下，新建默认的 Rakefile

```
$ touch Rakefile
$ subl Rakefile
```
写入以下内容：

```ruby
task :default => [:test]

task :test do
  ruby "test/hello.rb"
end
```

2、编写 hello.rb

```
$ mkdir test
$ touch hello.rb
$ subl hell.rb
```
写入以下内容：

```ruby
def hello
	puts 'hello'
end

hello
```

3、执行 Rake 任务

```
$ ls
Rakefile     test
$ rake
/Users/Christen/.rvm/rubies/ruby-1.9.3-p392/bin/ruby test/hello.rb
hello
```
OK，成功了，不过也仅限于此，时间有限，以后再研究。

参考：

<http://rake.rubyforge.org/>

<https://github.com/jimweirich/rake>

## 试用 Python
----

没写过代码的人，写一个小脚本，也这么费劲：

```python
#!/usr/bin/python
from datetime import date
import os
import re

u_title =  raw_input("Please ENTER the Title:\n")
p_title = re.sub(r'\s+', '-', u_title.strip())

# post
rakecmd = "rake post title=" + "'" + p_title + "'"
os.popen(rakecmd)

# print
now = date.today()
p_date =  now.strftime("%Y-%m-%d")

# info
print 'File has been Created:\n' './_posts/'+ p_date + '-' + p_title.lower() + '.md'
print 'Done...'
```
本来想尝试 [subprocess](http://docs.python.org/2.7/library/subprocess.html#module-subprocess) ，官方的例子执行没有问题，但不能调用 rake，目前不明所以。

`subprocess.call(["ls", "-l"])`

小脚本涉及的知识点：

*   [shebang line](http://en.wikipedia.org/wiki/Shebang)
*   [re](http://docs.python.org/2/library/re.html#re.sub)
*   [date](http://docs.python.org/2/library/datetime.html)
*   [strip](http://docs.python.org/2/library/string.html#string.lstrip)

简单的去除空白：

```python
s = "  \t a string example\t  "
s = s.strip()
s = s.rstrip()
s = s.lstrip()
s = s.strip(' \t\n\r')
```

利用正则表达式：

```python
import re
pat = re.compile(r'\s+')
s = '  \t  foo   \t   bar \t  '
print pat.sub('', s)
```

参考：[stackoverflow](http://stackoverflow.com/questions/1185524/how-to-trim-whitespace-including-tabs)

用法：

```
$ chmod 777 ./post.py
$ ./post.py
Please ENTER the Title:
Test Post
File has been Created:
./_posts/2013-03-25-test-post.md
Done...
```
终于可以少写几个字了，而且比默认的 rake 还有所增强，会自动去除标题中多余的空格！
