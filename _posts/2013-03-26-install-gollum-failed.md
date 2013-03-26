---
layout: post
title: "安装 GitHub Wiki 引擎 gollum 失败"
description: "<p>Gollum is a simple wiki system built on top of Git that powers GitHub Wikis.</p><p>Gollum wikis are simply Git repositories that adhere to a specific format. Gollum pages may be written in a variety of formats and can be edited in a number of ways depending on your needs. You can edit your wiki locally.</p><p>看起来很诱人，安装极为顺利，启动立刻报错，囧！</p><p>担心把 Jekyll 的环境折腾坏了，不敢再尝试网上的纠错方法。</p><p>无限期搁置。</p>"
category: program
tags: [ruby, openssl, git, github, wiki]
---
{% include JB/setup %}

A simple, Git-powered wiki with a sweet API and local frontend.

<https://github.com/gollum/gollum>

----

Gollum is a simple wiki system built on top of Git that powers GitHub Wikis.

Gollum wikis are simply Git repositories that adhere to a specific format. Gollum pages may be written in a variety of formats and can be edited in a number of ways depending on your needs. You can edit your wiki locally:

*   With your favorite text editor or IDE (changes will be visible after committing).
*   With the built-in web interface.
*   With the Gollum Ruby API.

----

看起来很诱人，安装极为顺利，启动立刻报错，囧！

担心把 Jekyll 的环境折腾坏了，不敢再尝试网上的纠错方法。

无限期搁置。

安装日志：

```
CChentekiMacBook-Pro:chenzixin Christen$ sudo gem install gollum
Password:
Fetching: mime-types-1.21.gem (100%)
Fetching: diff-lcs-1.2.1.gem (100%)
Fetching: grit-2.5.0.gem (100%)
Fetching: github-markup-0.7.5.gem (100%)
Fetching: github-markdown-0.5.3.gem (100%)
Building native extensions.  This could take a while...
Fetching: rack-1.5.2.gem (100%)
Fetching: rack-protection-1.5.0.gem (100%)
Fetching: tilt-1.3.6.gem (100%)
Fetching: sinatra-1.3.6.gem (100%)
Fetching: mustache-0.99.4.gem (100%)
Fetching: nokogiri-1.5.9.gem (100%)
Building native extensions.  This could take a while...
Fetching: sanitize-2.0.3.gem (100%)
Fetching: useragent-0.4.16.gem (100%)
Fetching: stringex-1.5.1.gem (100%)
Fetching: gollum-2.4.11.gem (100%)
Successfully installed mime-types-1.21
Successfully installed diff-lcs-1.2.1
Successfully installed grit-2.5.0
Successfully installed github-markup-0.7.5
Successfully installed github-markdown-0.5.3
Successfully installed rack-1.5.2
Successfully installed rack-protection-1.5.0
Successfully installed tilt-1.3.6
Successfully installed sinatra-1.3.6
Successfully installed mustache-0.99.4
Successfully installed nokogiri-1.5.9
Successfully installed sanitize-2.0.3
Successfully installed useragent-0.4.16
Successfully installed stringex-1.5.1
Successfully installed gollum-2.4.11
15 gems installed
Installing ri documentation for mime-types-1.21...
Installing ri documentation for diff-lcs-1.2.1...
Installing ri documentation for grit-2.5.0...
Installing ri documentation for github-markup-0.7.5...
Installing ri documentation for github-markdown-0.5.3...
Installing ri documentation for rack-1.5.2...
Installing ri documentation for rack-protection-1.5.0...
Installing ri documentation for tilt-1.3.6...
Installing ri documentation for sinatra-1.3.6...
Installing ri documentation for mustache-0.99.4...
Installing ri documentation for nokogiri-1.5.9...
Installing ri documentation for sanitize-2.0.3...
Installing ri documentation for useragent-0.4.16...
Installing ri documentation for stringex-1.5.1...
Installing ri documentation for gollum-2.4.11...
Installing RDoc documentation for mime-types-1.21...
Installing RDoc documentation for diff-lcs-1.2.1...
Installing RDoc documentation for grit-2.5.0...
Installing RDoc documentation for github-markup-0.7.5...
Installing RDoc documentation for github-markdown-0.5.3...
Installing RDoc documentation for rack-1.5.2...
Installing RDoc documentation for rack-protection-1.5.0...
Installing RDoc documentation for tilt-1.3.6...
Installing RDoc documentation for sinatra-1.3.6...
Installing RDoc documentation for mustache-0.99.4...
Installing RDoc documentation for nokogiri-1.5.9...
Installing RDoc documentation for sanitize-2.0.3...
Installing RDoc documentation for useragent-0.4.16...
Installing RDoc documentation for stringex-1.5.1...
Installing RDoc documentation for gollum-2.4.11...
```

