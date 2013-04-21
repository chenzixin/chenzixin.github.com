---
layout: post
title: "Mac OS X 安装 Jekyll 记录"
description: "<p>我知道网上有很多这样的日志，绝不少我这一篇，但网传三分钟建一个 Jekyll Blog，窃以为那只是理想状况，现实生活中，往往是有很多意外的。</p><p>我不知道你是从哪里结识 Jekyll，一个好的引路人，也能节约你不少的时间，比如 <a href='http://jekyllbootstrap.com/' target='_blank'>JekyllBootstrap</a>，用他的 Repository 快速生成，比按照<a href='http://www.ruanyifeng.com/blog/2012/08/blogging_with_jekyll.html' target='_blank'>阮一峰</a>的步骤手工搭建，要快上不少。不过，后者更能让你理解 Jekyll 的运作原理。</p><p>我的工作环境：Mac OS X 10.8.2</p>"
category: program
tags: [jekyll]
---
{% include JB/setup %}

我知道网上有很多这样的日志，绝不少我这一篇，但网传三分钟建一个 Jekyll Blog，窃以为那只是理想状况，现实生活中，往往是有很多意外的。

我不知道你是从哪里结识 Jekyll，一个好的引路人，也能节约你不少的时间，比如 [JekyllBootstrap](http://jekyllbootstrap.com/)，用他的 Repository 快速生成，比按照[阮一峰](http://www.ruanyifeng.com/blog/2012/08/blogging_with_jekyll.html)的步骤手工搭建，要快上不少。不过，后者更能让你理解 Jekyll 的运作原理。

[官方维基](https://github.com/mojombo/jekyll/wiki)

我的工作环境：Mac OS X 10.8.2

## 第一步 Hosted Jekyll


访问 [Jekyll Bootstrap](http://jekyllbootstrap.com/)，按照指引操作（注册 GitHub 账号这里就不说了，非常简单），如果这一步出错：

```java
$ git push origin master

Permission denied (publickey).
fatal: The remote end hung up unexpectedly
```

你可能要生成 SSH Keys，参考文章：

[Generating SSH Keys](https://help.github.com/articles/generating-ssh-keys)

[Git Permission Denied Publickey](http://www.celticwolf.com/blog/2011/02/08/git-permission-denied-publickey/) （可能需要翻墙）

顺利的话，大概两三分钟，你就能看到[自己的页面](http://USERNAME.github.com)。

## 第二步 Run Jekyll Locally

你需要一点点[Ruby](http://www.ruby-lang.org/en/)的基础知识，至少要了解 [RubyGems](http://rubygems.org/)，[rake](http://rubygems.org/gems/rake) 等工具。

安装命令很简单：

`
$ gem install jekyll
`

不过你很可能会遇到以下错误：

{% highlight ruby%}
ERROR:  Error installing jekyll:
	ERROR: Failed to build gem native extension.
...
Results logged to /Library/Ruby/Gems/1.8/gems/fast-stemmer-1.0.2/ext/gem_make.out
{% endhighlight %}

原因：Ruby 版本 1.8.7，太低，推荐升级到 1.9.3 。

建议使用 [RVM](https://rvm.io/)，然而执行安装命令

`
$ \curl -L https://get.rvm.io | bash -s stable --ruby
`

RVM 会自动安装 Ruby 2.0，然后 Gem 安装不错，绕了弯路。

解决方法：

`
$ rvm pkg install openssl
`

注意，成功之后，不要直接遵照提示执行：

`
$ rvm reinstall all --force
`

openssl 的问题会依旧。

如果你已经安装了 2.0.0，卸载：

`
$ rvm remove 2.0.0
`

重新安装1.9.3：

`
$ rvm install 1.9.3 -C --with-openssl-dir=$HOME/.rvm/usr
`

成功之后，再安装 jekyll，以下 11 个工具会安装：

{% highlight ruby%}
Successfully installed liquid-2.4.1
Successfully installed fast-stemmer-1.0.2
Successfully installed classifier-1.3.3
Successfully installed directory_watcher-1.4.1
Successfully installed syntax-1.0.0
Successfully installed maruku-0.6.1
Successfully installed kramdown-0.14.2
Successfully installed yajl-ruby-1.1.0
Successfully installed posix-spawn-0.3.6
Successfully installed pygments.rb-0.3.7
Successfully installed jekyll-0.12.1
11 gems installed
{% endhighlight %}

接下来，你就可以使用

`
$ jekyll --sever
`

本地测试。

发表博客：

`
$ rake post title="Hello World"
`

更多命令，请参考[这里](http://jekyllbootstrap.com/usage/jekyll-quick-start.html)。

## 第三步 Enhance Jekyll


### 语法高亮

参考[这里](https://github.com/mojombo/jekyll/wiki/Install)的 Pygments Usage 。

注：安装 Jekyll 的时候，已经装好了 Pygments 。

第一：生成 样式文件

`$ pygmentize -S default -f html > pygments.css`

注：Windows 下安装 Jekyll 的时候，提示 Pygments 安装成功，但可能无法使用 pygmentize 命令。

解决办法：

```tex
cd c:\Ruby193\lib\ruby\gems\1.9.1\gems\pygments.rb-0.3.7\vendor\pygments-main
python stepup.py install
```

会在 Python\scripts 目录下 生成 pygmentize.exe

拷贝 pygments.css 至 assets/themes/twitter/css

修改 \_includes/themes/twitter/default.html

>任何不以下划线开头的文件和目录都会被复制到生成的网站。

添加

`<link href="{{ ASSET_PATH }}css/pygments.css" rel="stylesheet" type="text/css" media="all">`

第二：测试 代码高亮

{% raw %}
>{% highlight ruby %}
>
>require 'redcarpet'
>
>markdown = Redcarpet.new("Hello World!")
>
>puts markdown.to_html
>
>{% endhighlight %}
{% endraw %}

第三：检查 \_config.yml

`pygments: true`

似乎 显示行号 的功能不好用，参数：linenos 。

找到原因了：

If you use linenos, you might want to include an additional CSS class definition for `lineno` in syntax.css to distinguish the line numbers from the highlighted code.

Pygments 支持的[语言](http://pygments.org/languages/)列表。

注：Windows 下 `invalid byte sequence in GBK` 解决方法：

修改

`c:\Ruby193\lib\ruby\gems\1.9.1\gems\pygments.rb-0.3.7\vendor\pygments-main\`

convertible.rb 27 行

将

`self.content = File.read(File.join(base, name))`

改为：

`self.content = File.read(File.join(base, name), :encoding => "utf-8")`

确保 post.md 保存为 UTF-8 无 BOM 格式才行(EmEditor UTF-8 无签名)。

有些同学在 Win7 下还需要设置环境变量：

{% highlight tex %}
export LC_ALL=zh_CN.UTF-8
export LANG=zh_CN.UTF-8
{% endhighlight %}

在 gitbash 下直接执行即可。


### 定义域名

如果你不想用 http://chenzixin.github.com 这个域名，可以换成自己的域名。

具体方法是在 Repositories 的根目录，新建一个名为CNAME的文本文件，写入你要绑定的域名，比如 www.chenzixin.com 。

如果绑定的是顶级域名，则DNS要新建一条A记录，指向 204.232.175.78 。

修改 \_config.yml


`
production_url : http://www.chenzixin.com
`

就 OK 了。

如果你有多个域名，可以注册多个 GitHub 账号，然后在授权给一个主账号提交项目即可。

>settings -> Manage Collaborators


### 配置评论

注册一个 [Disqus](http://www.disqus.com/) 账号，个性 \_config.yml，如：

`
short_name : chenzixin 
`

即可。

### 添加监测

在 [Google Analytics](https://www.google.com/analytics/) 新增监测，配置

`
tracking_id : 'UA-39101310-1'
`

即可。

至于主题、插件等话题，暂不讨论，目前就想专注写作，以后再看。

### 微软平台

1. 安装 Ruby 1.9.3：rubyinstaller-1.9.3-p392.exe
2. 安装 Ruby Dev Kit：DevKit-tdm-32-4.5.2-20111229-1559-sfx.exe
3. 安装 jekyll

Windows 7 下测试通过。

###延伸阅读

[Template Data](https://github.com/mojombo/jekyll/wiki/Template-Data)

[Liquid Extensions](https://github.com/mojombo/jekyll/wiki/Liquid-Extensions)


全文完。