报错信息：

```
ChentekiMacBook-Pro:chenzixin Christen$ gollum --help
/Users/Christen/.rvm/rubies/ruby-1.9.3-p392/lib/ruby/site_ruby/1.9.1/rubygems/custom_require.rb:36:in `require': cannot load such file -- openssl (LoadError)
	from /Users/Christen/.rvm/rubies/ruby-1.9.3-p392/lib/ruby/site_ruby/1.9.1/rubygems/custom_require.rb:36:in `require'
	from /Users/Christen/.rvm/rubies/ruby-1.9.3-p392/lib/ruby/1.9.1/net/https.rb:22:in `<top (required)>'
	from /Users/Christen/.rvm/rubies/ruby-1.9.3-p392/lib/ruby/site_ruby/1.9.1/rubygems/custom_require.rb:36:in `require'
	from /Users/Christen/.rvm/rubies/ruby-1.9.3-p392/lib/ruby/site_ruby/1.9.1/rubygems/custom_require.rb:36:in `require'
	from /Users/Christen/.rvm/gems/ruby-1.9.3-p392/gems/gollum-2.4.11/lib/gollum/gitcode.rb:3:in `<top (required)>'
	from /Users/Christen/.rvm/rubies/ruby-1.9.3-p392/lib/ruby/site_ruby/1.9.1/rubygems/custom_require.rb:36:in `require'
	from /Users/Christen/.rvm/rubies/ruby-1.9.3-p392/lib/ruby/site_ruby/1.9.1/rubygems/custom_require.rb:36:in `require'
	from /Users/Christen/.rvm/gems/ruby-1.9.3-p392/gems/gollum-2.4.11/lib/gollum/markup.rb:8:in `<top (required)>'
	from /Users/Christen/.rvm/rubies/ruby-1.9.3-p392/lib/ruby/site_ruby/1.9.1/rubygems/custom_require.rb:36:in `require'
	from /Users/Christen/.rvm/rubies/ruby-1.9.3-p392/lib/ruby/site_ruby/1.9.1/rubygems/custom_require.rb:36:in `require'
	from /Users/Christen/.rvm/gems/ruby-1.9.3-p392/gems/gollum-2.4.11/lib/gollum.rb:21:in `<top (required)>'
	from /Users/Christen/.rvm/rubies/ruby-1.9.3-p392/lib/ruby/site_ruby/1.9.1/rubygems/custom_require.rb:36:in `require'
	from /Users/Christen/.rvm/rubies/ruby-1.9.3-p392/lib/ruby/site_ruby/1.9.1/rubygems/custom_require.rb:36:in `require'
	from /Users/Christen/.rvm/gems/ruby-1.9.3-p392/gems/gollum-2.4.11/bin/gollum:18:in `<top (required)>'
	from /Users/Christen/.rvm/gems/ruby-1.9.3-p392/bin/gollum:19:in `load'
	from /Users/Christen/.rvm/gems/ruby-1.9.3-p392/bin/gollum:19:in `<main>'
	from /Users/Christen/.rvm/gems/ruby-1.9.3-p392/bin/ruby_noexec_wrapper:14:in `eval'
	from /Users/Christen/.rvm/gems/ruby-1.9.3-p392/bin/ruby_noexec_wrapper:14:in `<main>'
```

这里有一个博客，可供参考：<https://blog.theroux.ca/ruby/Markdown-based-wiki-using-gollum/>

博主的引擎，也是 Jekyll。

